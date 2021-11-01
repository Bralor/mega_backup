import pytest

from mega_backup.parse_tool import Parser


class TestParser:
    def setup(self):
        self.config = "foo.conf"
        self.testing = Parser(self.config)

    def test_config_file_available(self):
        """Verify that the name of the config file was providet."""
        assert self.testing.config

    def test_existing_conf_file(self):


