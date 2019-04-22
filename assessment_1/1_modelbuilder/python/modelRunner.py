# Imports
import arcpy

# Setting up workspace
h = "M:/geog5990m/src/practical1"
arcpy.env.workspace = h
arcpy.ImportToolbox(h + "/arc/Models.tbx", "models")

dataDir = h + "/arc/data/"

# Run model
arcpy.models.Explosion(dataDir + "original/input/buildings.shp",
						"100 Meters",
						dataDir + "original/input/explosion.shp",
						dataDir + "output/pyIntersect.shp")
