class UserNotFound(Exception):
    """
        Exception raised when User is Not Found.
    """
    def __init__(self, message="User is Not Found"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class NonceSignatureNotCorrect(Exception):
    """
        Exception raised nonce is not correct.
    """

    def __init__(self, message="nonce is not correct"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message



class MissingParameter(Exception):
    """
        Exception raised when User is Not Found.
    """

    def __init__(self, message="missing parameter"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message
