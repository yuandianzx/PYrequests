import os
import xlrd
from API_TEST_FRAME.common.config_utils import configUtils

excel_path = os.path.join(os.path.dirname(__file__), configUtils.read_config('path', 'testcase_path'), 'test.xlsx')
print(excel_path)
workbook = xlrd.open_workbook(excel_path)   # 创建一个工作簿对象
sheet =  workbook.sheet_by_index(0)         # 根据获取sheet页
nrows = sheet.nrows     # 获取总行数
ncols = sheet.ncols     # 获取总列数
first_row = sheet.row_values(0)
# print(first_row)
sheet_list = []
for row in range(1,nrows):      # 将excel值取出转换为字典，并追加值列表中
    dict = {}
    for col in range(0,ncols):
        cell_value = sheet.cell_value(row, col)
        dict[first_row[col]] = cell_value
    sheet_list.append(dict)
    # print(dict)
print(sheet_list)



