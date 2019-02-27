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
instrument.Connect()

# Get ref to lasers
lasers = instrument.LaserControl

from NimDotNet import LaserProgram

# Set up a laser program to alternate lasers 1 and 2
my_laser_program = LaserProgram([[0.0,60.0,0.0],[0.0,0.0,60.0]])

# Switch lasers off but enable then
lasers.GlobalOnState = False
lasers[1].Enabled = True
lasers[2].Enabled = True

# Set the program and enable
lasers.Program = my_laser_program
lasers.EnableProgram = True
# Enable lasers
lasers.GlobalOnState = True

#...do acquisitions!...