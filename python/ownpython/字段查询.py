# -*- coding: UTF-8 -*-
from imp import reload
import sys
import arcpy
reload(sys)
sys.setdefaultencoding('utf-8')

mxd = arcpy.mapping.MapDocument(r'E:\gis\python.mxd')
df = arcpy.mapping.ListDataFrames(mxd, "图层")[0]

shp = r'E:\code\gis\flpoint.shp'
path = r'E:\code'
tempShp = path + '/temp.shp'
fildname = '可用性'
fildValue = '停用'
Expression = "\""+fildname + "\" ='"+fildValue+"'"

arcpy.Select_analysis(shp, tempShp, Expression)
