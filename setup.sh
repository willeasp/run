#! /bin/bash

if [ $EUID -ne 0 ]
then
    echo "Please run as root to install to path."
    exit
fi

chmod +x run.py
ln -s /home/willster/dev/python/run/run.py /usr/local/bin/run
