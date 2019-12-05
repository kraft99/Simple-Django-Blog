class NewsLetterException(Exception):
    pass


class EmailAlreadyExistException(NewsLetterException):
    pass


class EmailDoesNotExistException(NewsLetterException):
    pass

