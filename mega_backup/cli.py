import argparse

from facade import MegaFacade


def backup(email: str) -> None:
    mega_backup = MegaFacade(email)
    mega_backup.start_session()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--add_conf",
                        action="store",
                        metavar="'config_file'",
                        nargs=1,
                        help="add a JSON file with paths")
    parser.add_argument("--backup",
                        action="store",
                        metavar="'email_address'",
                        nargs=1,
                        help="read a configuration file then log in with email"
                        )
    parser.add_argument("--add_path",
                        action="store",
                        metavar="'/abs/path/to/file'",
                        nargs=1,
                        help="add a single path to yout JSON config.")
    args = parser.parse_args()

    if args.backup:
        print("MEGA BACKUP: backup the files..")
        backup(args.backup[0])
    elif args.add_conf:
        print("MEGA BACKUP: adding file..")
        # upload(args.upload[0], args.upload[1])
    elif args.add_path:
        print("MEGA BACKUP: adding path to the JSON file..")
    else:
        parser.print_help()

