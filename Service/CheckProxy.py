#!/usr/bin/env python  
# -*- coding:utf8 -*-  
import urllib2  
import time  
from bs4 import BeautifulSoup
from MySqlDB.MySqlConn import Mysql
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
req_timeout = 5
testUrl = "http://www.baidu.com/"  
testStr = "百度"
file1 = open('proxy.txt' , 'w')  
# url = ""  
# req = urllib2.Request(url,None,req_header)  
# jsondatas = urllib2.urlopen(req,None,req_timeout).read()  
cookies = urllib2.HTTPCookieProcessor()  
checked_num = 0  
grasp_num = 0  
for page in range(1, 160):  
    req = urllib2.Request('http://www.xici.net.co/nn/' + str(page), None, req_header)  
    html_doc = urllib2.urlopen(req, None, req_timeout).read()  
    # html_doc = urllib2.urlopen('http://www.xici.net.co/nn/' + str(page)).read()  
    soup = BeautifulSoup(html_doc)  
    trs = soup.find('table', id='ip_list').find_all('tr')  
    for tr in trs[1:]:  
        tds = tr.find_all('td')  
        ip = tds[1].text.strip()  
        port = tds[2].text.strip()  
        protocol = tds[5].text.strip()  
        if protocol == 'HTTP' or protocol == 'HTTPS':  
            #of.write('%s=%s:%s\n' % (protocol, ip, port))  
            print '%s=%s:%s' % (protocol, ip, port)  
            grasp_num +=1  
            proxyHandler = urllib2.ProxyHandler({"http": r'http://%s:%s' % (ip, port)})  
            opener = urllib2.build_opener(cookies, proxyHandler)  
            opener.addheaders = [('User-Agent',  
                                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')]  
            t1 = time.time()  
            try:  
                req = opener.open(testUrl, timeout=req_timeout)  
                result = req.read()  
                timeused = time.time() - t1  
                pos = result.find(testStr)  
                if pos > 1:  
                    file1.write(protocol+"\t"+ip+"\t"+port+"\n")  
                    checked_num+=1
                    print checked_num, grasp_num
                    insertSql = "insert into proxyip(address,port) values(%s,%s)"
                    l=[]
                    l.append(ip)
                    l.append(port)
                    print mysql.update(insertSql,l)
                else:  
                    continue  
            except Exception,e:  
                continue  
file1.close()  
print checked_num,grasp_num  