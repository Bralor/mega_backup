import os
import tarfile
from tqdm import tqdm
from typing import List
from datetime import datetime
from traceback import format_exc


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

