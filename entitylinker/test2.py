#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


code = open('entitylinker.py','r').read()
lexer = get_lexer_by_name("python",stripall = True)
formatter = HtmlFormatter(style = "monokai", monospace = True)
result = '<link rel="stylesheet" type="text/css" href="aaa.css">\n'+ highlight(code, lexer, formatter)

open('test.html','wb').write(result)

open('aaa.css','wb').write(formatter.get_style_defs('.highlight')) 