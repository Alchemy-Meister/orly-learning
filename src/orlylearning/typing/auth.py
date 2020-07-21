from typing import Optional, TypedDict

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
