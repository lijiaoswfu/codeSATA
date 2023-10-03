#######################
import arcpy
from arcpy import env
import os

import sys
###############
##################################

fc= arcpy.GetParameterAsText(0)
fieldname= arcpy.GetParameterAsText(1)
shapeName = arcpy.Describe(fc).shapeFieldName

rows = arcpy.UpdateCursor(fc) 

i=1;
#########################################
##
for row in rows:#记录循环
    feat = row.getValue(shapeName)
    row.setValue(fieldname,feat.area)
    arcpy.AddMessage("No:"+str(i)+":"+str(feat.area))
    rows.updateRow(row)

    i=i+1;