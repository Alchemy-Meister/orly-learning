class EmailError(Exception):
    pass

class PasswordError(Exception):
    pass

class MissingRegistrationFields(Exception):
    def __init__(self, missing_field, compulsory_fields):
        super().__init__(
            f'missing {repr(missing_field)} registration field, '
            f'the following fields are required: {compulsory_fields}'
        )

class InvalidCredentials(Exception):
    def __init__(self):
        super().__init__('email or password are incorrect')

class InvalidSession(Exception):
    def __init__(self):
        super().__init__('the provided session is not valid')
