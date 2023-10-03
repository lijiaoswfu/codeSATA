#######################
import arcpy
from arcpy import env
import os

import sys
###############
##################################

fc= arcpy.GetParameterAsText(0)
fieldname= arcpy.GetParameterAsText(1)
k= arcpy.GetParameter(2)  ##开始值

rows = arcpy.UpdateCursor(fc) 

i=k
#########################################
##
for row in rows:
    
    row.setValue(fieldname,i)
    arcpy.AddMessage("No:"+str(i))
    rows.updateRow(row)
    i=i+1;
如果需要进度条代码如下：

import arcpy
from arcpy import env
import os

import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

fc= arcpy.GetParameterAsText(0)
fieldname= arcpy.GetParameterAsText(1)
k= arcpy.GetParameter(2)
num=arcpy.GetCount_management(fc)
n=int(str(num))
arcpy.SetProgressor("step", "更新:"+fc+",Field="+fieldname,0,n,1)
rows = arcpy.UpdateCursor(fc) 

i=k

for row in rows:
    arcpy.SetProgressorLabel("正在等待....") 
    row.setValue(fieldname,i)
    arcpy.AddMessage("当前:"+str(i))
    rows.updateRow(row)
    arcpy.SetProgressorPosition()
    i=i+1
arcpy.ResetProgressor()
del row