#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

from .orlylearning_error import ORlyLearningError


class InvalidSessionError(ORlyLearningError):
    def __init__(self):
        super().__init__('the provided session is not valid')
