#!/usr/bin/env python  
# -*- coding:utf8 -*-  
import urllib2  
import time
from MySqlDB.MySqlConn import Mysql
from Service.ShowCharType import *
import sys  
reload(sys)  
sys.setdefaultencoding( "utf-8" )
mysql = Mysql()
req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',  
  'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',  
  #'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',  
  'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',  
  'Accept-Encoding':'en-us',  
  'Connection':'keep-alive',  
  'Referer':'http://www.baidu.com/'  
   }  
req_timeout = 3
testUrl = "http://www.baidu.com/"
# url = ""  
# req = urllib2.Request(url,None,req_header)  
# jsondatas = urllib2.urlopen(req,None,req_timeout).read()  
cookies = urllib2.HTTPCookieProcessor()  
checked_num = 0  
grasp_num = 0  

req = urllib2.Request('http://api.xicidaili.com/free2016.txt', None, req_header)
html_doc = urllib2.urlopen(req, None, req_timeout).read()
_arr=html_doc.split('\r\n')
while True:
    for _arrChild in _arr:
        print _arrChild
        selectSql = "select count(*) as result from proxyip where address_port=%s "
        res_select=mysql.getOne(selectSql,_arrChild)
        if res_select['result'] == 0:
            proxyHandler = urllib2.ProxyHandler({"http": r'%s' % (_arrChild)})
            opener = urllib2.build_opener(cookies, proxyHandler)
            opener.addheaders = [('User-Agent',
                                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')]
            t1 = time.time()
            try:
                req = opener.open(testUrl, timeout=req_timeout)
                result = req.read()
                charsetCur=chardet_detect_str_encoding(result)
                timeused = time.time() - t1
                insertSql = "insert into proxyip(address_port) values(%s)"
                l=[]
                l.append(_arrChild)
                print mysql.update(insertSql,l)
                mysql.end()
            except Exception,e:
                print e
                pass
            pass
        else:
            continue
    time.sleep(10*60)