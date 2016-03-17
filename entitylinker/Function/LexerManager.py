#coding=utf8
import os
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


class LexerManager():

    # 核心代码名字首字母是大写的
    def __init__(self,codestyle, isCoreCode=False):
        lexer = get_lexer_by_name(codestyle,stripall = True)
        formatter = HtmlFormatter(style = "monokai", monospace = True)
        css = open('../qss/aaa.css').read().decode('utf-8')

        self.codeDict = {}
        if isCoreCode:
            dir_path = '../code/%s/'%codestyle
        else:
            dir_path = '../data/%s/'%codestyle
        
        dir =  os.listdir(dir_path)
    
        for name in dir:
            code = open(dir_path + name).read().decode('utf-8')
            result = css + highlight(code, lexer, formatter)
            self.codeDict[name] = result

    def getCode(self, filename):
        return self.codeDict[filename]
