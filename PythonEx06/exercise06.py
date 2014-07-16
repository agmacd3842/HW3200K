### Andrew MacDonald
### Exercise 06
### Challenge 1

import arcpy
from arcpy import env
env.workspace = "P:/PythonEx06/Exercise06/"
outWorkspace = "P:/PythonExo6/Exercise06/Exercise06_2/"
fclist = arcpy.ListFeatureClasses()
for item in fclist:
    name = arcpy.Describe(item)
    shapefile = name.name
    data = name.dataType
    print"{} is a {} feature class.".format(shapefile, data)

### Challenge 2
import arcpy
from arcpy import env
env.workspace = "P:/PythonEx06/Exercise06/"
outWorkspace = "P:/PythonEx06/Exercise06/"
fclist = arcpy.ListFeatureClasses()
for item in fclist:
    shapefile = arcpy.Describe(item)
    desc = shapefile.shapeType
    if desc == "Polygon":  
        arcpy.CopyFeatures_management(shapefile, outWorkspace)
    
    
