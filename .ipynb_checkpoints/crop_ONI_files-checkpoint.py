#############################################################################
# Crop and concatenate ONI files                                            #
# Josh Titlow- 13 February, 2019                                            #
#                                                                           #
# ---PROCESSING STEPS----                                                   #
# 1. Initiatilize empty array                                               #
# 2. Crop the images                                                        #
# 3. Concatenate                                                            #
# 4. Save as binary (.raw) for Picasso                                      #
#                                                                           #
# ---COMMAND LINE USAGE-----                                                #
# 1. Pass indir and prefix (assumes suffix is .tif)                         #
#############################################################################

import numpy as np
from skimage.util import crop
import os
import sys
<<<<<<< HEAD
import argparse
import tifffile
=======
>>>>>>> 62675e050218d15ed7a8d444d6571f7996f34f09


def main(argList):

    parser= argparse.ArgumentParser()
    parser.add_argument('-indir', help='directory with ONI files')
    parser.add_argument('-file_prefix', help='directory with ONI files')
    args= parser.parse_args(args=argList)
    infiles = os.listdir(args.indir)

<<<<<<< HEAD
    # initiate empty array
    merge = np.empty((0, 1024, 414))

    # crop image and add to array
    for file in infiles:
        if file.startswith(args.file_prefix) and file.endswith('.tif'):
            print ("cropping:", file)
            file_path = os.path.join(args.indir, file)

            im = tifffile.imread(file_path)
            crop_amt = ((0, 0), (0, 0), (610, 0))
            im = crop(im,crop_amt)
            merge = np.concatenate((merge, im), axis=0)

    # make sure data are in correct format
    print ('image shape is:', merge.shape)

    # save file
    print ('saving...')
    #merge.astype('uint16').tofile(os.path.join(args.indir, args.file_prefix+'.raw'))
    merge.astype('uint16').tofile(os.path.join(file_path+'.raw'))
=======
# initiate empty array
merge = np.empty((0, 1024, 414))

# crop image and add to array
for file in infiles:
    if file.startswith(args.file_prefix) and file.endswith('.tif'):
        print "converting", file, " to .tiff"
        file_path = os.path.join(args.indir, file)

        im = tifffile.imread(file_path)
        crop_amt = ((0, 0), (0, 0), (610, 0))
        im = crop(im,crop_amt)
        merge = np.concatenate((merge, im), axis=0)

# make sure data are in correct format
print ('image shape is:', merge.shape)

# save file
merge.astype('uint16').tofile(os.path.join(args.indir, args.file_prefix, '.raw')
>>>>>>> 62675e050218d15ed7a8d444d6571f7996f34f09

if __name__=='__main__':
    main(sys.argv[1:])
