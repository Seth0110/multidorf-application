from pathlib import Path
from sys import platform
import os
import subprocess
import json

if platform == 'win32':
    data_root = Path(os.getenv('APPDATA')) / 'multidorf'
elif platform == 'darwin':
    data_root = None # TODO
else:
    data_root = Path.home() / '.config/multidorf'

instance_dir = data_root / 'instances'
appconfig_file = data_root / 'appconfig.json'



def delete_recursively(directory:Path):
    for path in directory.iterdir():
        if path.is_dir():
            delete_recursively(path)
        elif path.is_file():
            path.unlink()
    directory.rmdir()


def browse(directory:Path):
    if platform == 'win32':
        subprocess.Popen(r'explorer "' + str(directory) + '"')
    elif platform == 'darwin':
        raise NotImplementedError
    else:
        subprocess.Popen('xdg-open ' + str(directory))