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

# Connect to simulated hardware
instrument.ConnectToSimulatedHardware()
# Start the camera view
instrument.CameraControl.BeginView()
# Print the current state (should be zero == not active)
print(acquisition.State)

# Start acquisition
acquisition.Start('NimPythonTraining','Example1', 100);
# Wait until the acquisition has completed
while acquisition.State == acquisition.AcquisitionState.ACQUISITION_ACTIVE or acquisition.State == acquisition.AcquisitionState.ACQUISITION_COMPLETING:
	time.sleep(1)

# Acqusition should have completed now
# Data manager contains the results
# Let's check what we can get from data_manager
print_methods(data_manager)

# Check the status
if data_manager.CurrentStatus == data_manager.Status.EMPTY:
	print('No data. Acquisition failed!')

# Print the filenames
files = data_manager.Files
print('Files:')
for f in files:
	print(f)

# Print the directory
print('Directory:')
print(data_manager.Directory)

# Disconnect
instrument.Disconnect()