# Imports
import arcpy

# Set workspace
w = "M:/geog5990m/src/practical"
arcpy.env.workspace = w

# Import toolbox
arcpy.ImportToolbox(w + "1/arc/Models.tbx", "models")


#Executing: Explosion 
# M:\geog5990m\src\practical2\arc\data\input\explosion.shp 
#"100 Meters"
# M:\geog5990m\src\practical2\arc\data\input\buildings.shp
# M:\geog5990m\src\practical1\arc\data\output\test.shp

es = w + "2/arc/data/input/explosion.shp"
print("es", es)

arcpy.models.Explosion(w + "2/arc/data/output/pyintersect.shp",w + "2/arc/data/input/buildings.shp","100 Meters",es)


