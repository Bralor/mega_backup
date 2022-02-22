
class LoginError(Exception):
    """User defined exception."""
    pass


class NotRegisteredUser(LoginError):
    """User defined exception that tells if user is not registered."""

    def __init__(self, message: str):
        self.message = message


class PasswordIsNotCorrect(LoginError):
    """
    User defined exception that occures if user email and password does
    not match.
    """

    def __init__(self, message: str):
        self.message = message


class MegaLogger:
    """Testing double class for the method from the package mega."""

    def __init__(self, email: str = "", password: str = ""):
        self._email = email
        self._password = password

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @email.setter
    def email(self, email: str):
        self._email = email

    @password.setter
    def password(self, password: str):
        self._password = password

    def get_registered_user(self):
        return {"foo@bar.com": "1234567890A"}.get(self._email)

    @staticmethod
    def logged_successfully():
        return "Success"

    def login_client(self):
        if not (password := self.get_registered_user()):
            raise NotRegisteredUser("User not registered!")
        elif password != self._password:
            raise PasswordIsNotCorrect("Incorrect password")
        else:
            return self.logged_successfully()
