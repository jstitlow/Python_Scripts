
global data_manager
global instrument
global acquisition
global profiles

import time
import numpy as np
from PIL import Image

lasers = instrument.LightControl
lasers.GlobalOnState = False
lasers[1].PercentPower = 0
lasers[2].PercentPower = 50
lasers[1].Enabled = False
lasers[2].Enabled = True

exposure = 33
instrument.CameraControl.SetTargetExposureMilliseconds(exposure)
print('Camera exposure: ')
print(instrument.CameraControl.GetExposureTimeMilliseconds())

number_of_frames = 10

stageX = stage["x"]
stageY = stage["y"]
stageZ = stage["z"]

stageX.RequestMoveAbsolute(3.500)
stageY.RequestMoveAbsolute(4.500)
stageZ.RequestMoveAbsolute(63.606)
while stageX.IsMoving or stageY.IsMoving or stageZ.IsMoving:
    time.sleep(0.01)
time.sleep(0.1)

x_pos = stage.GetPositionInMicrons(stage.Axis.X)
y_pos = stage.GetPositionInMicrons(stage.Axis.Y)
z_pos = stage.GetPositionInMicrons(stage.Axis.Z)
print("Stage positions: ", x_pos, y_pos, z_pos)

lasers.GlobalOnState = True
acquisition.Start('Data', 'X%s_Y%s_Z%s' % (x_pos, y_pos, z_pos), number_of_frames)
while acquisition.IsActiveOrCompleting:
    time.sleep(0.1)
lasers.GlobalOnState = False
while data_manager.IsBusy:
    time.sleep(0.1)

print("Acquisition complete")

# Access the first file
files = data_manager.Files
print('Files:', files[0])
Im = Image.open(files[0])
Im_Arr = np.array(Im)
print("Loaded %s" % (files[0]))
