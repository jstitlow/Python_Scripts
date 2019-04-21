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
<<<<<<< HEAD
filenames = [file for file in os.listdir(cwd) if file.endswith('.tiff')] # input file suffix
#filenames = [file for file in os.listdir(cwd)]

=======
#filenames = [file for file in os.listdir(cwd) if file.endswith('.oir')] # input file suffix
filenames = [file for file in os.listdir(cwd)]
print filenames
>>>>>>> 62675e050218d15ed7a8d444d6571f7996f34f09
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
<<<<<<< HEAD
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
=======
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
>>>>>>> 62675e050218d15ed7a8d444d6571f7996f34f09
