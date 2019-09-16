# aiida-plumed

AiiDA plugin providing support for Plumed2.

NOTE: This plugin is in a pre-alpha development state and is not currently usable.


# Installation

```shell
git clone https://github.com/ConradJohnston/aiida-plumed .
cd aiida-plumed
pip install -e .  # also installs aiida, if missing (but not postgres)
#pip install -e .[precommit,testing] # install extras for more features
verdi quicksetup  # better to set up a new profile
verdi calculation plugins  # should now show your calclulation plugins
```

# Usage

Here goes a complete example of how to submit a test calculation using this plugin.

# License

MIT

# Contact

conrad.s.johnston@googlemail.com
