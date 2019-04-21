# !/usr/bin/python

import os, sys


s = "Arp3-0.png"

os.rename("s","s[:-6]")



# This works better

[os.rename(f, f.replace('FindFoci-MAX_12', '12')) for f in os.listdir('.') if not f.startswith('.')]