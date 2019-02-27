global data_manager
global instrument
global acquisition
global profiles

import time

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

stageX = stage["x"]
stageY = stage["y"]
stageZ = stage["z"]

x_start_pos = stage.GetPositionInMicrons(stage.Axis.X)
y_start_pos = stage.GetPositionInMicrons(stage.Axis.Y)
z_start_pos = stage.GetPositionInMicrons(stage.Axis.Z)

# Define parameters for scan stage positions
num_of_x_positions = 3
num_of_y_positions = 3
x_increment_um = 5
y_increment_um = 5
frames_per_pos = 5
total_frames = frames_per_pos * num_of_x_positions * num_of_y_positions

# Create list of stage positions to visit
x_half_scan_range = ((num_of_x_positions - 1) * x_increment_um) / 2
y_half_scan_range = ((num_of_y_positions - 1) * y_increment_um) / 2
x0 = x_start_pos - x_half_scan_range
y0 = y_start_pos - y_half_scan_range

stage_positions = []
for x in range(num_of_x_positions):
    for y in range(num_of_y_positions):
        stage_positions.append([x0 + x * x_increment_um, y0 + y * y_increment_um])

acquisition.InitAcquisition('XYData', 'Example1', total_frames)

print("Acquiring data. Looping through stage positions...")
for stage_pos in stage_positions:
    stageX.RequestMoveAbsolute(stage_pos[0])
    stageY.RequestMoveAbsolute(stage_pos[1])
    while stageX.IsMoving or stageY.IsMoving:
        time.sleep(0.01)
    lasers.GlobalOnState = True
    acquisition.ContinueFor(frames_per_pos)
    while acquisition.IsActiveOrCompleting:
        time.sleep(0.1)
    lasers.GlobalOnState = False
    time.sleep(0.1)

while data_manager.IsBusy:
    time.sleep(0.1)

print("Acquisition complete")
