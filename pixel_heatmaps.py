# Script to extract pixel intensities relative to centroid coordinates
# Created: 9 August 2018
#
# Requires a directory of single channel .tiff images
# Requires the '_FISH-QUANT_all_spots_yymmdd.csv' file from a FQ bash run
#     > add the folowing columns to the FQ.CSV file: 'X_pix', 'Y_pix', and 'Z_pix'
#     > populate each column with the pixel coordinates that correspond to centroid position values
#         > i.e., X_pix = ROUND((Pos_X/n),0)    where n=pixel size
#
# TO DO:
#
# Write centroid coordinate to pixel coordinate calculation into Python script
# Write code to calculate pixel intensities directly from multichannel image
# Append pixel value output directly to the FQ_spots.csv file
# Install arg parse

import os
from skimage import io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

image_dir ='/Users/joshtitlow/Desktop/airyscan/images/smFISH/rRNA_normalised/'

centroid_file = pd.read_csv('/Users/joshtitlow/Desktop/airyscan/images/images/_batch/_FISH-QUANT__all_spots_180801.csv', header=13)

# create lists to store pixel values
mean_pixels = []
min_pixels = []
max_pixels = []

# setup a figure
fig = plt.figure(figsize = (10,10))

# start counting so the plt
n = 1

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

    # load pixel values into a numpy array and create a matrix
    matrix = numpy.array([im[Z1,x0,y0],im[Z1,x1,y0],im[Z1,x2,y0],im[Z1,x0,y1],im[Z1,x1,y1],im[Z1,x2,y1],im[Z1,x0,y2],im[Z1,x1,y2],im[Z1,x2,y2]])
    data = matrix.reshape((3, 3))

    # setup a figure (for single plots)
    #fig = plt.figure(figsize = (1,0.5)) # this line is outside the loop for this script

    # define subplot in that figure
    #ax = fig.add_subplot(121) # numbers equal position of plot within the figure
    ax = fig.add_subplot(50,50,n) # numbers equal position of plot within the figure

    # modify the plot
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # define heatmap settings
    heatmap = ax.pcolor(data, cmap=plt.cm.Greys, vmin=0, vmax=461)
    heatmap.set_label('pixel intensity')

    # plot heatmap
    #plt.colorbar(heatmap)

    # calculate some descriptive statistics on the intensity of pixels surrounding the centroid
    pixelmean = np.mean([im[Z1,x0,y0],im[Z1,x1,y0],im[Z1,x2,y0],im[Z1,x0,y1],im[Z1,x1,y1],im[Z1,x2,y1],im[Z1,x0,y2],im[Z1,x1,y2],im[Z1,x2,y2]])
    pixelmin = np.min([im[Z1,x0,y0],im[Z1,x1,y0],im[Z1,x2,y0],im[Z1,x0,y1],im[Z1,x1,y1],im[Z1,x2,y1],im[Z1,x0,y2],im[Z1,x1,y2],im[Z1,x2,y2]])
    pixelmax = np.max([im[Z1,x0,y0],im[Z1,x1,y0],im[Z1,x2,y0],im[Z1,x0,y1],im[Z1,x1,y1],im[Z1,x2,y1],im[Z1,x0,y2],im[Z1,x1,y2],im[Z1,x2,y2]])

    # add pixel statistics to a list
    mean_pixels.append(pixelmean)
    min_pixels.append(pixelmin)
    max_pixels.append(pixelmax)

    # iterate
    n+=1

# calculate some basic stastistics about pixel intensity from the whole dataset
meanpixel=np.mean(mean_pixels)
minpixel=np.min(min_pixels)
maxpixel=np.max(max_pixels)

# print basic statistics from the whole dataset
print "Mean pixel intensity =", meanpixel
print "Min pixel intensity =", minpixel
print "Max pixel intensity =", maxpixel

# write basic statistics to csv file
df = pd.DataFrame(mean_pixels, columns=["column"])
df.to_csv('test_list.csv', index=False)

# plot figure and save
plt.savefig('test_matrix.png')
plt.show(fig)
