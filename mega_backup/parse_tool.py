import os
import json
from typing import Dict, Union, List


class JsonConfigLoader:
    """Load the content of .json config file."""

    def __init__(self, config: str = ""):
        self.config = config

    @property
    def config(self) -> str:
        return self._config

    @config.setter
    def config(self, name: str) -> None:
        if not isinstance(name, str):
            raise FileNotFoundError("Filename has to be string.")
        self._config = name

    @staticmethod
    def is_config(config: str) -> bool:
        return os.path.isfile(config)

    def load_json(self) -> Union[Dict[str, str], None]:
        """Load the json file as Python dictionary."""
        if self.is_config(self._config):
            with open(self._config, encoding="utf-8") as json_f:
                return json.load(json_f)

    def parse_config_paths(self) -> List[str]:
        """
        From the given dictionary get all the absolute paths.

        Example:
        {'path1': 'path/to/file1', ...} -> ['path/to/file1', ...]
        """
        return list(self.load_json().values())

