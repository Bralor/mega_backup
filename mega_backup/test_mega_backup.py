import os
import pytest

from mega_backup.parse_tool import Parser


class TestParser:
    def setup(self):
        self.testing = Parser()

    def test_find_config(self):
        assert self.testing.find_config()

    def test_check_config(self, capfd):
        self.testing.check_config()
        stdout = capfd.readouterr()[0]
        assert stdout.startswith("Config file found:")

    def test_parse_config(self):
        paths = self.testing.parse_config()
        results = [path for path in paths]
        assert results

    def test_correct_abs_path(self):
        testing_path = {"foo": "mega_backup/"}
        assert self.testing.create_abs_paths(testing_path)

    def test_incorrect_abs_path(self):
        testing_path = {"foo": "bar"}
        assert not self.testing.create_abs_paths(testing_path)

