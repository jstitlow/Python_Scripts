# Rename Olympus matl experiment files with descriptions
# created: 8 September 2018
#
# Run from inside target directory
#
# Assumes .oir files have been converted to .tiff
#     > if not, then modify input file suffix below
#
# May need to modify filename output

import os
import xml.etree.ElementTree as ET

tree = ET.parse('matl.omp2info')
root = tree.getroot()

#get cwd
cwd = os.getcwd()
filenames = [file for file in os.listdir(cwd) if file.endswith('.tiff')] # input file suffix

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

#files = ('20180824_60x_cycle_A01_G001_0001.oir', '20180824_60x_cycle_A01_G010_0001.oir')
#print 'old filename =', files

# replace image name with description nameL
for i in filenames:
    for fileId, filename in file_dict.items():
        if i in fileId+'.tiff' and 'OrR' not in fileId: # if input files are .oir.tiff
            newfile = i.replace(i, '20180824_CPTI00'+filename+'.tiff') # output file suffix
            print newfile
            os.rename(i, newfile)
        if i in fileId+'.tiff' and 'OrR' in fileId:
            newfile = i.replace(i, '20180824_'+filename+'.tiff') # filename output
            os.rename(i, newfile)
    print processing i
