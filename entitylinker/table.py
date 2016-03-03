#coding=utf8
import xlrd
import xlwt
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class tableManager:
    def __init__(self):
        self.excel = xlrd.open_workbook('..//data//table_data.xls')
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
          
            






    #ctype = 1 # 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
    #value = 'lixiaoluo'
    #xf = 0 # 扩展的格式化 (默认是0)
    #table.put_cell(row, col, ctype, value, xf)
    #table.cell(0,0) # 文本:u'lixiaoluo'
    #table.cell(0,0).value 

#def excelWrite():
#    excel = xlwt.Workbook() #注意这里的Workbook首字母是大写，无语吧
#    sheet = excel.add_sheet('table',cell_overwrite_ok=True)
    
#    s = file('..//data//table_data.tbd').read()
#    tables =  json.loads(s)
#    i = j = count = 0

#    for table in tables:
#        count += 1
#        sheet.write(i,0,u'第%d个表格'%count)
#        i += 1
#        for row in table:
#            j = 0
#            for mention in row:          
#                sheet.write(i,j,mention)
#                j += 1
#            i += 1


#    excel.save('..//data//table_data.xls')


#t = tableManager()
#tables = t.getTable()
