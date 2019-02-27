# This example assumes the following globals:
# data_manager (NimDotNet.DataManager)
# instrument (NimDotNet.NimControl)
# acquisition (NimDotNet.AcquisitionManager)
# profiles (NimDotNet.UserProfileManager)

global data_manager
global instrument
global acquisition
global profiles

# Connect to the microscope
# instrument.Connect()

# Get ref to lasers
lasers = instrument.LightControl

from NimDotNet import LightProgram

# Set up a laser program to alternate lasers 1 and 2
my_laser_program = LightProgram([[0.0,20.0,0.0],[0.0,0.0,20.0]])

# Switch lasers off but enable then
lasers.GlobalOnState = False
lasers[1].Enabled = True
lasers[2].Enabled = True

# Set the program and enable
lasers.Program = my_laser_program
lasers.ProgramActive = True
# Enable lasers
lasers.GlobalOnState = True

#...do acquisitions!...
