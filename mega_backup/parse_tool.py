import os
import json
from typing import Dict, Union, List

from configparser import ConfigParser


class Parser:
    def __init__(self, config: str, keyname: str = "PATHS") -> None:
        self.config = config
        self.keyname = keyname
        self.config = self.find_config().pop()

    @staticmethod
    def find_config() -> list:
        return [
            file
            for file in os.listdir()
            if os.path.splitext(file)[1] == ".conf"
        ]

    def check_config(self):
        if not self.config:
            raise AssertionError("Configuration file with paths is missing")
        else:
            print(f"Config file found: {self.config}")

    def parse_config(self):
        config_object = ConfigParser()
        config_object.read(self.config)
        return config_object[self.keyname]

    @staticmethod
    def create_abs_paths(paths) -> list:
        return [
            paths[path]
            for path in paths
            if os.path.isdir(paths[path])
        ]


class JsonConfigLoader:
    """Load the content of .json config file."""

    def __init__(self, filename: str):
        self.filename = filename

    @staticmethod
    def is_config(filename: str) -> bool:
        return os.path.isfile(filename)

    def load_json(self) -> Union[Dict[str, str], None]:
        """Check if the .json file exists and return its content."""
        if self.is_config(self.filename):
            with open(self.filename, encoding="utf-8") as json_f:
                return json.load(json_f)

    # read the .json file and parse the file paths
    def parse_config_paths(self) -> List[str]:
        """
        From the given dictionary get all the absolute paths.

        Example: {'path1': 'path/to/file1', ...} -> ['path/to/file1', ...]
        """
        return list(self.load_json().values())

