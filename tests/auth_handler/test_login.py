from http import HTTPStatus
import json

import pytest
import responses

from orlylearning.exceptions import InvalidCredentials
from orlylearning.handler import AuthHandler

@pytest.fixture(name='auth')
def init_auth():
    return AuthHandler(None, None)

@pytest.fixture(name='_response')
def init_response(logged_headers):
    def login_callback(request):
        request_body = json.loads(request.body)
        if (
                'valid' in request_body.get('email', '')
                and 'valid' in request_body.get('password', '')
        ):

            return (HTTPStatus.OK.value, logged_headers, '')

        return (HTTPStatus.BAD_REQUEST, {}, '')

    with responses.RequestsMock() as rsps:
        rsps.add_callback(
            responses.POST, AuthHandler.OREILLY_LOGIN, callback=login_callback
        )
        yield rsps

def test_authorized_login(auth, _response, logged_headers):
    session = auth.login('valid-email', 'valid-password')
    session_cookie_names = list(session.cookies.get_dict().keys())
    headers_cookies = logged_headers['set-cookie']
    assert all(
        cookie_name in headers_cookies
        for cookie_name in session_cookie_names
    )

def test_unauthorized_login(auth, _response):
    with pytest.raises(InvalidCredentials):
        auth.login('wrong-email', 'wrong-password')
