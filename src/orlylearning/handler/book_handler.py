#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

from http import HTTPStatus
from typing import Iterator, Sequence
from urllib.parse import urljoin

from orlylearning.errors import InvalidSessionError

from ..constants.urls import Url

from .abstract_handler import AbstractHandler


class BookHandler(AbstractHandler):

    LEARNING_BOOK = urljoin(Url.LEARNING, '/api/v1/book/{}/')
    LEARNING_BOOK_CHAPTER = urljoin(LEARNING_BOOK, 'chapter/')

    def get_info(self, book_id: str):
        self._check_session()

        response = self.session.get(BookHandler.LEARNING_BOOK.format(book_id))
        if response.status_code == HTTPStatus.UNAUTHORIZED.value:
            raise InvalidSessionError()

        return response.json()


    def get_chapters_info(self, book_id: str) -> Sequence[dict]:
        self._check_session()

        return [
            chapter
            for page_chapters in self.__get_chapters(
                BookHandler.LEARNING_BOOK_CHAPTER.format(book_id)
            )
            for chapter in page_chapters
        ]


    def __get_chapters(self, page_url: str) -> Iterator[list]:
        response = self.session.get(page_url)
        if response.status_code == HTTPStatus.UNAUTHORIZED.value:
            raise InvalidSessionError()

        response = response.json()

        yield response['results']
        if response['next']:
            yield from self.__get_chapters(response['next'])
