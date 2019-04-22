import arcpy
import pythonaddins

class ExplosionButtonClass(object):
    """Implementation for addin_addin.explosionbutton (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
		pythonaddins.MessageBox("What are *you* looking at?", "Hello")

		# Directories
		h = "M:/geog5990m/src/practical1"
		dataDir = h + "/arc/data/"
		object = pythonaddins.GPToolDialog(h + "/arc/Models.tbx", "Explosion")

		# Script args
		buildings = arcpy.GetParameterAsText(0)
		pythonaddins.MessageBox(buildings)
		radius = arcpy.GetParameterAsText(1)
		pythonaddins.MessageBox(radius)
		explosion = arcpy.GetParameterAsText(2)
		pythonaddins.MessageBox(explosion)
		intersect = arcpy.GetParameterAsText(3)
		pythonaddins.MessageBox(intersect)


		try:
			# Setting up workspace
			# try:
				# arcpy.env.workspace = h
				# arcpy.ImportToolbox(h + "/arc/Models.tbx", "models")
			# except arcpy.ExecuteError as e:
				# print("Import toolbox error", e)
			
			# Running model
			try:
				object(buildings,radius,explosion,intersect)
			except arcpy.ExecuteError as e:
				pythonaddins.MessageBox("Model run error: " + e)
		except Exception as e:
			pythonaddins.MessageBox(e)


