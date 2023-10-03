# 读取操作空间下的shp文件，然后新建一个GDB数据库，建一个面类，然后将面shp文件复制进数据库面类下
import arcpy
import os

ws = "E:/gis/shp/涪陵2000shp"
gdb = "Database.gdb"
prj = "乡镇界.prj"
arcpy.env.workspace = ws
arcpy.CreateFileGDB_management(ws, gdb)
sr = arcpy.SpatialReference(os.path.join(ws, prj))
arcpy.CreateFeatureDataset_management(gdb, "Polygons", sr)
fc_list = arcpy.ListFeatureClasses()
for fc in fc_list:
    fc_desc = arcpy.Describe(fc)
    if fc_desc.shapeType == "Polygon":
        newfc = os.path.join(gdb, "Polygons", fc_desc.basename)
        arcpy.CopyFeatures_management(fc, newfc)
