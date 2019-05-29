
# Chromagnon bash
#
# -Runs chromagnon channel alignment tool on an entire directory
#
#

import subprocess
import os

flag = ('-h')
export_command = "chromagnon "+flag
popen = subprocess.Popen(export_command, shell=True, stdout=subprocess.PIPE)
out, err = popen.communicate()
print out
