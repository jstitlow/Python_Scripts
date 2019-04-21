# Script to extract pixel intensities from centroid coordinates
# Created: 9 August 2018
#
# Requires a directory of single channel .tiff images
# Requires the '_FISH-QUANT_all_spots_yymmdd.csv' file from a FQ bash run
#     > add the folowing columns to the FQ.CSV file: 'X_pix', 'Y_pix', and 'Z_pix'
#     > populate each column with the pixel coordinates that correspond to centroid position values
#         > i.e., X_pix = ROUND((Pos_X/n),0)    where n=pixel size
#
# TODO:
#
# Write centroid coordinate to pixel coordinate calculation into Python script
# Append list of pixel values to the FQ.csv file

import os
from skimage import io
import pandas as pd
import numpy

image_dir ='/Users/joshtitlow/Desktop/airyscan/images/smFISH/rRNA_normalised/'

centroid_file = pd.read_csv('/Users/joshtitlow/Desktop/airyscan/images/images/_batch/_FISH-QUANT__all_spots_180801.csv', header=13)

# index rows in the FQ.csv file to get file names and pixel coordinates
for index, row in centroid_file.iterrows():

    # get file name from File column
    image  = row['File']

    # open the image using sci kit image
    im = io.imread(image_dir+image)

    # store pixel coordinates (3x3 matrix surrounding the centroid) as variables
    Y = row['Y_pix']
    X = row['X_pix']
    Z1 = row['Z_pixAb']
    Z2 = row['Z_pixBl']
    x0 = row['X_pix'] - 1
    x1 = row['X_pix']
    x2 = row['X_pix'] + 1
    y0 = row['Y_pix'] - 1
    y1 = row['Y_pix']
    y2 = row['Y_pix'] + 1

    # calculate the average intensity of pixels surrounding the centroid
    pixel = numpy.mean([im[Z1,x0,y0],im[Z1,x1,y0],im[Z1,x2,y0],im[Z1,x0,y1],im[Z1,x1,y1],im[Z1,x2,y1],im[Z1,x0,y2],im[Z1,x1,y2],im[Z1,x2,y2]])

    # return the intensity of a single pixel from the plane directly below (Z1) or below (Z2) the centroid
    #pixel=im[Z1,Y,X]
    print(pixel)
