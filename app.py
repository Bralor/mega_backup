import argparse

from mega_backup.mega_backup import MegaFacade


def backup(email: str) -> None:
    mega_backup = MegaFacade(email)
    mega_backup.start_session()


def upload(file: str, email: str) -> None:
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--backup",
                        action="store",
                        metavar="VAR",
                        nargs=1,
                        help="Read a configuration file then create and upload \
                        archive to MEGA.nz")
    parser.add_argument("-u", "--upload",
                        action="store",
                        metavar="VAR",
                        nargs=2,
                        help="Find the file and upload to MEGA.nz")
    args = parser.parse_args()

    if args.backup and len(args.backup) == 1:
        backup(args.backup[0])

    elif args.upload:
        upload(args.upload[0], args.upload[1])

    elif args:
        parser.print_help()

