import arcpy

import sys

import os

from os.path import join, getsize 

reload(sys) 

sys.setdefaultencoding('utf8') 

inpath = arcpy.GetParameterAsText(0)

for root, dirs, files in os.walk(inpath):

    arcpy.env.workspace = root

    workspaces = arcpy.ListWorkspaces("*", "Access")

    for workspace in workspaces:

        try:

            arcpy.AddMessage("正在压缩mdb: " + str(workspace))

            arcpy.Compact_management(workspace)

        except Exception, ErrorDesc:

            arcpy.AddError(str(ErrorDesc))

    workspaces = arcpy.ListWorkspaces("*", "FileGDB")

    for workspace in workspaces:

        try:

            arcpy.AddMessage("正在压缩gdb: " + str(workspace))

            arcpy.Compact_management(workspace)

        except Exception, ErrorDesc:

            arcpy.AddError(str(ErrorDesc))