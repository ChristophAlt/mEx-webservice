from sanic.exceptions import SanicException


class UserException(SanicException):

    def __init__(self, message):
        super().__init__(message)
