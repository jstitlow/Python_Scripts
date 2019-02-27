# This example assumes the following globals:
# data_manager (NimDotNet.DataManager)
# instrument (NimDotNet.NimControl)
# acquisition (NimDotNet.AcquisitionManager)
# profiles (NimDotNet.UserProfileManager)

global data_manager
global instrument
global acquisition
global profiles

# load all associated data from the specified file
file_to_load = 'C:/Data/DEFAULT_USER/NimPythonTraining/Example2/Example2_2017-04-25_19h33m36s614ms.tif'
data_manager.LoadData(file_to_load)

# lets see what we loaded
for f in data_manager.Files:
	print(f)