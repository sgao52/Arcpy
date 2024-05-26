# This code is designed to use merge function combine all county level data to one, preserve all attributes
# Created by copilot, edited by Shan.
# Second step
import arcpy

# set working environment
arcpy.env.workspace = r'H:\ProjectGISData\HeTianProject\HeTianProject.gdb'

# list of features to merge
features = [
    r'H:\ProjectGISData\HeTianProject\和田数据分类\2016\于田县\新疆自治区65于田县653226_xz_2016.shp',
    r'H:\ProjectGISData\HeTianProject\和田数据分类\2016\和田市\新疆自治区65和田市653201_xz_2016.shp',
    r'H:\ProjectGISData\HeTianProject\和田数据分类\2016\墨玉县\新疆自治区65墨玉县653222_xz_2016.shp',
    r'H:\ProjectGISData\HeTianProject\和田数据分类\2016\民丰县\新疆自治区65民丰县653227_xz_2016.shp',
    r'H:\ProjectGISData\HeTianProject\和田数据分类\2016\洛浦县\新疆自治区65洛浦县653224_xz_2016.shp',
    r'H:\ProjectGISData\HeTianProject\和田数据分类\2016\皮山县\新疆自治区65皮山县653223_xz_2016.shp',
    r'H:\ProjectGISData\HeTianProject\和田数据分类\2016\策勒县\新疆自治区65策勒县653225_xz_2016.shp'
]

# Output feature class
output_feature_class = 'MergedFeatureClass'

# Use merge tool
arcpy.Merge_management(features, output_feature_class)
print('merge complete')