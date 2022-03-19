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
        self.test_instance = JsonConfigLoader(
            "mega_backup/data/testing_config.json"
        )

    def test_json_config_file_name_parameter(self):
        assert self.test_instance.config == \
            "mega_backup/data/testing_config.json"

    def test_json_config_file_incorrect_name_parameter(self):
        assert self.test_instance.config != \
            "mega_backup/data/foobar.json"

    def test_does_the_config_file_exist(self):
        assert self.test_instance.is_config(
            "mega_backup/data/testing_config.json"
        )

    def test_does_the_incorrect_config_file_exist(self):
        assert not self.test_instance.is_config(
            "mega_backup/data/foobar.json"
        )

    def test_load_the_json_config_file_is_not_empty(self):
        assert self.test_instance.load_json() != {}

    def test_load_the_json_config_file_has_key(self):
        assert "cert" in self.test_instance.load_json()

    def test_load_the_incorrect_json_config_file(self):
        """Read the existing .json file and check the incorrect content."""
        assert "pictures" not in self.test_instance.load_json()

    def test_collect_all_given_paths(self):
        """Get all the correct paths from the given .json file."""
        assert "/path/to/certificates" in \
            self.test_instance.parse_config_paths()

    def test_collect_incorrect_given_paths(self):
        """Get all the incorrect paths from the given .json file."""
        assert "/path/to/another/certificates" not in \
            self.test_instance.parse_config_paths()
