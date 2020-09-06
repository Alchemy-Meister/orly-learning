from typing import Optional, Sequence

from requests import Session

from .typing.auth import RegistrationFields
from .handler import AuthHandler, BookHandler, UserHandler

class ORlyLearningClient():

    def __init__(
            self,
            session: Optional[Session] = None,
            proxy: Optional[dict] = None
    ):
        self._handlers = {
            'auth': AuthHandler(session),
            'book': BookHandler(session),
            'user': UserHandler(session)
        }

        self.set_proxy(proxy)

    def login(self, email: str, password: str):
        self._set_session(self._handlers['auth'].login(email, password))

    def logout(self):
        self._set_session(self._handlers['auth'].logout())

    def register(self, registration_fields: RegistrationFields):
        self._set_session(self._handlers['auth'].register(registration_fields))

    def get_user_info(self) -> Optional[dict]:
        return self._handlers['user'].get_info()

    def get_book_info(self, book_id: str) -> dict:
        return self._handlers['book'].get_info(book_id)

    def get_book_chapters_info(self, book_id: str) -> Sequence[dict]:
        return self._handlers['book'].get_chapters_info(book_id)

    def set_session(
            self, session: Optional[Session], set_proxy: bool = True
    ):
        if session and set_proxy:
            session.proxies = self._handlers['auth'].proxy

        self._set_session(session)

    def set_proxy(self, proxy: Optional[dict] = None):
        if proxy is None:
            proxy = {}

        for handler in self._handlers.values():
            handler.set_proxy(proxy)

    def _set_session(self, session: Optional[Session], set_auth: bool = False):
        for handler_id, handler in self._handlers.items():
            if handler_id != 'auth' or set_auth:
                handler.session = session
