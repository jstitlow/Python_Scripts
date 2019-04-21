# Run from a dir containing .tif files to generate subdirs for FISHquant
# Josh Titlow: 4 June 2016

import os

cwd = os.getcwd()

files = [name for name in os.listdir(cwd) if name.endswith(".tif")]

names = [os.path.splitext(x)[0] for x in files]

subfolders = ['Images','Outlines','Results']

for folder in names:
    os.mkdir(os.path.join(cwd, folder))
    
    for sub in subfolders:
        os.mkdir(os.path.join(cwd, folder, sub))
        