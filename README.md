### MEGA backup
This package is wrapper of [mega.py](https://github.com/odwyersoftware/mega.py)
that upload your data to your Mega account.

#### Installation
Install the dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```

#### Usage
Define backup paths configuration file:
```
python mega.py --create-conf "~/.config"
```

Add backup path:
```
python mega.py --add-path "~/.nvim"
```

Upload backup archive:
```
python mega.py --upload-backup
```

