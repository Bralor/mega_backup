import os
import sys
from getpass import getpass
from datetime import datetime

from mega import Mega


# enter credentials
if not sys.argv[1]:
    print("Usage: python name.py 'username' 'arg2'")
else:
    username = sys.argv[1]
    password = getpass()

# load file paths
with open("config.txt", mode="r", encoding="utf-8") as conf:
    abs_paths = conf.readlines()  # ["home/matous/Documents, "..", ...]

# make backup tar file
today = datetime.now().strftime("%d-%Y")
filename = f"os-backup-{today}.tar"

# clear and check the names of the dirs
existing_f = [path.strip() for path in abs_paths if os.path.isdir(path.strip())]
existing_f.insert(0, filename)

# make tar file
if os.path.isfile("./make_backup"):
    os.system(f"./make_backup '{' '.join(existing_f)}'")

# mega upload init API
mega = Mega()
m = mega.login(username, password)

# mega upload
destinated_f = "os_backup2021"
if (folder := m.find(destinated_f)):
    m.upload(filename, folder[0])

