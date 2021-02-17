import os
import sys
import tarfile
from tqdm import tqdm
from typing import List
from getpass import getpass
from datetime import datetime
from traceback import format_exc
from configparser import ConfigParser

from mega import Mega


class Parser:
    def __init__(self, email: str):
        self.email = email
        self._CONF_FILE = "backup.conf"
        self._ALL_PATHS = "PATHS"

    def parse_config(self) -> List[str]:
        config_object = ConfigParser()
        config_object.read(self._CONF_FILE)
        return config_object[self._ALL_PATHS]

    @staticmethod
    def create_absolute_paths(paths):
        return [paths[path] for path in paths if os.path.isdir(paths[path])]


class BackUp:
    def __init__(self, files: List[str]):
        self.files = files
        self.name = self.create_archive_name()

    @staticmethod
    def create_archive_name():
        today = datetime.now().strftime("%d-%m-%Y")
        return f"backup-{today}.tar"

    def write_tar_file(self) -> str:
        writting_progress = tqdm(self.files)

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
            return "Success"


class Login:
    def __init__(self, email, backup_file):
        self.mega = Mega()
        self.email = email
        self.password = getpass()
        self.target = "os_backup2021"
        self.backup_file = backup_file

    def login_client(self):
        return self.mega.login(self.email, self.password)

    def upload_file(self, instance):  # check the parameter
        if (cloud_folder := instance.find(self.target)):
            instance.upload(self.backup_file, cloud_folder[0])
        else:
            pass

