# 1 ArcGIS ModelBuilder

This is a practical for advanced programming in which we use the ModelBuilder in
ArcGIS to build a model.
We subsequently extract the model as a Python script, apply some modifications
and then feed the modified version back into ArcGIS.

The model aims to simulate an explosion taking place in an urban space, taking
as arguments the buildings, the point of the explosion and the radius of the
explosion.
The model then goes on to create a buffer about the centre of the explosion and
calculate the intersection of the buffer and the buildings.
