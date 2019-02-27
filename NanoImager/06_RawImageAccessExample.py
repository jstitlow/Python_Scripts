# This example assumes the following globals:
# data_manager (NimDotNet.DataManager)
# instrument (NimDotNet.NimControl)
# acquisition (NimDotNet.AcquisitionManager)
# profiles (NimDotNet.UserProfileManager)

global data_manager
global instrument
global acquisition
global profiles

# We're going to write images to a tiff
# so we need numpy for arrays and tifffile for writing
import numpy
import tifffile

# assuming we have loaded data at this point...

# get image access
image_access = data_manager.RawImages

# print some values
print(image_access.TotalFrames)
print(image_access.NChannels)
print(image_access.AcqData.JSON)

# Loop through images and channels
for i in range(image_access.TotalFrames):
	image = image_access.GetImage(i)
	for c in range(image_access.NChannels):
		croppedImage = image_access.GetChannelImage(i,c)
		mappedImage = image_access.GetMappedChannelImage(i,c)

# image is now the last image
# we can access pixels directly
pixel_sum = 0
for y in range(0,image.Dims.Height):
	for x in range(0,image.Dims.Width):
		pixel_sum += image.Pixels[y*image.Dims.Width + x]

print(pixel_sum)

# Convert the cropped image to a numpy array
output_data = numpy.zeros((croppedImage.Dims.Height, croppedImage.Dims.Width), numpy.uint16)
for y in range(0,croppedImage.Dims.Height):
	for x in range(0,croppedImage.Dims.Width):
		output_data[y][x] = croppedImage.Pixels[y*croppedImage.Dims.Width + x]

# create file name in current directory
file_name = data_manager.Directory + '/croptiff.tiff'
# open and write to tiff file
with tifffile.TiffWriter(file_name) as tiff:
	tiff.save(output_data, description=croppedImage.Metadata.JSON);
	print ('File ' + file_name + ' exported')