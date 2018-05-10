import sys
import os
from pathlib import PosixPath, WindowsPath, Path
import tkinter


def data_directory():
    if sys.platform == 'win32': # windows
    	return Path(os.getenv('APPDATA')) / 'multidorf'
    elif sys.platform == 'darwin': # macos
        raise NotImplementedError()
    else: # unix
        return Path.home() / '.config/multidorf'


def main():
    dir = data_directory()
    dir.mkdir(parents=True, exist_ok=True)
    dlDir = dir / 'download'
    dlDir.mkdir(exist_ok=True)
    instanceDir = dir / 'instance'
    instanceDir.mkdir(exist_ok=True)


if __name__ == '__main__':
    main()