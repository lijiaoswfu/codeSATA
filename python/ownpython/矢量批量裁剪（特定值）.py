# -*- coding: UTF-8 -*-
from imp import reload
import sys
import os
import string
import arcpy
reload(sys)
sys.setdefaultencoding('utf-8')

mxd = arcpy.mapping.MapDocument(r'E:\gis\python.mxd')
df = arcpy.mapping.ListDataFrames(mxd, "图层")[0]
arcpy.env.overwriteOutput = True


clipshp = r'E:\gis\shp\涪陵2000shp\乡镇界.shp'
fieldname = '乡镇名'
outworkspace = r'E:\gis\temp'
mdbbool = 'false'    # 是否mdb,ture是MDB，false为GDB

desc = arcpy.Describe(clipshp)
filepath = desc.CatalogPath
p = filepath.find(".mdb")
ftype = "String"
for field in desc.fields:
    if field.Name == fieldname:
        ftype = field.Type
        break
jfb_Select = outworkspace+"/tempshp.shp"  # 不能c:\要c:\\或者 c:/

# arcpy.AddMessage(u"7=执行到这里")
fieldvalue = "马武镇"  # 可以直接修改为特定值
# fieldvalue =""+ str(row.getValue(fieldname))
# arcpy.AddMessage(u"值fieldvalue="+fieldvalue)
if p > 0:  # mdb
    Expression = "["+fieldname + "]="
else:
    Expression = "\""+fieldname + "\"="
    # arcpy.AddMessage(u"表达式Expression1="+Expression)
if ftype == "String":
    Expression = Expression+"'"+fieldvalue+"'"
else:
    Expression = Expression+fieldvalue
    # arcpy.AddMessage(u"Expression2="+Expression)
arcpy.Select_analysis(clipshp, jfb_Select, Expression)
# arcpy.AddMessage(u"6=clipshp"+clipshp)
out_mdb = ""
# arcpy.AddMessage("======================================================out_mdb"+out_mdb)
if mdbbool == "true":
    out_mdb = outworkspace + "\\"+fieldvalue + \
        ".mdb"  # os.path.basename(dataset)
else:
    out_mdb = outworkspace + "\\"+fieldvalue+".gdb"
print(u"out_mdb"+out_mdb)
if not arcpy.Exists(out_mdb):
    if mdbbool == "true":
        arcpy.CreatePersonalGDB_management(
            os.path.dirname(out_mdb), os.path.basename(out_mdb))
    else:
        arcpy.CreateFileGDB_management(
            os.path.dirname(out_mdb), os.path.basename(out_mdb))


arcpy.env.workspace = r'E:\gis\shp.gdb\shp'
datasets = arcpy.ListDatasets(feature_type='feature')
datasets = [''] + datasets if datasets is not None else []
for ds in datasets:
    for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
        inworkspace = os.path.join(arcpy.env.workspace, ds, fc)
        print(inworkspace)
        mydatasets = string.split(inworkspace, ";")
        for dataset in mydatasets:
            mylayer = os.path.basename(dataset)
            print(u"clip:"+dataset+" to "+out_mdb+"\\" + mylayer)
            mylayer = mylayer.replace("(", "")
            mylayer = mylayer.replace(")", "")
            arcpy.Clip_analysis(dataset, jfb_Select,
                                out_mdb+"\\" + mylayer, "")

    if arcpy.Exists(jfb_Select):
        arcpy.Delete_management(jfb_Select)
