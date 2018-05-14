import os
import subprocess
from pathlib import Path
from sys import platform

if platform == 'win32':
    data_root = Path(os.getenv('APPDATA')) / 'multidorf'
elif platform == 'darwin':
    data_root = Path.home() / 'Library' / 'multidorf'
elif platform == 'linux':
    data_root = Path.home() / '.config/multidorf'
else:
    raise NotImplementedError

instance_dir = data_root / 'instances'
appconfig_file = data_root / 'appconfig.json'


def delete_recursively(directory: Path) -> None:
    """
    Delete a directory recursively
    :rtype: None
    :param directory:Path
    """
    for path in directory.iterdir():
        if path.is_dir():
            delete_recursively(path)
        elif path.is_file():
            path.unlink()
    directory.rmdir()


def browse(directory: Path) -> None:
    """
    :param directory:Path
    :return:None
    """
    if platform == 'win32':
        subprocess.Popen(args=['explorer', '"' + str(directory) + '"'])
    elif platform == 'darwin':  # use 'open' on mac
        os.system('open ' + str(directory))
    elif platform == 'linux':  # use xdg-open I guess lol
        subprocess.Popen(args=['xdg-open', str(directory)])
    else:
        raise NotImplementedError
