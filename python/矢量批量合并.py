import sys

#############

#################################

import arcpy

import string



try:

    workspace =arcpy.GetParameterAsText(0)  #'C:\Users\Administrator\Desktop\\cc'

 

    outdb =arcpy.GetParameterAsText(1)   #'C:\Users\Administrator\Desktop\\lutian.mdb'

    arcpy.env.workspace = workspace

    arcpy.AddMessage("outdb:"+outdb)

    files = arcpy.ListWorkspaces("","")

    for File in files:

        arcpy.AddMessage("File:"+File)

       

        arcpy.env.workspace = outdb

        fcs = arcpy.ListFeatureClasses()

        for fc in fcs:

            arcpy.AddMessage("fc:"+fc)

            if arcpy.Exists(File + "\\" + fc):

                arcpy.Append_management([ File + "\\" + fc], outdb + "\\" + fc,"NO_TEST","","")

            else:

                arcpy.AddMessage("not exists:"+File + "\\" + fc)

           

        fcs = arcpy.ListTables()

        for fc in fcs:

            arcpy.AddMessage("fc:"+fc)

            if arcpy.Exists(File + "\\" + fc):

                arcpy.Append_management([File + "\\" + fc], outdb + "\\" + fc,"NO_TEST","","")

            else:

                arcpy.AddMessage("not exists:"+File + "\\" + fc)

           

        dss = arcpy.ListDatasets()

        for ds in dss:

            arcpy.AddMessage("ds:"+ds)

            arcpy.env.workspace = outdb+"\\"+ds

            fcs1 = arcpy.ListFeatureClasses()

            for fc1 in fcs1:

                arcpy.AddMessage("fc1:"+fc1)

                if arcpy.Exists(File + "\\" + ds + "\\" + fc1):

                    arcpy.Append_management([File + "\\" + ds + "\\" + fc1], outdb + "\\" + ds + "\\" + fc1,"NO_TEST","","")

                else:

                    arcpy.AddMessage("not exists:"+File + "\\" + ds + "\\" + fc1)





except arcpy.ExecuteError:

    arcpy.AddWarning(arcpy.GetMessages())