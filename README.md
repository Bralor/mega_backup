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
{
    "documents": "/path/to/documents",
    "projects": "/path/to/projects",
    "nvim": "/path/to/.config/nvim"
}
```
Name this file like `my_backup.json` and place him into the folder
`mega_backup/data`.

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

