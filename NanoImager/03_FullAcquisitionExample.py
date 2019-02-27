# This example assumes the following globals:
# data_manager (NimDotNet.DataManager)
# instrument (NimDotNet.NimControl)
# acquisition (NimDotNet.AcquisitionManager)
# profiles (NimDotNet.UserProfileManager)

global data_manager
global instrument
global acquisition
global profiles

# We'll need the 'time' import to sleep
import time

# Connect to the microscope
instrument.Connect()

# Set camera parameters
camera = instrument.CameraControl
# FPS
camera.SetTargetFramesPerSecond(50)
# Or we could do exposure
# camera.SetTargetExposureMilliseconds(25)

# Set acquisition parameters
acquisition.SaveTiffFiles = True
acquisition.RealTimeLocalization = True

# Set laser powers
lasers = instrument.LaserControl
# Set laser index 1 and 2 to 50% power
lasers.SetPercentPower(1, 50)
lasers.SetPercentPower(2, 50)
# Switch on lasers
lasers.EnableLaser(1, True)
lasers.EnableLaser(2, True)

# Start acquisition
acquisition.Start("NimPythonTraining","Example3", 100);
# Wait until the acquisition has completed
while acquisition.State == acquisition.AcquisitionState.ACQUISITION_ACTIVE or acquisition.State == acquisition.AcquisitionState.ACQUISITION_COMPLETING:
	time.sleep(1)

# Turn off the lasers
lasers.GlobalOnState = False

# Check the status
if data_manager.CurrentStatus == data_manager.Status.EMPTY:
	print("No data. Acquisition failed!")

# Print the filenames
files = data_manager.Files
print('Files:')
for f in files:
	print(f)

# Disconnect
instrument.Disconnect()