import os
import json
from typing import Dict, Union, List


class JsonConfigLoader:
    """Load the content of .json config file."""

    def __init__(self, filename: str = ""):
        self.filename = filename

    @property
    def filename(self) -> str:
        return self._filename

    @filename.setter
    def filename(self, name: str) -> None:
        if not isinstance(name, str):
            raise FileNotFoundError("Filename has to be string.")
        self._filename = name

    @staticmethod
    def is_config(filename: str) -> bool:
        """If the given filename exists, return True. Otherwise False."""
        return os.path.isfile(filename)

    def load_json(self) -> Union[Dict[str, str], None]:
        """Load the json file as Python dictionary."""
        if self.is_config(self._filename):
            with open(self._filename, encoding="utf-8") as json_f:
                return json.load(json_f)

    def parse_config_paths(self) -> List[str]:
        """
        From the given dictionary get all the absolute paths.

        Example: {'path1': 'path/to/file1', ...} -> ['path/to/file1', ...]
        """
        return list(self.load_json().values())

