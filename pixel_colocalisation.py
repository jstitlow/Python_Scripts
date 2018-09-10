### Copyright (C) 2018 Clara Eleonore Pavillet

# Name: Nuclei_Reconstruction
# Date of Creation: 03/03/18
# Last Update: 05/03/18

# Python Version: 3.6

# Description: 	Virtually reconstruct nuclei voxel coordinates (xyz) from the binary segmentation done with the 3D Object tool in Fiji.
# 				It takes in each individual xy containing file per z sclice and creates a matrix and csv file of xyz nuclei coordinates.
# 				Since FISH_Quant reads in nanometers (nm), all pixel values will be multiplied by 139.15.

# Additional Note:	Focus on an individual msp300 for now
# 					Important notes are commented out in this version!!!

##############################################################################

import os
import re
import pandas as pd
from natsort import natsorted, ns
import numpy as np
from tifffile import tifffile
# import bhtsne
import matplotlib as mpl
mpl.use('Agg') #this line is for servers that don't have a display/monitor
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import csv

# _____________________________________________________________________________

# Turn txt to Numpy Array XY binary coordinates per Z slice

# Create a list of paths to iterate over (for bash mode)

dir_path = '/Users/cebook/Documents/DPhil_Projects/Ilan_Davis/smFISH_Analysis/Data/msp300/msp300_BinaryNucleiSegmentation/'
Folders = [x for x in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path,x))]
print(Folders)

# Create Dictionary for slices

SlicesDictionary = {}
numfiles = sum(1 for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)) and f[0] != '.')
print(numfiles)
# Will need to restrict count to .txt
# nuclei_array = np.empty((512,512,numfiles))

# 512x512xnumber of files in directory
# Either create empty matrix and add in the arrays as they come (overwritting the empty matrix in z) OR create dictionary to store 2D and dstack them


# for folder in Folders:
# 	for i in range(len(Folders)):
# 		if subpath == dir_path + Folder[i]

# _____________________________________________________________________________

# Create a binary matrix of 2D per slice nuclei coordinates for one image
subdir_path = '/Users/cebook/Documents/DPhil_Projects/Ilan_Davis/smFISH_Analysis/Data/msp300/msp300_BinaryNucleiSegmentation/msp300_p1s3r/'

for root, dirs, files in os.walk(subdir_path):
    for file in natsorted(files):
        if file.endswith('.txt'):
            print(file)

            xy_slice = np.loadtxt(subdir_path + file)

            print('Here is the slice Shape: ', xy_slice.shape)
            print('Here is the slice Type: ', xy_slice.dtype)
            print('Here is the slice Preview: ', xy_slice)

            Slice_Name = os.path.basename(subdir_path + file)

            SlicesDictionary.update({Slice_Name : xy_slice})

print(SlicesDictionary.keys())

# nuclei_array = np.append(nuclei_array, [xy_slice], axis=0)
msp300_p1s3r_BinaryStack = np.dstack(SlicesDictionary.values())
print(msp300_p1s3r_BinaryStack.shape)
print(msp300_p1s3r_BinaryStack)


print(msp300_p1s3r_BinaryStack[:,:,0].shape)
print(msp300_p1s3r_BinaryStack[:,:,36].shape) #So max is reached at 36 since 0 is 1

# But dont forget it does 0 to 511, and gives rows (Y), columns (X)... could transpose to get xy instead
# for index, x in np.ndenumerate(msp300_p1s3r_BinaryStack[:,:,10]):
# 	if x == 1:
# 		print(index, x)
# 	else:
# 		pass

# Clean up! To then write to CSV below :-) This one is a test on one z slice
for index, x in np.ndenumerate(msp300_p1s3r_BinaryStack[:,:,10]):
	if x == 1:
		print(str(index).lstrip('(').rstrip(')').replace(',', ''),x)
	else:
		pass

print(np.size(msp300_p1s3r_BinaryStack, 0))

print(np.size(msp300_p1s3r_BinaryStack, 1))

print(np.size(msp300_p1s3r_BinaryStack, 2))



# Restrict to last one which is the 37th slice (will therefore not run index 37, last one is 36 as seen above)
# for zslice in range(msp300_p1s3r_BinaryStack.shape[-1]):
# 	for index, x in np.ndenumerate(msp300_p1s3r_BinaryStack[:,:,zslice]):
# 		while zslice != np.size(msp300_p1s3r_BinaryStack, 2):
# 			if x == 1:
# 				print(index, x)
# 			else:
# 				pass

# This works:
# for z in range(msp300_p1s3r_BinaryStack.shape[2]):
#     print('This is slice number: ', z)
#     print(msp300_p1s3r_BinaryStack[...,z])
#     for index, x in np.ndenumerate(msp300_p1s3r_BinaryStack[:,:,z]):
#     	if x == 1:
#     		print(index, x)
#     	else:
#     		pass

# for z in range(msp300_p1s3r_BinaryStack.shape[2]):
#     print('This is slice number: ', z)
#     print(msp300_p1s3r_BinaryStack[...,z])
#     for index, x in np.ndenumerate(msp300_p1s3r_BinaryStack[:,:,z]):
#     	if x == 1:
#     		print(str(index).lstrip('(').rstrip(')').replace(',', ''),x)
#     	else:
#     		pass


# Write to CSV file all nuclei points as YXZ (add 1 to all values as they are recorded since python as seen above starts count at 0)
# Get folder name for csv name
FolderPath = os.path.dirname(subdir_path)
csv_name_pix = os.path.basename(FolderPath) + '_pixel_values' + '.csv'
csv_name_nano = os.path.basename(FolderPath) + '_nano_values' + '.csv'
print(csv_name_pix)
print(csv_name_nano)

# Work for header:
# with open(csv_name, 'w') as csvfile:
#         columns = ['Y_POS', 'X_POS', 'Z_POS']
#         writer = csv.DictWriter(csvfile, fieldnames=columns)
#         csvwriter = csv.writer(csvfile, delimiter=',')
#         writer.writeheader()

#     csvfile.close()


# with open(csv_name, 'w') as csvfile:
#         columns = ['Y_POS', 'X_POS', 'Z_POS']
#         writer = csv.DictWriter(csvfile, fieldnames=columns)
#         csvwriter = csv.writer(csvfile, delimiter=',')
#         writer.writeheader()

#         for z in range(msp300_p1s3r_BinaryStack.shape[2]):
#         	for index, x in np.ndenumerate(msp300_p1s3r_BinaryStack[:,:,z]):
#         		if x == 1:
#         			a = z + 1 #Need to add 1 to each element
#         			terminal_row = str(index).lstrip('(').rstrip(')').replace(',', '') + ' ' + str(a)
#         			csv_row = re.sub("r[\d+\.\d*]", " ", terminal_row).split()
#         			csvwriter.writerow(csv_row)
#         		else:
#         			pass
# csvfile.close()

# Create file based on pixel values
with open(csv_name_pix, 'w') as csvfile:
        columns = ['Y_POS', 'X_POS', 'Z_POS']
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        csvwriter = csv.writer(csvfile, delimiter=',')
        writer.writeheader()

        for z in range(msp300_p1s3r_BinaryStack.shape[2]):
        	for index, x in np.ndenumerate(msp300_p1s3r_BinaryStack[:,:,z]):
        		if x == 1:
        			a = z + 1 #Need to add 1 to each element
        			l, d = str(index).lstrip('(').rstrip(')').replace(',', '').split(' ')
        			r, c = int(l) + 1, int(d) + 1 #Change to int so I can add 1
        			terminal_row =  str(r) + ' ' + str(c) + ' ' + str(a)
        			csv_row = re.sub("r[\d+\.\d*]", " ", terminal_row).split()
        			csvwriter.writerow(csv_row)
        		else:
        			pass
csvfile.close()

# Create file based on nano values (*139.125)
with open(csv_name_nano, 'w') as csvfile:
        columns = ['Y_POS', 'X_POS', 'Z_POS']
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        csvwriter = csv.writer(csvfile, delimiter=',')
        writer.writeheader()

        for z in range(msp300_p1s3r_BinaryStack.shape[2]):
        	for index, x in np.ndenumerate(msp300_p1s3r_BinaryStack[:,:,z]):
        		if x == 1:
        			a = (z + 1) * 139.125 #Need to add 1 to each element
        			l, d = str(index).lstrip('(').rstrip(')').replace(',', '').split(' ')
        			r, c = (int(l) + 1)*139.125, (int(d) + 1)*139.125 #Change to int so I can add 1
        			terminal_row =  str(r) + ' ' + str(c) + ' ' + str(a)
        			csv_row = re.sub("r[\d+\.\d*]", " ", terminal_row).split()
        			csvwriter.writerow(csv_row)
        		else:
        			pass
csvfile.close()
