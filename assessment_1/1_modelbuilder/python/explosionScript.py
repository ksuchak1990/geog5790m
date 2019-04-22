# Imports
import arcpy

print("here")

# Script args
buildings = arcpy.GetParameterAsText(0)
print(buildings)
radius = arcpy.GetParameterAsText(1)
print(radius)
explosion = arcpy.GetParameterAsText(2)
print(explosion)
intersect = arcpy.GetParameterAsText(3)
print(intersect)

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
		arcpy.models.Explosion(buildings,radius,explosion,intersect)
	except arcpy.ExecuteError as e:
		print("Model run error", e)
except Exception as e:
	print(e)


