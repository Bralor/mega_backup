import sys

from mega_backup.mega_backup import MegaFacade


def main(conf: str, email: str) -> None:
    mega_backup = MegaFacade(conf, email)
    mega_backup.start_session()


if __name__ == "__main__":
    config_file = sys.argv[1]
    email = sys.argv[2]
    main(config_file, email)

