import os
import tarfile
from tqdm import tqdm
from typing import List
from datetime import datetime
from traceback import format_exc
from typing import List


class BackUp:
    def __init__(self):
        self.abs_paths = []
        self.name = self.create_archive_name()

    @property
    def abs_paths(self):
        """List of absolute paths"""
        return self._abs_paths

    @abs_paths.setter
    def abs_paths(self, vals):
        self._abs_paths = vals

    @staticmethod
    def create_archive_name():
        today = datetime.now().strftime("%d-%m-%Y")
        return f"backup-{today}.tar"

    def write_tar_file(self) -> str:
        writting_progress = tqdm(self._abs_paths)

        try:
            tar_file = tarfile.open(self.name, mode="w:gz")  # open for gzip compressed writting

        except BaseException:
            err = format_exc()
            return err
        else:
            for file in writting_progress:
                tar_file.add(file)
                writting_progress.set_description(f"Compressing {file}")

            tar_file.close()
            return "Compressing complete!"

    @staticmethod
    def remove_local_archive(file: str) -> None:
        if os.path.exists(file):
            os.remove(file)
            print(f"{file} removed")
        else:
            print(f"{file} does not exist")


class BackupCreator:
    """Create a backup folder from the given directories."""

    def __init__(self, name: str, folders: List[str]):
        self.name = name
        self.folders = folders
        self.format_: str = "%d-%m-%Y"

    def create_name(self, date: str) -> str:
        """Create a new name for the .tar archive."""
        return f"{self.name}-{date}.tar"

    def write_archive(self, date: str, mod: str = "w:gz") -> None:
        """
        Create a new .tar archive with the given name as a parameter 'filename'.

        Example:
        date = "11-11-2011"
        self.name = "test"
        -> filename = "test-11-11-2011.tar"
        """
        filename = self.create_name(date)
        progress = tqdm(self.folders)

        with tarfile.open(filename, mod) as tar_ar:
            for dir_ in progress:
                tar_ar.add(dir_)
                progress.set_description(f"Compressing {dir_}")


