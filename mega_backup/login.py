from getpass import getpass

from mega import Mega


class AccessLogger:
    """Access the remote Mega account."""

    def __init__(self, email: str = "", password: str = ""):
        self._email = email
        self.password = password

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

    @staticmethod
    def insert_password():
        return getpass()

    def login_client(self):
        """Create session with the credentials to your Mega account."""
        self.session = Mega()
        return self.session.login(self._email, self.insert_password())

    def upload_file(self, mega_instance, file: str, target: str):
        """
        Upload the file in the parameter 'file' to the folder 'target'
        on your Mega account.
        """
        if (is_available := mega_instance.find(target)):
            print("Uploading data..")
            mega_instance.upload(file, is_available[0])
