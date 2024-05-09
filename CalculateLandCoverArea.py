import arcpy
from arcpy.sa import *
# This code utilizes the mosaic, reclassify, clip, raster to vector geoprocessing tools to handle landcover raster data, aim to export certain type of landcover area
# Created by copilot, edited by Shan

# Set Env
arcpy.env.workspace = r'H:\ProjectGISData\UzProj\TestArcpy'

# Set local variables
inRaster1 = r'H:\ProjectGISData\UzProj\SatelliteLandCover\41T_20210101-20220101.tif'
inRaster2 = r'H:\ProjectGISData\UzProj\SatelliteLandCover\41S_20210101-20220101.tif'
    # To mosaic multiple images into one, use this list raster
inRasterList = [inRaster1, inRaster2]
inMaskData = r'H:\ProjectGISData\UzProj\gadm41_UZB_shp\gadm41_UZB_0.shp'
mosaicRaster = 'mosaic.tif' # Mosaic raster

# Mosaic Raster
arcpy.MosaicToNewRaster_management(inRasterList, arcpy.env.workspace, mosaicRaster, number_of_bands = 1)
outname = r'H:\ProjectGISData\UzProj\TestArcpy\MaskedTest.tif'
# Execute mask operation and save output
outExtractByMask = ExtractByMask(mosaicRaster, inMaskData)
outExtractByMask.save(outname)

# Reclassify raster and save
reclassField = 'VALUE'
remap = RemapValue([[2,1],[4,1]]) # Assign 2 (Vege) and 4(Wetland) to new value 1
outReclassify = Reclassify('MaskedTest.tif', reclassField, remap, 'NODATA')
outReclassify.save('Reclassified.tif')

# Covnvert raster to polygon
outPolygons = 'TestUziVege.shp'
field = 'value'
arcpy.RasterToPolygon_conversion(outReclassify, outPolygons, 'NO_SIMPLIFY', field)

# Calculate area and add to attribute table
arcpy.AddField_management(outPolygons, 'Area', 'DOUBLE')
arcpy.CalculateField_management(outPolygons, 'Area', '!shape.area@squaremeters!', 'PYTHON_3.9')

print('Process complete')