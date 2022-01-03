### MEGA backup

---

This package is wrapper of [mega.py](https://github.com/odwyersoftware/mega.py)
that uploads your data to your Mega account.

<br>

#### Installation

---

Install the dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```
*note*. for better user experience use the virtual enviroments.

<br>

#### Add configuration file

---

Create CONF file with correct paths (according to the example):
```
[PATHS]
docs = /home/<user>/Documents
pictures = /home/<user>/Pictures
downloads = /home/<user>/Downloads
```
Name this file like `backup.conf` and place him into the root folder.

<br>

#### Usage

---

You can use a little help:
```
$ python mega_backup/cli.py -h
usage: cli.py [-h] [-add_conf 'config_file'] ...
```

Backup your data (after creating config file) to the Mega account (with your
account email address):
```
python mega_backup/cli.py --backup "your_email"
```

Add single backup path to your config file:
```
python mega.py --add_path "~/.nvim"
```

<br>

