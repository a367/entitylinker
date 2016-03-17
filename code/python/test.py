# -*- coding: utf-8 -*-

import requests
import threading
import json
import sys
from lxml import etree
reload(sys)
sys.setdefaultencoding('utf8')

results = []

def get_proxies_from_site():
    url = 'http://proxy.ipcn.org/country/'
    xpath = '/html/body/div[last()]/table[last()]/tr/td/text()'
    
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8,ja;q=0.6,en;q=0.4',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Host':'proxy.ipcn.org',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
        }

    r = requests.get(url,headers=headers)
    tree = etree.HTML(r.text)

    results = tree.xpath(xpath)

    proxies = [line.strip() for line in results]


    return proxies

def check(proxy):
    url = 'http://lwons.com/wx'
    succeed = False
    try:
        r = requests.get(url, proxies=proxy)
        if r.text == 'default':
            succeed = True
    except Exception, e:
        print 'error:'
        succeed = False
    if succeed:
        print 'succeed:'
        results.append(proxy)




#使用http://lwons.com/wx网页来测试代理主机是否可用
def get_valid_proxies(proxies):
    
    threads = []

    for p in proxies[:100]:
        proxy = {'http': 'http://' + p}
        t = threading.Thread(target=check,args=(proxy,))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()

def webPost(proxy):
    url = 'http://bbs.cdstm.cn/misc.php?action=votepoll&fid=208&tid=29453&pollsubmit=yes&quickforward=yes'

    payload = {
        'fromhash':'33bb819a',
        'pollanswers[]':'494',
        'pollsubmit':'true'
        }
    r = requests.post(url, data=payload, proxies=proxy)
    print 'successful'


if __name__ == '__main__':
    proxies = get_proxies_from_site()

    get_valid_proxies(proxies)
    print 'get %d proxies' %len(results)

    threads = []

    for res in results:
        t = threading.Thread(target=webPost,args=(res,))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
        