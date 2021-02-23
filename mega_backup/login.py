from getpass import getpass

from mega import Mega


class Login:
    def __init__(self, email):
        self.email = email
        self.mega = Mega()
        self.password = getpass()
        self.target = "os_backup2021"

    def login_client(self):
        return self.mega.login(self.email, self.password)

    def upload_file(self, instance, archive):  # check the parameter
        if (cloud_folder := instance.find(self.target)):
            print("Uploading data...")
            instance.upload(archive, cloud_folder[0])

