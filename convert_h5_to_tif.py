#############################################################################
# Convert Huygens .h5 file to .tiff                                         #
# Josh Titlow- 9 February, 2019                                             #
#                                                                           #
# Requires add path to indir                                                #
#                                                                           #
# Has code for passing command line arguments                               #
#                                                                           #                                                          #
#############################################################################

import h5py as h5
import numpy as np
import matplotlib.pyplot as plt
import tifffile
import os, sys
import argparse


def main(argList):

    parser= argparse.ArgumentParser()
    parser.add_argument('-indir', help='directory with .h5 files')
    args= parser.parse_args(args=argList)
    infiles = os.listdir(args.indir)

    # Get indir
    indir = args.indir
    infiles = os.listdir(indir)

    # Setup outdir
    #if not os.path.exists(os.path.join(indir, 'aligned_deconvolved')):
    #    os.makedirs(os.path.join(indir, 'aligned_deconvolved'))
    #    outdir = os.path.join(indir, 'aligned_deconvolved')

    for file in infiles:
        if file.endswith('.h5'):
            print ("converting", file, " to .tif")

            # Read H5 file
            file_path = os.path.join(indir, file)
            f = h5.File(file_path)

            # Get list of datasets within the H5 file
            datasetNames = [n for n in f.keys()]

            for n in datasetNames:

                # Get dataset name from .h5 (there is only one dataset in these files)
                datasetName = (n + '/ImageData/Image')
                dset = f.get(datasetName)
                out_file = os.path.join(indir, file.split('.')[0]+'.tif')

                # Convert dataset to numpy array
                dset = np.array(dset)

                # Change data structure to make image-j happy
                print ("changing format from:")
                print (dset.shape)
                dset = np.rollaxis(dset,0,3)
                print(dset.shape)

                #save file
                tifffile.imsave(out_file, dset, imagej = True)

if __name__=='__main__':
    main(sys.argv[1:])
