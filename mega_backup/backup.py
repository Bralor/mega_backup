import os
import tarfile
from typing import List
from datetime import datetime

from tqdm import tqdm


class BackupCreator:
    """Create an archive that contains all the given paths."""

    def __init__(self, name: str, folders: List[str]) -> None:
        self.name = name
        self.folders = folders
        self.format_: str = "%d-%m-%Y"

    def create_name(self, date: str) -> str:
        """
        Return a new name for the tar archive.

        :param date: mandatory parameter with the given date.
        :return: a string with the name.

        :Example:

        >>> self.name = "foo"
        >>> arch = self.create_name("11-11-2011")
        >>> arch
        "foo-11-11-2011.tar"
        """
        return f"{self.name}-{date}.tar"

    def write_archive(self, date: str, mod: str = "w:gz") -> None:
        """
        Create a new .tar archive in current directory.

        :param date: a string with date.
        :param mod: a string with specific mode for tarfile creating.
        """
        filename = self.create_name(date)
        progress = tqdm(self.folders)

        with tarfile.open(filename, mod) as tar_ar:
            for dir_ in progress:
                tar_ar.add(dir_)
                progress.set_description(f"Compressing {dir_}")


    @staticmethod
    def remove_archive(filename: str) -> str:
        """
        Remove the archive that has been already send.

        :param filename: a name of the archive.
        :rtype param: string

        :Example:
        >>> self.remove_archive("foobar-11-11-2011.tar")
        >>> import os
        >>> "foobar-11-11-2011.tar" in os.listdir()
        False
        """
        try:
            os.remove(filename)

        except FileNotFoundError:
            msg: str = f"There is no such file, {filename}"
        else:
            msg: str = f"{filename} successfully removed"
        finally:
            return msg
