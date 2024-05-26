# This code decrypt Chinese geo survey data from short cut pinyin to mandarin/english readable format
# created by copilot, edited by shan.
# Third step
import arcpy
import xlrd

# Set excel path and feature path, select first sheet
excel_path = r'H:\ProjectGISData\HeTianProject\CodeTest\HeTianTest1.xls' # xlrd only support .xls file name
featurePath = r'H:\ProjectGISData\HeTianProject\CodeTest\2013和田二类数据.shp'
workbook = xlrd.open_workbook(excel_path)

# Define sheet info
sheets_info = {
    'Xian':'XIAN',
    'DiLei':'DI_LEI',
    'LinZhong':'LIN_ZHONG',
    'YouShi':'YOU_SHI_SZ',
    'LinQuan':'LD_QS'
}

code_to_name = {}
# Iterate over each sheet and row to populate dic
for sheet_name, field_name in sheets_info.items():
    sheet = workbook.sheet_by_name(sheet_name)
    for row_num in range(0, sheet.nrows): # first row is data
        code = sheet.cell(row_num, 0).value
        chinese_name = sheet.cell(row_num, 1).value
        code_to_name[code]=chinese_name

# Print dictionary 
print('Code to Name Mappings')

# Add a new Field for chinese name (Arcpro limit 10 characters)
for field_name in sheets_info.values():
    new_field_name = f'{field_name[:7]}_De'
    if new_field_name not in [f.name for f in arcpy.ListFields(featurePath)]:
        arcpy.AddField_management(featurePath, new_field_name, 'TEXT')

# Update feature class with chinese name\
for field_name in sheets_info.values():
    new_field_name = f'{field_name[:7]}_De'
    with arcpy.da.UpdateCursor(featurePath,[field_name, new_field_name]) as cursor: # Indicate the field that needs to convert
        for row in cursor:
            code = row[0]
            chinese_name = code_to_name.get(code, 'Unknown')
            print(f"Updating {field_name} with {chinese_name}")
            row[1] = chinese_name
            cursor.updateRow(row)

print(f"Updated fields in the feature class at {featurePath}")