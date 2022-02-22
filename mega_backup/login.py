from getpass import getpass

from mega import Mega


class Login:
    def __init__(self, email):
        self.email = email
        self.session = Mega()
        self.password = getpass()
        self.target = "os_backup2021"

    def login_client(self):
        return self.session.login(self.email, self.password)

    def upload_file(self, instance, archive):  # check the parameter
        if (cloud_folder := instance.find(self.target)):
            print("Uploading data...")
            instance.upload(archive, cloud_folder[0])


class AccessLogger:
    """Access the remote Mega account."""

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
    def password(self):
        self._password = getpass()

    def login_client(self):
        """Create session with the credentials to your Mega account."""
        self.session = Mega()
        return self.session.login(self._email, self._password)


