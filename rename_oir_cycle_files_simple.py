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
filenames = [file for file in os.listdir(cwd) if file.endswith('.tiff')] # input file suffix
#filenames = [file for file in os.listdir(cwd)]

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
            fileId = image.text
        file_dict[fileId]= filename

# replace image name with description nameL
for i in filenames:
    print "oldfile =", i
    i = i.replace(i, (os.path.splitext(i)[0])+'.oir')
    for fileId, filename in file_dict.items():
        if i in fileId:
            newfile = i.replace(i, '20180810_smFISH_screen_'+filename+'.tiff') # input file suffix
            print "newfile =", newfile
            #os.rename(i, newfile)
#            os.rename(i, newfile)
