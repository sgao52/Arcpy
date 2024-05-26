# This code use 2023 LULC data minus 2013 LULC data to get the forest gain and loss info in the whole country, and use zonal statistics function to get the province level of forest gain&loss data.
# created by copilot, edited by shan.
import arcpy
from arcpy import env
from arcpy.sa import *

# Set Env
env.workspace = r''

#Set local variables
inRaster2013 = r'' # 2013 lulc
inRaster2023 = r'' # 2023 lulc
outRec_2013 = 'reclassified_2013' # 2013 reclassification output
outRec_2023 = 'reclassified_2023' # 2023 reclassification output
zonalFeature = r'' # City administrative shp path
outTable = 'ForestChangeTable'
excelFile = 'forestChange.xlsx'
# Define reclassification value 
remap = RemapValue([[1,0], [2,1], [3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]]) # Assign value 2 to 1 and other to 0

# Reclassify rasters
reclassified2013 = Reclassify(inRaster2013, 'Value', remap, 'NODATA')
reclassified2023 = Reclassify(inRaster2023, 'Value', remap, 'NODATA')
reclassified2013.save(outRec_2013)
reclassified2023.save(outRec_2023)

# Perform raster calculation
rasterDiff = Raster(outRec_2023) - Raster(outRec_2013)

# Zonal Statistics as table
ZonalStatisticsAsTable(zonalFeature, 'target_field', rasterDiff, outTable, 'DATA','SUM' )

# Convert this table to .xlsx file
arcpy.TableToExcel_conversion(outTable, excelFile)