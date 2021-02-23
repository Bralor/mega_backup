import os
from configparser import ConfigParser


class Parser:
    def __init__(self, filename: str):
        self.filename = filename
        self._ALL_PATHS = "PATHS"

    def parse_config(self) -> "configparser.SectionProxy":  # incorrect annotation
        config_object = ConfigParser()
        config_object.read(self.filename)
        return config_object[self._ALL_PATHS]

    @staticmethod
    def create_absolute_paths(paths):
        return [
            paths[path]
            for path in paths
            if os.path.isdir(paths[path])
        ]

