# Assumes an appropriate dataset for FRET analysis has been loaded and localized

# import the required modules/objects
import time
from NimDotNet import TraceAnalysis, TraceAnalysisSettings

# Create trace analysis object
ta = TraceAnalysis(data_manager)
# Create default settings
tas = TraceAnalysisSettings()

# Start trace analysis
ta.Start(tas)
# Wait for it to complete
while ta.IsRunning:
	time.sleep(0.5)

# Get some data
from NimDotNet import TracePointVarType as VT
framesAndDDPhotons = ta.GetData([VT.FRAME, VT.PHOTON_DD])

# Apply filters and get data again
ta.MinSteps = 100
ta.MinAverageSumPhotons = 200
filteredFramesAndDDPhotons = ta.GetData([VT.FRAME, VT.PHOTON_DD])

# Assign a trace to a group and filter
ta.SetGroupsForId(100,[1])
ta.UnfilteredGroups = [1]
group1Data = ta.GetData([VT.FRAME, VT.PHOTON_DD])

# Print all photon count for group 1 (e.g. ID 100)
for d in group1Data:
	print(f[1])