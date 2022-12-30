# Reconfigure: A configuration tool for Klipper on Recore

The aim of this project is to produce a GUI allowing easy configuration for simple configurations of klipper to run on Recore.
Any advanced setup that tries to use outputs for different purposes from what they were designed for will not be included.

This means that if you need to do some fancy I2C or SPI connectivity shenanigans, you will need to do so by hand. This app
will not replace the Recore's [thorough Wiki documentation](https://wiki.iagent.no/wiki/Main_Page).

## Warning

At the moment this python script is entirely experimental, and any and all usage of this software should be considered risky.
Use of the configuration output may fail to function or even break your hardware depending on how you wired it up.
We take no responsibility for any damage incurred from non-released versions of the software.

## Requirements

At this stage, to be able to run, you need to have Python3 and the python3-tk library installed.
On Ubuntu you can either use `sudo apt install python3-tk` or `pip3 install tk`.

Then you can run the program with `python reconfigure.py`

### Windows users

Please note that on Windows, to be able to run the script, you need to either launch it from the Python console, or 
from the Powershell. Running it from the DOS (cmd) terminal won't work.