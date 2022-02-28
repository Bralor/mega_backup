import pytest

from mega_backup.login import AccessLogger
from mega_backup.tests.test_doubles import PasswordIsNotCorrect
from mega_backup.tests.test_doubles import MegaLogger, NotRegisteredUser


class TestAccessLogger:

    def setup(self):
        self.test = AccessLogger()

    def test_if_property_email_is_empty(self):
        """Property email has to be empty."""
        assert not self.test.email

    def test_given_email_property(self):
        """Check if the property has correct email."""
        email = "foo@bar.com"
        self.test.email = email
        assert self.test.email == "foo@bar.com"

    def test_the_empty_property_password(self):
        """Property password should be empty."""
        assert not self.test.password

    # does not test the function getpass()
    # def test_empty_password_as_property(self):
        # """Check if the property has correct password."""
        # password: str = "foobar"
        # self.test.password = password
        # assert self.test.password == "foobar"

    def test_the_login_method_with_proper_email_and_password_double(self):
        self.test_double = MegaLogger()
        self.test_double.email = "foo@bar.com"
        self.test_double.password = "1234567890A"
        assert self.test_double.login_client() == "Success"

    def test_the_login_method_with_incorrect_email_double(self):
        self.test_double = MegaLogger()
        self.test_double.email = "foo@bar.cz"
        self.test_double.password = "1234567890A"

        with pytest.raises(NotRegisteredUser, match="User not registered"):
            self.test_double.login_client()

    def test_the_login_method_with_incorrect_password_double(self):
        self.test_double = MegaLogger()
        self.test_double.email = "foo@bar.com"
        self.test_double.password = "1234567890a"

        with pytest.raises(PasswordIsNotCorrect, match="Incorrect password"):
            self.test_double.login_client()


    def test_the_uploading_file_into_the_non_existing_folder(self):
        """Create the test double methods for this test function."""
        pass


    def test_the_uploading_file_into_the_existing_folder(self):
        pass
