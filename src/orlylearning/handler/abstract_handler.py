#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

from abc import ABC
from typing import Optional

from requests import Session

from orlylearning.errors import InvalidSessionError


class AbstractHandler(ABC):
    def __init__(self, session: Optional[Session] = None):
        self.session = session


    def _check_session(self):
        if not self.session:
            raise InvalidSessionError()


    def set_proxy(self, proxy: dict):
        if self.session:
            self.session.proxies = proxy
