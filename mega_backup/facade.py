from datetime import datetime

from mega_backup.login import Login
from mega_backup.backup import BackupCreator
from mega_backup.parse_tool import JsonConfigLoader


class MegaFacade:
    def __init__(self, email: str):
        self.parse_conf = JsonConfigLoader()
        self.make_back_up = BackupCreator("test")
        self.login = Login(email)

    def start_session(self):
        # sys.argv for the config file
        self.parse_conf.config = "mega_backup/data/matous_backup.json"
        paths: list = self.parse_conf.parse_config_paths()

        self.make_back_up.folders = paths
        self.make_back_up.write_archive(
            datetime.now().strftime(self.make_back_up.format_)
        )

        # remove the new archive
        return paths


