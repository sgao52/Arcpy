# This code is used to test field diff in a bunch of mass shapefiles under same survey method, aim to test if there's different fields in same year level data
# created bt copilot, edited by Shan
# This is the very first step of data processing
import arcpy

# define a function to list fields in a shapefile
def list_fields(shapefile):
    fields = arcpy.ListFields(shapefile)
    field_names = [field.name for field in fields]
    return field_names

# function to count rows in shps
def count_rows(shapefile):
    return int(arcpy.GetCount_management(shapefile).getOutput(0))

# list of shapefile paths
shapefiles = [
    r'H:\ProjectGISData\HeTianProject\和田数据分类\2014\于田县\二类\yt_xbm.shp',
    r'H:\ProjectGISData\HeTianProject\和田数据分类\2014\和田市\二类\hetianshi_xbm.shp',
    r'H:\ProjectGISData\HeTianProject\和田数据分类\2014\墨玉县\二类\my_xbm.shp',
    r'H:\ProjectGISData\HeTianProject\和田数据分类\2014\民丰县\二类\mf_xbm.shp',
    r'H:\ProjectGISData\HeTianProject\和田数据分类\2014\洛浦县\二类\luopuxian_xbm.shp',
    r'H:\ProjectGISData\HeTianProject\和田数据分类\2014\皮山县\二类\ps_xbm.shp',
    r'H:\ProjectGISData\HeTianProject\和田数据分类\2014\策勒县\二类\celexian_xbm.shp',
    r'H:\ProjectGISData\HeTianProject\和田数据分类\2014\和田县\二类\hetianxian_xbm.shp'
]

# Dictionary to hold field names for each shp
shapefile_info = {}
# Iterate over shps and list their fields and rows
total_rows = 0
for shapefile in shapefiles:
    fields = list_fields(shapefile)
    rows = count_rows(shapefile)
    shapefile_info[shapefile] = {'fields':fields, 'rows':rows}
    total_rows += rows
    print(f'{shapefile} has {len(fields)} fields : {fields} and {rows} rows.')

print(f'Total number of rows of all shps:{total_rows}.')

# Function to compare fields of all shp
def compare_shp_fields(shapefile_info):
    all_fields = set()
    for info in shapefile_info.values():
        all_fields.update(info['fields'])

    # dictionary to hold difference in fields
    field_diff = {field:[] for field in all_fields}

    # compare fields
    for field in all_fields:
        for shapefile, info in shapefile_info.items():
            if field not in info['fields']:
                field_diff[field].append(shapefile)
    return field_diff

# get the differences in fields
dif = compare_shp_fields(shapefile_info)

print('dif in fields between shps:')
for field, shapefiles in dif.items():
    if shapefiles:
        print(f"Field'{field}' is missing in {','.join(shapefiles)}") # this will print fields that is missing in specific shapefiles