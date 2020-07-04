import os
import xlrd

excel_path = os.path.join(os.getcwd(), 'test.xlsx')     # 获取excel文件的路径
# print(excel_path)

workbook = xlrd.open_workbook(excel_path)           # 使用xlrd创建一个工作薄对象
sheet = workbook.sheet_by_name('Sheet1')           #根据工作表的名称创建表格对象
# sheet = workbook.sheet_by_index(0)                # 根据工作表的索引创建表格对象
# print(sheet)
# print(sheet.row_values(0))      # 读取test.excel的Sheet1中第一行的数据
print(sheet.col_values(1))        # 作业一：读取test.excel的Sheet1中第二列的数据

# print(sheet.merged_cells)
def judgeMerge(x,y):            # 作业二：判断单元格是否是合并单元格
    merged = sheet.merged_cells
    for rlow,rhigh,clow,chigh in merged:
        if x >=rlow and x < rhigh:
            if y >= clow and y < chigh:
                print('此单元格是合并的')
            else:
                print('此单元格是普通单元格')

# x = int(input())
# y = int(input())
# judgeMerge(x,y)
col2 = sheet.col_values(1)  # 取出test.xlsx的第二列数据
print(col2.sort())


