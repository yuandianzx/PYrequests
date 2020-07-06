import os
import xlrd

excel_path = os.path.join(os.getcwd(), '..', 'test_case\\test.xlsx')
print(excel_path)
workbook = xlrd.open_workbook(excel_path)   # 创建一个工作簿
# workbook.
