import xlrd
import os
import logging

class Helper(object):

    def readExcels(self,nrow):
        # 读取Excel数据 nrow是输入的行数
        table = xlrd.open_workbook('D:\Project\TestCase\Gjs_Po\data\Gjsinfo.xlsx', 'r')
        sheet = table.sheet_by_index(0)
        return sheet.row_values(nrow)

    def readusername(self,nrow):
        # 读取用户名
        return str(self.readExcels(nrow)[0])  # 强制转换为str

    def readpassword(self,nrow):
        # 读取密码
        return str(self.readExcels(nrow)[1])

    def readAssertText(self,nrow):
        # 读取预期结果
        return str(self.readExcels(nrow)[2])

    def dirName(self,filename,filePath='log'):
        #定义日志文件 filename = log.md 为存储日志
        return os.path.join(os.path.dirname(os.path.dirname(__file__)),filePath,filename)

    def log(self,log_content):
        '''日志定义级别'''
        # 定义文件
        logFile = logging.FileHandler(self.dirName('logInfo.md'), 'a',encoding='utf-8')
        # log格式
        fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s')
        logFile.setFormatter(fmt)

        # 定义日志
        logger1 = logging.Logger('logTest', level=logging.DEBUG)
        logger1.addHandler(logFile)
        logger1.info(log_content)

