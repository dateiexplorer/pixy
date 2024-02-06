import configparser as cp
import getpass
import os
import subprocess
import sys


def exec_pip(username, passphrase, proxy):
    cmd = [sys.executable, '-m', 'pip', '--proxy',
           f'http://{username}:{passphrase}@{proxy}']
    cmd.extend(sys.argv[1:])

    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError as e:
        pass


def main():
    # Load configuration, read the config files in the given order.
    # Special user configs overwrite system widge configs.
    config = cp.ConfigParser()
    config.read([
        '/etc/pixyconfig',
        os.path.expanduser('~/.config/pixy/config'),
        os.path.expanduser('~/.pixyconfig'),
        '.pixyconfig'
    ])

    username = config.get('auth', 'username')
    proxy = config.get('auth', 'proxy')

    # Get passphrase from input stream
    passphrase = getpass.getpass(
        prompt=f"Enter passphrase for '{username}@{proxy}': ")

    exec_pip(username, passphrase, proxy)


if __name__ == '__main__':
    main()
