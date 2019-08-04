import xlrd
import os


# def data_file(filename=None):
#     return os.path.join(os.path.dirname(__file__),"excel")

class Excel():
    def __init__(self,filename,sheetName):
        self.data = xlrd.open_workbook(filename)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为 key 值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols
        # 获取单元格内容
        self.row_col = self.table.cell_value(1, 0)
    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于 1")
        else:
            r = []
            j=1
            for i in range(self.rowNum-1):
                s = {}
                # 从第二行取对应 values 值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j+=1
            return r

if __name__ == '__main__':
    filename = ".\\excel\\testdata.xlsx"
    sheetName = "testdata"
    excel = Excel(filename,sheetName)
    print(excel.row_col)
    print(excel.dict_data())