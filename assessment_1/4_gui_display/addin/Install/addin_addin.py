import arcpy
import pythonaddins

class RiskButton(object):
    """Implementation for addin_addin.RiskButton (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.MessageBox("How now brown sheep", "woof")