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

# Get current position
stage = instrument.StageControl
x_start = stage.GetPositionInMicrons(stage.Axis.X)
y_start = stage.GetPositionInMicrons(stage.Axis.Y)
z_start = stage.GetPositionInMicrons(stage.Axis.Z)

# define parameters for scan stage positions
x_inc_um = 50
y_inc_um = 50
z_inc_um = 0.2
n_x = 5
n_y = 5
n_z = 3

stage_XY = []
stage_Z = []


for x in range(0, n_x):
	for y in range(0, n_y):
		stage_XY.append([x_start + x*x_inc_um, y_start + y*y_inc_um])

for z in range(0, n_z)
        stage_Z.append([z_start - n_z*z_inc_um + z*z_inc_um])

# define parameters for frames
frames_per_pos = 1
total_frames = frames_per_pos * n_x * n_y*n_z

# Autofocus
af = instrument.AutoFocusController

# Check we have a reference point, if not find one
if not af.HasReferencePoint:
	af.StartReferenceCalibration()
	while af.CurrentStatus == af.Status.CALIBRATING:
		time.sleep(1)
	# If we failed to calibrate for reference point raise and exception
	if af.LastCalibrationCode is not af.CalibrationCode.SUCCESS:
		raise Exception('Focus not calibrated')

# If we're not already z-locked, to z-lock
if af.CurrentStatus is not af.Status.FOCUSING_CONTINUOUS:
	af.StartContinuousAutoFocus()
	time.sleep(5)
	# Ensure we didn't fail
	if af.CurrentStatus is not af.Status.FOCUSING_CONTINUOUS:
		raise Exception('Could not activate continuous autofocus')

# Start a paused acquisition
acquisition.StartPaused('NimPythonTraining','Example8', total_frames)

# Lasers on
lasers.GlobalOnState = True

# Loop through stage positions
for stage_posXY in stage_XY:
	# Move to stage pos
	stage.SetPositionInMicrons(stage_posXY[0])
	stage.SetPositionInMicrons(stage_posXY[1])
	# Wait for 100ms
	time.sleep(0.1)

	for stage_posZ in stage_Z
                stage.SetPositionInMicrons(stage_posZ[0])
                time.sleep(0.1)
	# continue to acquire
	acquisition.ContinuePaused(frames_per_pos);
	# Wait until the acquisition has completed
	while acquisition.State == acquisition.AcquisitionState.ACQUISITION_ACTIVE or acquisition.State == acquisition.AcquisitionState.ACQUISITION_COMPLETING:
		pass
	# Ensure we still have auto focus
	if af.CurrentStatus is not af.Status.FOCUSING_CONTINUOUS:
		raise Exception('Continuous autofocus failed')