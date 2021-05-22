import os
import pytest


class TestParser:
    def test_if_conf_exists(self):
        assert "backup.conf" in os.listdir()

