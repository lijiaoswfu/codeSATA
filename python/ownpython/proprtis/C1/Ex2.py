# 根据输入的线层，按照步长布设点图层
import arcpy
import os
home = "E:/gis/temp"
arcpy.env.workspace = home
# Script parameters
in_fc = "rout.shp"
out_fc = "points9.shp"
interval = 50
use_percent = False
end_points = True
# Create output feature class
desc = arcpy.Describe(in_fc)
sr = desc.spatialReference
arcpy.CreateFeatureclass_management(home, out_fc, "POINT",
                                    "", "", "", sr)
# Add a field to transfer FID from input
fid_name = "NEW_ID"
arcpy.AddField_management(out_fc, fid_name, "LONG")
# Create new points based on input lines
with arcpy.da.SearchCursor(in_fc, ["SHAPE@", "OID@"]) as search_cur:
    with arcpy.da.InsertCursor(out_fc, ["SHAPE@",
                                        fid_name]) as insert_cur:
        for row in search_cur:
            line = row[0]
            if line:
                if end_points:
                    insert_cur.insertRow([line.firstPoint, row[1]])
                cur_length = interval
                max_position = 1
                if not use_percent:
                    max_position = line.length
                while cur_length < max_position:
                    insert_cur.insertRow(
                        [line.positionAlongLine(cur_length,
                                                use_percent), row[1]])
                    cur_length += interval
                if end_points:
                    insert_cur.insertRow([line.lastPoint, row[1]])
