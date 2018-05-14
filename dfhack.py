def dfhack_for_df(version) -> dict:
    return list_dfhack()[version]


def list_dfhack() -> dict:
    return {'0.44.10': {
        'version': '0.44.10-alpha1',
        'windows': {
            'x86': 'https://github.com/DFHack/dfhack/releases/download/0.44.10-alpha1/dfhack-0.44.10-alpha1-Windows-32.zip',
            'x86_64': 'https://github.com/DFHack/dfhack/releases/download/0.44.10-alpha1/dfhack-0.44.10-alpha1-Windows-64.zip',
        },
        'linux': {
            'x86': {
                'gcc-7': 'https://github.com/DFHack/dfhack/releases/download/0.44.10-alpha1/dfhack-0.44.10-alpha1-Linux-32-gcc-7.tar.bz2',
                'gcc-4.8': 'https://github.com/DFHack/dfhack/releases/download/0.44.10-alpha1/dfhack-0.44.10-alpha1-Linux-32-gcc-4.8.tar.bz2',
            },
            'x86_64': {
                'gcc-7': 'https://github.com/DFHack/dfhack/releases/download/0.44.10-alpha1/dfhack-0.44.10-alpha1-Linux-64-gcc-7.tar.bz2',
                'gcc-4.8': 'https://github.com/DFHack/dfhack/releases/download/0.44.10-alpha1/dfhack-0.44.10-alpha1-Linux-64-gcc-4.8.tar.bz2',
            }
        },
        'mac': {
            'x86': {
                'gcc-4.8': 'https://github.com/DFHack/dfhack/releases/download/0.44.10-alpha1/dfhack-0.44.10-alpha1-OSX-32-gcc-4.8.5.tar.bz2',
                'gcc-7': 'https://github.com/DFHack/dfhack/releases/download/0.44.10-alpha1/dfhack-0.44.10-alpha1-OSX-32-gcc-7.3.0.tar.bz2',
            },
            'x86_64': {
                'gcc-4.8': 'https://github.com/DFHack/dfhack/releases/download/0.44.10-alpha1/dfhack-0.44.10-alpha1-OSX-64-gcc-4.8.5.tar.bz2',
                'gcc-7': 'https://github.com/DFHack/dfhack/releases/download/0.44.10-alpha1/dfhack-0.44.10-alpha1-OSX-64-gcc-7.3.0.tar.bz2',
            },
        }
    }}
