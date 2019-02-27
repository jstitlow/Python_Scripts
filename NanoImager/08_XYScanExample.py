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
#instrument.Connect()

# Turn lasers off and then set them to the powers we want
lasers = instrument.LaserControl
lasers.GlobalOnState = False
lasers[1].PercentPower = 50
lasers[2].PercentPower = 50
lasers[1].Enabled = True
lasers[1].Enabled = True

# Get current position
stage = instrument.StageControl
x_start = stage.GetPositionInMicrons(stage.Axis.X)
y_start = stage.GetPositionInMicrons(stage.Axis.Y)

# define parameters for scan stage positions
x_inc_um = 50
y_inc_um = 50
n_x = 5
n_y = 5

stage_positions = []

for x in range(0, n_x):
	for y in range(0, n_y):
		stage_positions.append([x_start + x*x_inc_um, y_start + y*y_inc_um])

# define parameters for frames
frames_per_pos = 1
total_frames = frames_per_pos * n_x * n_y

# Autofocus
af = autofocus

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
for stage_pos in stage_positions:
	# Move to stage pos
	stage.RequestMoveAbsolute(stage.Axis.X, stage_pos[0])
	stage.RequestMoveAbsolute(stage.Axis.Y, stage_pos[1])
	while stage.IsMoving(stage.Axis.X) or stage.IsMoving(stage.Axis.Y):
		time.sleep(0.01)
	# Wait for 100ms
	time.sleep(0.1)
	# continue to acquire
	acquisition.ContinuePaused(frames_per_pos);
	# Wait until the acquisition has completed
	while acquisition.State == acquisition.AcquisitionState.ACQUISITION_ACTIVE or acquisition.State == acquisition.AcquisitionState.ACQUISITION_COMPLETING:
		time.sleep(0.1)
	# Ensure we still have auto focus
	if af.CurrentStatus is not af.Status.FOCUSING_CONTINUOUS:
		raise Exception('Continuous autofocus failed')