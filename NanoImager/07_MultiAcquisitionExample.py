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

# Turn lasers off and then set them to the powers we want
lasers = instrument.LaserControl
lasers.GlobalOnState = False
lasers.SetPercentPower(1, 50)
lasers.SetPercentPower(2, 50)
lasers.EnableLaser(1, True)
lasers.EnableLaser(2, True)

# lets do multiple acqusitions with different exposure times
exposure_times = [10,20,30,40,50]

for exposure in exposure_times:
	# set exposure time
	instrument.CameraControl.SetTargetExposureMilliseconds(exposure)
	# print actual exposure set
	print('Camera exposure: ')
	print(instrument.CameraControl.GetExposureTimeMilliseconds())
	# Lasers on
	lasers.GlobalOnState = True
	# Start acquisition
	acquisition.Start('NimPythonTraining','Example7_exposure' + str(exposure) + 'ms', 100);
	# Wait until the acquisition has completed
	while acquisition.State == acquisition.AcquisitionState.ACQUISITION_ACTIVE or acquisition.State == acquisition.AcquisitionState.ACQUISITION_COMPLETING:
		time.sleep(1)
	# Turn off the lasers
	lasers.GlobalOnState = False
	# Wait for 10 seconds before next
	time.sleep(10)