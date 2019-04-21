# Script to extract volume files from Imaris mask statistical output.
# Run the script from the directory that contains all of the Statistics root directories
# and create a directory called 'Volume'
# 22 June 2016- Josh Titlow

import glob
import shutil

mkdir 'Volumes'

dest = 'Volumes'

files = glob.glob('*/*Volume.csv')

for file in files:
    shutil.move(file, dest)