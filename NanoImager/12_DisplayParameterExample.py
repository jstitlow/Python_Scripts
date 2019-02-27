# Get display parameters
dp = data_manager.DisplayParameters
# For channel 1
dp1 = dp.ForChannel(1)

# Load Color class for easy definitions
from System.Drawing import Color
# Change the rendered points
dp1.RenderedPointsColor = Color.FromName("blue")
# From ARGB (ignores A)
dp1.RenderedPointsColor = Color.FromArgb(255,0,255,255)
# Point range (e.g. for Z positions)
dp1.RenderedPointsRangeMin = Color.FromName("orange")
dp1.RenderedPointsRangeMax = Color.FromName("green")
# Tracks...
dp1.TrackColor = Color.FromName("orange")
# Track range
dp1.TrackColorRangeMin = Color.FromName("red")
dp1.TrackColorRangeMax = Color.FromName("yellow")
# Point size
dp1.PointRenderingSigmaInNm = 10.0
# Raw images
dp1.RawImageColor = Color.FromName("magenta")
# Percentiles
dp1.RawImageLowerPercentile = 10.0
dp1.RawImageUpperPercentile = 90.0
# Charts
dp1.ChartColor = Color.FromName("blue")

# Reset to default
dp1.reset();