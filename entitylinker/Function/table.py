#coding=utf8
import xlrd
import xlwt
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class tableManager:
    def __init__(self):
        self.excel = xlrd.open_workbook('../data/list/table_data.xls')
    def getTable(self):
        table = self.excel.sheet_by_name('table')
        tables = []

        nrows = table.nrows
        ncols = table.ncols

        # 按列存储
        r = 0
        down_flag = False
        while True:
            r += 1

            # 获取当前表格的行数
            next_r = r
            while True:
                if next_r == nrows:
                    down_flag = True
                    break
                if table.cell(next_r,0).value != '':
                    next_r += 1
                else:
                    break

            # 获取当前表格的列数
            next_c = 0
            while True:
                if next_c == ncols:
                    break
                if table.cell(r,next_c).value != '':
                    next_c += 1
                else:
                    break

            t = []
            for cc in range(0,next_c):
                col = []
                for rr in range(r,next_r):
                    col.append(table.cell(rr,cc).value)
                t.append(col)
            tables.append(t)
            if down_flag:
                break
            else:
                r = next_r + 1

        return tables
          
            