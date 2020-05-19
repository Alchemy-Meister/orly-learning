from os.path import abspath, dirname, join

from urllib3.connection import HTTPHeaderDict
import pytest

PATH = abspath(dirname(__file__))

@pytest.fixture
def logged_headers():
    headers = HTTPHeaderDict()
    with open(join(PATH, 'session_cookies.txt'), 'r') as cookies_file:
        cookies = cookies_file.read().splitlines()

    for cookie in cookies:
        headers.add('set-cookie', cookie)

    return headers
