# Imports
import arcpy

# File directories
sf = "M:/geog5990m/src/practical2/arc/data/input/explosion.shp"
lf = "M:/geog5990m/src/practical2/arc/data/input/explosion2.lyr"

# Convert format
arcpy.management.MakeFeatureLayer(sf, "lyr")
arcpy.management.SaveToLayerFile("lyr", lf, "ABSOLUTE")
