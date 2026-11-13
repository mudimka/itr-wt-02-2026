class AppException(Exception):
    """Базовый класс"""


class InvalidArgumentException(AppException):
    pass


class UserNotFoundException(AppException):
    pass
