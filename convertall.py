##Runs terminal command from Python script
##In this case it uses convert command from ImageMagick, each line converts a .pdf file
##into a .png file

import sys
import subprocess

##Type infile after calling Python script
infile=sys.argv[1]


f=open(infile, 'r')
for line in f:
	line=line.strip('\n')
	subprocess.check_call(line, shell=True)
	
f.close()