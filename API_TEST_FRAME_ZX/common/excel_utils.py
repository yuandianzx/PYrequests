import os
import xlrd
from config_utils import ConfigUtils

class ExcelUtils():
    def __init__(self, file_path, sheet_name):  # 最好把sheet_name也作为初始化参数传进来
        self.file_path = file_path
        self.workbook = xlrd.open_workbook(self.file_path)  # 创建一个工作簿对象
        self.sheet = self.workbook.sheet_by_name(sheet_name)    # 根据sheet的名称来创建对象
        self.nrows = self.sheet.nrows
        self.ncols = self.sheet.ncols

    def get_sheet(self):
        '''封装sheet对象，方便扩展'''
        self.a = 1
        return self.sheet

    def get_merged_cell_value(self, row, col):
        '''封装合并单元格取值函数'''
        for (rlow, rhigh, clow, chigh) in self.sheet.merged_cells:     # self.sheet.merged_cells为获取合并单元格信息
            if row >= rlow and row < rhigh:
                if col >= clow and col < chigh:
                    cell_value = self.sheet.cell_value(rlow, clow)  # 如果单元格在合并单元格中，将左上角的值赋值给self.value
                    break  # 防止循环判断的时候，出现覆盖值的情况
                else:
                    cell_value = self.sheet.cell_value(row, col)    # 如果单元格不在合并单元格中，将该单元格的值赋值给self.value
            else:
                cell_value = self.sheet.cell_value(row, col)        # 如果单元格不在合并单元格中，将该单元格的值赋值给self.value
        return cell_value


    def read_excel(self):
        '''读取excel，将excel值取出转换为字典，并追加值列表中'''
        first_row = self.sheet.row_values(0)
        # print(first_row)
        # print(len(self.sheet.merged_cells))
        sheet_list = []
        for self.row in range(1, self.nrows):
            dict = {}
            for self.col in range(0, self.ncols):
                cell_value = self.get_merged_cell_value(self.row, self.col)        # 调用封装的get_merged_cell_value函数
                dict[first_row[self.col]] = cell_value     # 该列第一行作为key，该单元格作为value。以字典的形式存入dict中
            sheet_list.append(dict)     # 将该行的字典数据附加至列表中
        return sheet_list

    def data_conversion(self):
        data_dict = {}
        for row_data in excelUtils.read_excel():
            data_dict.setdefault(row_data['测试用例编号'], []).append(row_data)
        print(data_dict)




if __name__ == '__main__':
    file_path = os.path.join(ConfigUtils.read_config('path', 'test_case_path'), 'test_wechat.xlsx')
    excelUtils = ExcelUtils(file_path, 'Sheet1')
    # for row_data in excelUtils.read_excel():
    #     #     print(row_data)
    excelUtils.data_conversion()