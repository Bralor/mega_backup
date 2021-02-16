import os
import sys
import tarfile
from tqdm import tqdm
from typing import List
from getpass import getpass
from datetime import datetime
from traceback import format_exc
from configparser import ConfigParser


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




# if not sys.argv[1]:
    # print("Usage: python name.py 'username' 'arg2'")
# else:
    # username = sys.argv[1]
    # password = getpass()

# config_object = ConfigParser()
# config_object.read(_CONF_FILE)
# dirs = config_object[_ALL_PATHS]
# abs_paths = [dirs[path] for path in dirs if os.path.isdir(dirs[path])]

# today = datetime.now().strftime("%d-%Y")
# filename = f"os-backup-{today}.tar"
# abs_paths.insert(0, os.path.abspath(filename))

# if os.path.isfile("./make_backup"):
    # os.system(f"./make_backup  '{' '.join(abs_paths)}'")

# mega = Mega()
# m = mega.login(username, password)

# destinated_f = "os_backup2021"
# if (folder := m.find(destinated_f)):
    # m.upload(filename, folder[0])

