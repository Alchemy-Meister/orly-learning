#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

from typing import TypedDict


class __RegistrationCompulsoryFields(TypedDict):
    first_name: str
    last_name: str
    email: str
    password: str


class __RegistrationOptionalFields(TypedDict, total=False):
    country: str
    referrer: str
    recently_viewed_bits: str


class RegistrationFields(
        __RegistrationCompulsoryFields, __RegistrationOptionalFields
):
    pass
