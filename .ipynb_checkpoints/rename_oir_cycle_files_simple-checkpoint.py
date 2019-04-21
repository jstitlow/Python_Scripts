# Rename Olympus matl experiment files with descriptions
# created: 8 September 2018
#
# Run from inside target directory
#
# May need to modify filename output

import os
import xml.etree.ElementTree as ET

tree = ET.parse('matl.omp2info')
root = tree.getroot()

#get cwd
cwd = os.getcwd()
#filenames = [file for file in os.listdir(cwd) if file.endswith('.oir')] # input file suffix
filenames = [file for file in os.listdir(cwd)]
print filenames
# map matl namespace
ns = {'matl':'http://www.olympus.co.jp/hpf/protocol/matl/model/matl'}

# create a dictionary for image name and description
file_dict = {}

# add image name and description to the dictionary
for group in root.findall('matl:group', ns):
    for description in group.findall('matl:description', ns):
        filename = description.text
    for area in group.findall('matl:area', ns):
        for image in area.findall('matl:image', ns):
            fileID = image.text
        file_dict[fileID]= filename

# replace image name with description name
for i in filenames:
    for fileID, filename in file_dict.items():
        #if i in fileID:
        if any(i in fileID for fileID in file_dict.items()):
            print "processing", i
            newfile = i.replace(i,i+fileID+'.oir') # output file suffix
            print (newfile)
            #os.rename(i, newfile)
