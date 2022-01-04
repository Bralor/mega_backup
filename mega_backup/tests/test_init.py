import pytest

from mega_backup.facade_upd import MegaBackupFacade
from mega_backup.parse_tool import JsonConfigLoader


class TestInitiator:

    def setup(self):
        self.test_instance = MegaBackupFacade("email@foobar.com")

    def test_instance_parameter_email(self):
        """Check the if the instance parameter is correct."""
        assert self.test_instance.username == "email@foobar.com"

    def test_instance_incorrect_parameter_email(self):
        """Check if the instance parameter is NOT correct."""
        assert self.test_instance.username != "foobar@email.com"



class TestJsonLoader:

    def setup(self):
        self.test_instance = JsonConfigLoader("testing_config.json")

    def test_json_config_file_name_parameter(self):
        """Check if the instance parameter 'filename' is correct."""
        assert self.test_instance.filename == "testing_config.json"

    def test_json_config_file_incorrect_name_parameter(self):
        """Check if the instance parameter 'filename' is NOT correct."""
        assert self.test_instance.filename != "foobar.json"

    def test_does_the_config_file_exist(self):
        """Check if the method find existing file."""
        assert self.test_instance.is_config("config.json")

    def test_does_the_incorrect_config_file_exist(self):
        """Check if the method find incorrect file."""
        assert not self.test_instance.is_config("foobar.json")

    def test_load_the_json_config_file_is_not_empty(self):
        """Check if the loaded content of .json file is not an empty dict."""
        assert self.test_instance.load_json() != {}

    def test_load_the_json_config_file_has_key(self):
        """Check if the loaded content of .json file is not an empty dict."""
        assert "cert" in self.test_instance.load_json()

    def test_load_the_incorrect_json_config_file(self):
        """Read the existing .json file and check the incorrect content."""
        assert "pictures" not in self.test_instance.load_json()

