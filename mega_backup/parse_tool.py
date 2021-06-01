import os
from configparser import ConfigParser


class Parser:
    def __init__(self, key: str = "PATHS") -> None:
        self.key = key
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
        return config_object[self.key]

    @staticmethod
    def create_abs_paths(paths) -> list:
        return [
            paths[path]
            for path in paths
            if os.path.isdir(paths[path])
        ]
