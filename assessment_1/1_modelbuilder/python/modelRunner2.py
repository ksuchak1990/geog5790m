# Imports
import arcpy

# Directories
h = "M:/geog5990m/src/practical1"
dataDir = h + "/arc/data/"

try:
	# Setting up workspace
	try:
		arcpy.env.workspace = h
		arcpy.ImportToolbox(h + "/arc/Models.tbx", "models")
	except arcpy.ExecuteError as e:
		print("Import toolbox error", e)
	
	# Running model
	try:
		arcpy.models.Explosion(dataDir + "original/input/buildings.shp",
						"100 Meters",
						dataDir + "original/input/explosion.shp",
						dataDir + "output/pyIntersect2.shp")
	except arcpy.ExecuteError as e:
		print("Model run error", e)
except Exception as e:
	print(e)


