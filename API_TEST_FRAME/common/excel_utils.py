import os
import xlrd
from config_utils import ConfigUtils

class ExcelUtils():
    def __init__(self, file_path):
        self.file_path = file_path
        self.workbook = xlrd.open_workbook(self.file_path)  # 创建一个工作簿对象
        self.sheet = self.workbook.sheet_by_index(0)
        self.nrows = self.sheet.nrows
        self.ncols = self.sheet.ncols

    def get_sheet(self):        # 封装sheet对象，方便扩展
        return self.sheet

    def read_excel(self):
        first_row = self.sheet.row_values(0)
        # print(first_row)
        sheet_list = []
        for row in range(1, self.nrows):  # 将excel值取出转换为字典，并追加值列表中
            dict = {}
            for col in range(0, self.ncols):
                cell_value = self.sheet.cell_value(row, col)
                dict[first_row[col]] = cell_value
            sheet_list.append(dict)
        return sheet_list

if __name__ == '__main__':
    file_path = os.path.join(ConfigUtils.read_config('path', 'test_case_path'), 'test_wechat.xlsx')
    ExcelUtils = ExcelUtils(file_path)
    print(ExcelUtils.read_excel())