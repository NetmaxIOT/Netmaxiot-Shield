#!/usr/bin/env bash

##################################################3
# Netmax iot python 3 installer ##################3
apt-get install python3-dev libi2c-dev
cd i2c-tools-3.1.0/py-smbus
python3 setup.py build
python3 setup.py install

#################
