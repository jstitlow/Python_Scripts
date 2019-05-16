# Process .ome.tiffs for cshift correction in Chromagnon
#
# 1. Convert from .ome.tiff to .tiff
# 2. Create lists of target files and reference tiles
# 3. Manually copy and past lists into command line to run Chromagnon screen session
#
# ----TO DO----
#
# 1. Could probably combine the lists into a dictionary and iterate through to 
#    run the whole code in Python using subprocess
#
# ----USAGE----
#
# 1. Command > screen -S cshift
# 2. Command > conda activate chromagnon
# 3. Command > chromagnon target_list -R reference_list -E dv
# 4. Saves the aligned files as dv to be deconvolved in Huygens

import numpy as np
import tifffile
import os

# Get infiles
indir = '/Volumes/bioc1301/data/20190313_AdultBrain_MB077c_CamKYFP_smFISH_learning/'
#indir = '/usr/people/bioc1301/data/20190515/'
infiles = os.listdir(indir)

# Setup outdir
if not os.path.exists(os.path.join(indir, 'aligned')):
    os.makedirs(os.path.join(indir, 'aligned'))
    outdir = os.path.join(indir, 'aligned')
else: 
    print ('aligned directory already exists')
    
# Convert .ome.tiff to .tiff 
for file in infiles: 
    if file.endswith('.tif'):
        
        file_path = os.path.join(indir, file)
        print ('old file is:', file_path)
        out_file = os.path.join(outdir, file.split('.')[0]+'.tif')
        
        # change to Chromagnon and Image-J friendly format
        im = tifffile.imread(file_path)
        im = np.rollaxis(im,0,2)
        
        # save the file 
        tifffile.imsave(out_file, im, imagej = True)

        print ('new file is:', out_file)