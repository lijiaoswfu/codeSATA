#######################

import arcpy

import os

import sys

#############

###############################

indata = arcpy.GetParameterAsText(0)

outdata = arcpy.GetParameterAsText(1)

EXT = arcpy.GetParameterAsText(2)

dpi = arcpy.GetParameter(3)

EXT=EXT.upper()

for root, dirs, files in os.walk(indata): #会遍历所有文件包括子文件里的数据

   arcpy.AddMessage(u"目录:" + root)

   rootList=root.split('.')

   n=len(rootList)

   if (n<2): #不考虑进入 gdb 目录下循环

       for name in files:

           #arcpy.AddMessage(u"name:" + name)

           mystr=name.upper()

           if (mystr.endswith('.MXD')): #找到扩展名.mxd 的数据

               try:

                   fs = os.path.join(root,name)

                   mxd = arcpy.mapping.MapDocument(fs)

                   arcpy.AddMessage(u" 保 存 了 :" + outdata+"/" +

                   name.split('.')[0]+"."+EXT)

                  

                   if EXT=="JPG":

                       arcpy.mapping.ExportToJPEG(mxd,outdata +"/"+name.split('.')[0],resolution=dpi)

                   elif EXT=="TIF":

                       arcpy.mapping.ExportToTIFF(mxd,outdata +"/"+name.split('.')[0],resolution=dpi)

                   elif EXT=="PDF":

                       arcpy.mapping.ExportToPDF(mxd,outdata +"/"+name.split('.')[0],resolution=dpi)

                   elif EXT=="PNG":

                       arcpy.mapping.ExportToPNG(mxd,outdata +"/"+name.split('.')[0],resolution=dpi)

                   elif EXT=="EPS":

                       arcpy.mapping.ExportToEPS(mxd,outdata +"/"+name.split('.')[0],resolution=dpi)

                   elif EXT=="EMF":

                       arcpy.mapping.ExportToEMF(mxd,outdata +"/"+name.split('.')[0],resolution=dpi)

                   del mxd

               except Exception, ErrorDesc:

                   arcpy.AddError(str(ErrorDesc))