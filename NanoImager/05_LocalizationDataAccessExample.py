# This example assumes the following globals:
# data_manager (NimDotNet.DataManager)
# instrument (NimDotNet.NimControl)
# acquisition (NimDotNet.AcquisitionManager)
# profiles (NimDotNet.UserProfileManager)

global data_manager
global instrument
global acquisition
global profiles

# Assuming we have loaded data at this point...

# Get access to the localizations
loc_access = data_manager.Localizations

# print some stuff
print(loc_access.FrameCount)
print(loc_access.ResultCount)

# get all of the results into a Python list
locs = loc_access.GetLocalizationResults()
# print the count again
print(len(locs))

# if we don't want to get all of the localization results
# we can access them directly
# to do this, we need to import some classes into the interpreter
# first, our LocalizationResult
from NimDotNet import LocalizationResult
# second, an "Action" class, which is basically a function
from System import Action

# define a count variable
count = 0
# define a function to increment each count
def do_count(lr):
	global count
	count += 1
# Create a NimDotNet compatible function
nim_count = Action[LocalizationResult](do_count)
# Call this function for each localization
loc_access.ForEachLocalization(nim_count)
# print the count again
print(count)

# let's do something slightly more interesting
# let's find the brightest unfiltered point
max_bright = 0.0
def update_max_bright(lr):
	global max_bright
	if lr.isUnfiltered and lr.intensity > max_bright:
		max_bright = lr.intensity
loc_access.ForEachLocalization(Action[LocalizationResult](update_max_bright))
print(max_bright)

# let's make a chart!

# create lists for values
intensities = []
backgrounds = []

# create a function to add intensity and background to x/y lists
def update_lists(lr):
	global intensities,backgrounds
	if lr.isUnfiltered:
		intensities.append(lr.intensity)
		backgrounds.append(lr.background)
# call for each localization result
loc_access.ForEachLocalization(Action[LocalizationResult](update_lists))
# get plotly involved...
import plotly
from plotly.graph_objs import Scatter, Layout
# plot the chart
plotly.offline.plot({
	"data": [Scatter(x=intensities, y=backgrounds)],
	"layout": Layout(title="Some great chart")
})