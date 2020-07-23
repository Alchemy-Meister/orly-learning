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
        self.proxy = proxy

        self.auth_handler = AuthHandler(session, proxy)
        self.book_handler = BookHandler(session)
        self.user_handler = UserHandler(session)

    def login(self, email: str, password: str):
        self.set_session(self.auth_handler.login(email, password))

    def logout(self):
        self.set_session(self.auth_handler.logout(), set_proxy=False)

    def register(self, registration_fields: RegistrationFields):
        self.set_session(
            self.auth_handler.register(registration_fields), set_proxy=False
        )

    def get_user_info(self) -> Optional[dict]:
        return self.user_handler.get_info()

    def get_book_info(self, book_id: str) -> dict:
        return self.book_handler.get_info(book_id)

    def get_book_chapters_info(self, book_id: str) -> Sequence[dict]:
        return self.book_handler.get_chapters_info(book_id)

    def set_session(
            self, session: Optional[Session], set_proxy: bool = True
    ):
        if session and set_proxy and self.proxy:
            session.proxies = self.proxy

        self.auth_handler.session = session
        self.book_handler.session = session
        self.user_handler.session = session

    def set_proxy(self, proxy: dict):
        self.proxy = proxy

        self.auth_handler.proxy = self.proxy
        self.auth_handler.session.proxies = self.proxy
        self.book_handler.session.proxies = self.proxy
        self.user_handler.session.proxies = self.proxy
