from abc import ABC
from typing import Optional

from requests import Session

from ..exceptions import InvalidSession

class AbstractHandler(ABC):
    def __init__(self, session: Optional[Session] = None):
        self.session = session

    def _check_session(self):
        if not self.session:
            raise InvalidSession()

    def set_proxy(self, proxy: dict):
        if self.session:
            self.session.proxies = proxy
