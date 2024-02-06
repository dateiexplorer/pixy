import configparser as cp
import getpass
import os
import subprocess
import sys
import urllib.parse


def exec_pip(env = os.environ.copy()):
    cmd = [
        sys.executable,
        "-m",
        "pip",
    ]
    cmd.extend(sys.argv[1:])

    try:
        subprocess.check_call(cmd, env=env)
    except subprocess.CalledProcessError:
        pass


def main():
    # Load configuration, read the config files in the given order.
    # Special user configs overwrite system widge configs.
    config = cp.ConfigParser()
    config.read(
        [
            "/etc/pixyconfig",
            os.path.expanduser("~/.config/pixy/config"),
            os.path.expanduser("~/.pixyconfig"),
            ".pixyconfig",
        ]
    )

    username = config.get("auth", "username")
    proxy = config.get("auth", "proxy")
    password_required = bool(username)

    env = os.environ.copy()
    if not proxy: 
        print("No proxy is set in the config. Defaulting to normal pip.")
    elif password_required:
        # Get passphrase from input stream.
        passphrase = getpass.getpass(prompt=f"Enter passphrase for '{username}@{proxy}': ")
        
        # Encode username and passphrase.
        username = urllib.parse.quote(username) 
        passphrase = urllib.parse.quote(passphrase)
        
        # Set environment variable.
        env["PIP_PROXY"] = f"http://{username}:{passphrase}@{proxy}"

    exec_pip(env)


if __name__ == "__main__":
    main()
