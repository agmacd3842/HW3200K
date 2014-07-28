### Andrew MacDonald
### Exercise 7
### Challenge 1

import arcpy
from arcpy import env
env.workspace = "P:/gitprojects/HW3200K/Exercise07/"
fc = "airports.shp"
cursor = arcpy.da.SearchCursor(fc, ["FEATURE"])
for row in cursor:
    if row is "airport":
        arcpy.Buffer_analysis( cursor , "P/gitprojects/3200K/Exercise07/airportbuffered/", "15000 METERS")
    elif row is "seaplane base":
        arcpy.Buffer_analysis(cursor , "P/gitprojects/3200K/Exercise07/seaplanesbuffered/" , "7500 METERS")

pass

### Challenge 2

import arcpy
from arcpy import env
env.workspace = "P:/gitprojects/HW3200K/Exercise07/"
fc = "P:/gitprojects/HW3200K/Exercise07/roads.shp/"
cursor = arcpy.da.InsertCursor(fc, ["FERRY"])
feature = arcpy.da.SearchCursor(fc, ["FEATURE"])
for row in cursor:
    if row in "FEATURE" is "airport":
        cursor.UpdateRow("YES")
    else:
        cursors.UpdateRow("NO")



