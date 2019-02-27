import numpy as np
from skimage.util import crop
import tifffile
import os


# Get files
indir = '/usr/people/bioc1301/data/20190221_NMJ_culture_sggYFP_stability'
infiles = os.listdir(indir)

# Crop image and add to array
for file in infiles:
    file_path = os.path.join(indir, file)
    im = tifffile.imread(file_path)
    im = np.rollaxis(im,0,2)
    im = im.replace(im, (os.path.splitext(im)[0])+'.tif')
    tifffile.imsave('file_path', im, imagej = True)
