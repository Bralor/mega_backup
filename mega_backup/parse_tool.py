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
        """
        Verify if the given config file exists.

        :Example:
        >>> print(is_config("mega_backup/data/testing_config.json"))
        True
        >>> print(is_config("testing_config.json"))
        False
        """
        return os.path.isfile(config)

    def load_json(self) -> Union[Dict[str, str], None]:
        """
        Return the dictionary with key-value pairs parsed from the config file.

        :Example:
        >>> jl = JsonConfigLoader()
        >>> jl.config = "mega_backup/data/testing_config.json"
        >>> print(jl.load_json())
        {'cert': '/path/to/certificates', 'documents': '/path/to/documents', ...}
        """
        if self.is_config(self._config):
            with open(self._config, encoding="utf-8") as json_f:
                return json.load(json_f)

    def parse_config_paths(self) -> List[str]:
        """
        From the given dictionary get all the absolute paths.

        :Example:
        >>> jl = JsonConfigLoader()
        >>> jl.config = "mega_backup/data/testing_config.json"
        >>> jl.parse_config_paths()
        ['/path/to/certificates', '/path/to/documents', ... ]
        """
        return list(self.load_json().values())

