global data_manager
global instrument
global acquisition
global profiles

import time

from System import Func

from NimDotNet import LocalizationResult
from NimDotNet import Vector3f

# We need to connect to a simulated instrument and create some simulated localisations which we will then modify
instrument.ConnectToSimulatedHardware()
instrument.CameraControl.BeginView()

acquisition.Start('NimPythonTraining', 'Example1', 5)

# Wait until the acquisition has completed
while acquisition.IsActiveOrCompleting:
    time.sleep(0.1)

# Wait for data_manager to reload analysed data
while data_manager.IsBusy:
    time.sleep(0.1)

# Now we should have data
loc_access = data_manager.Localizations
locs = loc_access.GetLocalizationResults()

# Define a function to modify localisations


def modify_locs(lr):
    ar = LocalizationResult(lr)

    ar.rawPos = Vector3f(random.uniform(0.0, 100.0), random.uniform(0.0, 100.0), random.uniform(0.0, 100.0))
    ar.mappedPos = Vector3f(random.uniform(0.0, 100.0), random.uniform(0.0, 100.0), random.uniform(0.0, 100.0))

    return ar

loc_access.ModifyEachLocalization(Func[LocalizationResult, LocalizationResult](modify_locs))

print("Modification Success")

nim_cleanup()
