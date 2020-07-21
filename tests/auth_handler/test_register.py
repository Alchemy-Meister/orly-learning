from http import HTTPStatus
import json
from urllib.parse import unquote

import pytest
import responses

from orlylearning.exceptions import (
    EmailError, MissingRegistrationFields, PasswordError
)
from orlylearning.handler import AuthHandler

@pytest.fixture(name='auth')
def init_auth():
    return AuthHandler(None, None)

@responses.activate
def test_missing_registration_fields(auth):
    with pytest.raises(MissingRegistrationFields):
        auth.register({
            'first_name': 'learning',
            'email': 'available.email@domain.com',
            'password': 'valid.P4$$W0RD'
        })

def register_get_callback(_request):
    return (HTTPStatus.OK.value, {}, json.dumps({'valid': True}))

def check_email_callback(request):
    if 'available' in unquote(request.url.split('?')[1]).split('=')[1]:
        return (HTTPStatus.OK.value, {}, json.dumps({'success': True}))

    return (
        HTTPStatus.OK.value, {}, json.dumps(
            {
                'success': False,
                'message': 'This email address is already registered'
            }
        )
    )

def check_password_callback(request):
    request_body = json.loads(request.body)
    if 'valid' in request_body.get('password', ''):
        return (HTTPStatus.OK.value, {}, json.dumps({'valid': True}))

@pytest.fixture(name='response')
def init_response():

    with responses.RequestsMock() as rsps:
        yield rsps

def test_email_not_available(auth, response):
    response.add_callback(
        responses.GET,
        AuthHandler.LEARNING_REGISTER,
        callback=register_get_callback
    )

    response.add_callback(
        responses.GET,
        AuthHandler.LEARNING_EMAIL_CHECK,
        callback=check_email_callback,
        match_querystring=False,
    )

    with pytest.raises(EmailError):
        auth.register({
            'first_name': 'Thomas',
            'last_name': 'Edwards',
            'email': 'repeated.email@domain.com',
            'password': 'abc',
            'country': 'US'
        })

# def test_invalid_password(auth, response):
#     response.add_callback(
#         responses.GET,
#         AuthHandler.LEARNING_REGISTER,
#         callback=register_get_callback
#     )

#     response.add_callback(
#         responses.GET,
#         AuthHandler.LEARNING_EMAIL_CHECK,
#         callback=check_email_callback,
#         match_querystring=False,
#     )

#     response.add_callback(
#         responses.POST,
#         AuthHandler.LEARNING_PASSWORD_CHECK,
#         callback=check_password_callback
#     )
#     with pytest.raises(PasswordError):
#         auth.register({
#             'first_name': 'Thomas',
#             'last_name': 'Edwards',
#             'email': 'available.email@domain.com',
#             'password': 'abc',
#             'country': 'US'
#         })

@pytest.fixture(name='fields')
def init_registration_fields():
    return {
        'first_name': 'Thomas',
        'last_name': 'Edwards',
        'email': 'available.email@domain.com',
        'password': 'valid.P4$$W0RD',
        'country': 'US'
    }

#     def register_post_callback(request):
#         request_body = json.loads(request.body)
#         if 'valid' in request_body.get('password', ''):
#             return (HTTPStatus.BAD_REQUEST, {}, '')

#         return (HTTPStatus.OK.value, logged_headers, '')



#         rsps.add_callback(
#             responses.POST,
#             AuthHandler.LEARNING_REGISTER,
#             callback=register_post_callback
#         )
