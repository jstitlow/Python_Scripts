# This example assumes the following globals:
# data_manager (NimDotNet.DataManager)
# instrument (NimDotNet.NimControl)
# acquisition (NimDotNet.AcquisitionManager)
# profiles (NimDotNet.UserProfileManager)

global data_manager
global instrument
global acquisition
global profiles

import time

# Connect to emulated hardware and start camera
instrument.ConnectToSimulatedHardware()
camera = instrument.CameraControl
camera.BeginView()

# Create an image source from the camera
nFrames = 10
image_source = camera.CreateImageSource(10)

# Collect all into an image list
image_list = []
while True:
	image = image_source.GetNextImage()
	if image:
		image_list.append(image)
	else:
		break

# Below should be a list of size nFrames
print(len(image_list))