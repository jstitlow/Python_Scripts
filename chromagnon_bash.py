# Chromagnon bash
#
# -Runs chromagnon channel alignment tool on an entire directory
#
#

import subprocess
import os

# specify directory of reference and target images
ref_dir = ('/usr/people/bioc1301/tmp/chromagnon/cal/')
ref_files = os.listdir(ref_dir)
targ_dir = ('/usr/people/bioc1301/tmp/chromagnon/aligned/')
targ_files = os.listdir(targ_dir)

ref_file = ('/usr/people/bioc1301/tmp/chromagnon/list.csv')
file_list = pd.read_csv(ref_file)
ref_dir = ('/usr/people/bioc1301/data/20190517_AdultBrain_smFISH_MB077c_CamKIIYFP_learning/cal')
targ_dir = ('/usr/people/bioc1301/data/20190517_AdultBrain_smFISH_MB077c_CamKIIYFP_learning/aligned')

for file in file_list.iterrows():
    print ('aligning:',file)
    targ = os.path.join(targ_dir, file.replace('_cal.tif','.tif'))
    ref = os.path.join(ref_dir, file)
    
    # call chromagnon from bash
    export_command = "chromagnon "+targ+" -R "+ref+" -E dv"
    popen = subprocess.Popen(export_command, shell=True, stdout=subprocess.PIPE)
    out, err = popen.communicate()
    output = out.split(':')[0]
    print (out)
