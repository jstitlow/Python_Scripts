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

# Get a list of avaiable instruments
instruments = instrument.GetAvailableInstruments()
# Print them
for instr in instruments:
	print(instr)
# Select an instrument
instrument.SelectInstrument('Emulated Hardware')
# Connect
instrument.Connect()

# Start acquisition
acquisition.Start('NimPythonTraining','Example2', 100);
# Wait until the acquisition has completed
while acquisition.State == acquisition.AcquisitionState.ACQUISITION_ACTIVE or acquisition.State == acquisition.AcquisitionState.ACQUISITION_COMPLETING:
	time.sleep(1)

# Check the status
if data_manager.CurrentStatus == data_manager.Status.EMPTY:
	print('No data. Acquisition failed!')

# Print the filenames
files = data_manager.Files
print('Files:')
for f in files:
	print(f)

# Disconnect
instrument.Disconnect()