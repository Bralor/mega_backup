import sys

from mega_backup.back_up import Parser, BackUp


backup_1 = Parser("string")
all_files = backup_1.parse_config()
absolute_paths = backup_1.create_absolute_paths(all_files)

if absolute_paths:
    make_backup = BackUp(absolute_paths)
    result = make_backup.write_tar_file()
    print(result)

