# pixy

Pixy is a helper command line tool to use all your lovely pip commands from
behind a proxy.

## Usage

To use pixy, you'll need a configuration file with the following content:
```
[auth]
username = <username>
proxy = <proxy>
```

This configuration can be stored system wide or on a per user basis.
The tool reads in the configuration from the following locations (least
files will overwrite the configurations made in previous files):

* `/etc/pixy/config`
* `~/.config/pixy/config` (`.config` folder in the users home directory)
* `~/.pixyconfig` (file in the users home directory)
* `.pixyconfig` (file in the current directory)

Now you'll be able to use pip via the pixy command from behind the proxy.

Example to install pandas (a popular python package) from behind a proxy using
pixy:
```
pixy install -U pandas

# Original pip command:
# pip install -U pandas
```

You'll be asked for a password if the proxy needs a user authentication.

> Note: pixy supports pips isolated build environments by settings the
> `PIP_PROXY` environment variable in a subprocess.