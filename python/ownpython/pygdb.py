# -*- coding: UTF-8 -*-
from imp import reload
import sys
import os
import arcpy
import importlib
importlib.reload(sys)
sys.setdefaultencoding('utf-8')

arcpy.env.workspace = r'E:\gis\shp.gdb'
datasets = arcpy.ListDatasets(feature_type='feature')
datasets = [''] + datasets if datasets is not None else []
for ds in datasets:
    for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
        path = os.path.join(arcpy.env.workspace, ds, fc)     # 获取要素图层名
        fields = arcpy.ListFields(path)
        for field in fields:
            print(("{0} is a type of {1} with a length of {2}".format(
                field.name, field.type, field.length)))    # 获取字段名、字段类型、字段长度
