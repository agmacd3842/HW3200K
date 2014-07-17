### Andrew MacDonald
### Exercise 06
### Challenge 1

import arcpy
from arcpy import env
env.workspace = "P:/gitprojects/HW3200K/PythonEx06/Exercise06/"
fclist = arcpy.ListFeatureClasses()
for item in fclist:
    name = arcpy.Describe(item)
    shapefile = name.name
    data = name.dataType
    print"{} is a {} feature class.".format(shapefile, data)

### Challenge 2
import arcpy
from arcpy import env
env.workspace = "P:/gitprojects/HW3200K/PythonEx06/Exercise06/"
arcpy.CreateFileGDB_management("P:/gitprojects/HW3200K/PythonEx06/", "challenge2.gdb")
fclist = arcpy.ListFeatureClasses()
for item in fclist:
    shapefile = arcpy.Describe(item)
    desc = shapefile.shapeType
    if desc == "Polygon":  
        arcpy.CopyFeatures_management(item, "P:/gitprojects/HW3200K/PythonEx06/challenge2.gdb/" + shapefile.name.split('.')[0])
    
    
