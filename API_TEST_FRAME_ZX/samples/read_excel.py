import os
import xlrd
from common.config_utils import ConfigUtils

excel_path = os.path.join(os.path.dirname(__file__), ConfigUtils.read_config('path', 'test_case_path'), 'test_wechat.xlsx')
print(excel_path)
workbook = xlrd.open_workbook(excel_path)   # 创建一个工作簿对象
sheet = workbook.sheet_by_name('Sheet1')         # 根据sheet页的名称创建对象
nrows = sheet.nrows     # 获取总行数
ncols = sheet.ncols     # 获取总列数
first_row = sheet.row_values(0)     # 获取第一行的数据，以列表的形式
# print(first_row)
sheet_list = []
for row in range(1,nrows):      # 将每一行的数据转化为列表，然后写入sheet_list中
    dict = {}
    for col in range(0,ncols):
        dict[first_row[col]] = sheet.cell_value(row, col)
    sheet_list.append(dict)

# print(sheet_list)
print(sheet.merged_cells)       # 返回合并单元格列表，(起始行、结束行、起始列、结束列)跟range函数一样，左闭右开区间。合并单元格只有左上角的单元格有值
rownum = 3
colnum = 0
value = None
for (rlow, rhigh, clow, chigh) in sheet.merged_cells:       # 判断单元格是否属于合并单元格，若属于则将左上角的值赋值给它
    if rownum >= rlow and rownum < rhigh:
        if colnum >= clow and colnum < chigh:
            value = sheet.cell_value(rlow,clow)
            break  # 防止循环判断的时候，出现覆盖值的情况
        else:
            value = sheet.cell_value(rownum, colnum)
    else:
        value = sheet.cell_value(rownum, colnum)
print(value)


# print(sheet.cell_value(11,0))
# print(sheet.cell_value(12,1))



