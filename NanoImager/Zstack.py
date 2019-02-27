# Zstack on a single XY position. Acquisition of multiple colors per Z position.
# The script assumes the instrument is already connected
# and the objective is focused on the coverslip surface 
# Import functions
import time

## INSTRUMENT PARAMETERS

nlasers = 3

## SET ACQUISITION PARAMETERS
n_frames = 1 # frames per plane
# Stage position parameters
z_increment = 0.1 # in microns
n_zsteps = 100 #goes down in z position, i.e., into the sample
#laser powers = [405, 532, 640] 
laser_powers = [0,11.83,0];
# Set exposure times in ms, one per wavelength
exposure_times = [100] # in order of acquisition
fv = 1
Folder = 'experiment'
File = 'Widefield' + str(fv)

# Initialize controls
# lasers = instrument.LightControl
# stage = instrument.StageControl
# af = instrument.AutoFocus

## STAGE PARAMETERS
# Check we have a reference point for autofocus, if not find one
#if not autofocus.HasReferencePoint:
#    autofocus.StartReferenceCalibration()
#    while autofocus.CurrentStatus == autofocus.Status.CALIBRATING:
#        time.sleep(0.1)
	# If we failed to calibrate for reference point raise an exception
#    if autofocus.LastCalibrationCode is not autofocus.CalibrationCompleteCode.SUCCESS:
#        raise Exception('Focus not calibrated')

## Get lasers ready, keeping them off
# Set powers
# light.GlobalOnState = False
for i in range(nlasers):
    light[i].PercentPower = 0
    light[i].Enabled = True

light[0].Enabled = False

# Parameters for frames
n_shots = len(exposure_times)
total_frames = n_frames*n_shots*n_zsteps
z_positions = []

## ACQUISITION
# Apply single shot autofocus
#autofocus.StartSingleShotAutoFocus(5000.0)
#while autofocus.CurrentStatus is autofocus.Status.FOCUSING_SINGLE_SHOT:
#    time.sleep(0.1)
	# Ensure we didn't fail
#if autofocus.LastStopCode is not autofocus.FocusStopCode.SUCCESS:
#    raise Exception('Could not activate single shot autofocus')
 
z0 = stage['z'].PositionInMicrons

for z in range(0, n_zsteps+1):
    z_positions.append([z0 - z*z_increment])

# Turn on lasers and set exposure times for camera
light[0].PercentPower = laser_powers[0]
light[1].PercentPower = laser_powers[1]
light[2].PercentPower = laser_powers[2]
time.sleep(0.2) 

# set exposure time
instrument.CameraControl.SetTargetExposureMilliseconds(exposure_times[0])

# Start a paused acquisition
acquisition.InitAcquisition(Folder, File, total_frames)

for zpos in z_positions:
    # Move to stage position
    stage["z"].RequestMoveAbsolute(zpos[0])
        # print(stage['z'].PositionInMicrons)

# Wait for all stages to stop
    while stage['x'].IsMoving or stage['y'].IsMoving or stage['z'].IsMoving:
        time.sleep(0.01)

    # Acquire colorset 1
    acquisition.ContinueFreeRunningFor(n_frames)

    # Wait until the acquisition has completed
    while acquisition.IsAcquiring:
        time.sleep(0.01)

# Wait for data_manager to finish processing
while data_manager.IsBusy:
    time.sleep(0.1)
