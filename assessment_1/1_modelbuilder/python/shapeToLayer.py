# Imports
import arcpy

# Directories
sf = "M:/geog5990m/src/practical1/arc/data/original/input/explosion.shp"
lf = "M:/geog5990m/src/practical1/arc/data/original/input/explosion.lyr"

# Convert
lyr = "explosion_lyr"
arcpy.management.MakeFeatureLayer(sf, lyr)
arcpy.management.SaveToLayerFile(lyr, lf, "ABSOLUTE")
