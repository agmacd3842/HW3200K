### Andrew MacDonald
### Exercise 10.
### Challenge 1

import arcpy
from arcpy import env
env.workspace = ("P:/gitprojects/Python/Data/Exercise10/")
mapdoc = arcpy.mapping.MapDocument("P:/gitprojects/Python/Data/Exercise10/Austin_TX.mxd")
listdf = arcpy.mapping.ListDataFrames(mapdoc)
newlayer = arcpy.mapping.Layer("P:/gitprojects/Python/Data/Exercise10/Austin/parks.shp")
for df in listdf:
    arcpy.mapping.AddLayer(listdf, newlayer)

