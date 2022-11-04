import arcpy, os
from collections import defaultdict
# Set work environemnt
arcpy.env.workspace = r'D:\GISDATA\IterateFeatureClasses1\IterateFeatureClasses\Data'
# Set output GDB, search keyword
output_gdb = r'D:\GISDATA\IterateFeatureClasses1\IterateFeatureClasses\Park_Merge.gdb'
search = 'Park'
fc = []
# use walk return data names in directory
walk = arcpy.da.Walk(datatype = 'FeatureClass', type = 'polygon')
# append selected feature into the fc list
for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        if search in filename:
            fc.append(os.path.join(dirpath, filename))
# merge them together as park_merge
if fc:
    output = os.path.join(output_gdb, os.path.basename(search) + '_merge')
    arcpy.Merge_management(fc, output)

