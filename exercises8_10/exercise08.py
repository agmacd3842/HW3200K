###Andrew MacDonald
### Exercise 8
### Challenge 1
import arcpy
import fileinput
import string
import os
from arcpy import env
env.workspace = "P:/gitprojects/HW3200K/"
env.overwriteOutput = True
outpath = "P:/gitprojects/HW3200K"
infile = "P:/gitprojects/3200k/points.txt/"
newfc = "HW3200K/newpolygon.shp"
arcpy.CreateFeatureClass_management(outpath, newfc, "Polygon")
cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
array = arcpy.Array()
point = arcpy.Point()
for line in fileinput.input(infile):
    point.ID, point.X, point.Y = line.split()

###Challenge 2
import arcpy
from arcpy import env
env.workspace = "P:/gitprojects/Python/Data/Exercise08/"
fc = "Hawaii.shp"
cursor = arcpy.SearchCursor(fc ["OID@", "SHAPE@"])
for row in cursor:
    print("Feature {0}: ".format(row[0]))
    partnum = 0
    for part in row[1]:
        print("Part {0}: ".format(partnum))
        for point in part:
            print("{0}, {1}".format(point.X, Point.Y))
        partnum += 1


        
