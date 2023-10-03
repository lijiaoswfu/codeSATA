import sys, os, string,types

import arcpy

from arcpy import env





arcpy.env.overwriteOutput = True



oldraster  = arcpy.GetParameterAsText(0)

arcpy.AddMessage("1oldraster="+oldraster)

clipshp  = arcpy.GetParameterAsText(1)

arcpy.AddMessage("2clipshp="+clipshp)

fieldname= arcpy.GetParameterAsText(2)

arcpy.AddMessage("3fieldname="+fieldname)

outworkspace= arcpy.GetParameterAsText(3)

arcpy.AddMessage("4="+outworkspace)



arcpy.CheckOutExtension("spatial")

rows = arcpy.SearchCursor(clipshp)



jfb_Select=outworkspace+"/temp.shp" #不能c:\要c:\\或者c:/





for row in rows:



    try:

        b=1

        value=row.getValue(fieldname)

        #gp.AddMessage("value="+value)

        if (type(value) is types.IntType):

            fieldvalue = str(value)

            b=2

        elif (type(value)  is types.StringType):   #是否string类型

            fieldvalue = value

        else:

            fieldvalue = str(value)

   

        arcpy.AddMessage("fieldvalue="+fieldvalue)

        if b==2:

            Expression="\""+fieldname +"\" ="+fieldvalue+""

        else:

            Expression="\""+fieldname +"\" ='"+fieldvalue+"'"

        arcpy.AddMessage("Expression="+Expression+",jfb_Select="+jfb_Select+",clipshp="+clipshp)

        arcpy.Select_analysis(clipshp, jfb_Select, Expression)

   

        out_raster =outworkspace+"/"+fieldvalue+".tif"

        arcpy.gp.ExtractByMask_sa(oldraster, jfb_Select, out_raster)

    except Exception, ErrorDesc:

        #If an error set output boolean parameter "Error" to True.

        arcpy.AddError(str(ErrorDesc))

if arcpy.Exists(jfb_Select):

arcpy.Delete_management(jfb_Select)