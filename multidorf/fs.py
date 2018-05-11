from pathlib import Path
import sys
import os


def data_root():
    if sys.platform == 'win32': # windows
        return Path(os.getenv('APPDATA')) / 'multidorf'
    elif sys.platform == 'darwin': # macos TODO
        raise NotImplementedError()
    else: # unix
        return Path.home() / '.config/multidorf'


def instance():
    return data_root() / 'instance'


def download():
    return data_root() / 'download'


def therapist():
    return data_root() / 'therapist'