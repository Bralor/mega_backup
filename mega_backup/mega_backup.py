from mega_backup.parse_tool import Parser
from mega_backup.backup import BackUp
from mega_backup.login import Login


class MegaFacade:
    def __init__(self, conf: str, email: str):
        self.parse_conf = Parser(conf)
        self.make_back_up = BackUp()
        self.login = Login(email)

    def start_session(self):
        abs_path = self.parse_conf.create_absolute_paths(self.parse_conf.parse_config())
        self.make_back_up.abs_paths = abs_path
        self.make_back_up.write_tar_file()
        session = self.login.login_client()
        self.login.upload_file(session, self.make_back_up.name)
        self.make_back_up.remove_local_archive(self.make_back_up.name)

