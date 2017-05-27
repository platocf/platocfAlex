# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import urllib,urllib2
import json
from Service.ShowCharType import *
import logging
import MySQLdb
import time
import datetime
import gzip, StringIO
import sys
import re
from tools.OpenUrl import *
import cookielib
# reload(sys)
# sys.setdefaultencoding('gbk')

file=open("6666.log",'wb+')
file.write("%s==========错误的原因:%s--%s"%('1','2','3'))
file.close()

def kelly(s,p,f):
    print 1.0/(1.0/s+1.0/p+1.0/f)
    pass
kelly(2.84,3.4,2.2)
s=datetime.datetime.strptime("2011-1-1 3:00", '%Y-%m-%d %H:%M')
datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print s
str1="888"
c = type(str1)

request = urllib2.Request("http://www.500.com")
opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))#为了开启回显，需要手动构造一个HTTPHandler
feeddata = opener.open(request).read()

loginUrl = "http://www.126.com"
request = urllib2.Request(loginUrl)
request.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36")
request.add_header("Accept",
                   "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
request.add_header("Accept-Encoding", "gzip, deflate, sdch")
#request.add_header("X-Requested-With","XMLHttpRequest")
request.add_header("Accept-Language","zh-CN,zh;q=0.8")
request.add_header("Host","www.126.com")
request.add_header("Upgrade-Insecure-Requests","1")
request.add_header("Cookie","starttime=; logType=")
request.add_header("Content-Type","text/html")
cj = cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)
resp = opener.open(request).read()
for index, cookie in enumerate(cj):
    print '[',index, ']',cookie
#time.strftime('%Y-%m-%d %H:%M:%S')
# from mysqlDB.mysqlOpr import *
# opr=mysqlOpr('192.168.10.210','root','123456',3306,'poi','utf8')
# mysqlOpr.initMysqlDB()
#conn=mysql.connect(host='192.168.10.210',user='root',passwd='123456',db='poi')
# try:
#     conn = MySQLdb.connect(host='192.168.10.210',user='root',passwd='123456',db='poi',port=3306,charset='utf8')
#     cur = conn.cursor()
#     conn.select_db('poi')
#     count = cur.execute('select * from league')
#     print 'there has %s rows record' % count
#
#     result = cur.fetchone()
#     print result
#     #print 'ID: %s info %s' % result
#
#     results = cur.fetchmany(5)
#     for r in results:
#         print r[1]
#
#     print '==' * 10
#     cur.scroll(0, mode='absolute')
#
#     results = cur.fetchall()
#     for r in results:
#         print r[1]
#
#     conn.commit()
#     cur.close()
#     conn.close()
#
# except MySQLdb.Error, e:
#     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
#webfile = urllib.urlopen('http://liansai.500.com/team/667/')
#request=urllib2.Request("http://odds.500.com/fenxi1/inc/shuju_jiaozhan.php?id=607163&hash=97e865f&home=0&limit=999&bhbc=0&r=1&callback=ajax")
#http://odds.500.com/fenxi1/yazhi.php?id=654875&ctype=1&start=30&r=1&style=0&guojia=0
# i=0
# while True:
#     url = "http://odds.500.com/fenxi1/ouzhi.php?id=607186&ctype=1&start=%s&r=1&style=0&guojia=0&chupan=1"%(i*30)
#     openUrls = OpenUrls()
#     webcontext=openUrls.getWebContent(url,i)
#     soup = BeautifulSoup(webcontext,"html.parser")
#     ouzhiData1=soup.find_all(ttl='zy')
#     if ouzhiData1.__len__() == 0:
#         print '获取完毕'
#         break
#     #print ouzhiData1
#     j=0
#     for ouzhiDataChild in ouzhiData1:
#         print "------------------------%s------------------------"%(i*30+j)
#         print ouzhiDataChild['id']
#         print ouzhiDataChild.contents[3]['title']
#         j+=1
#         pass
#     i += 1

# res=json.loads(webcontext)
# for listvalue in res:
#     print listvalue
# print webcontext
# print soup
# print soup.title
# print soup.head
# print soup.a
# print soup.div
# print soup.div.get('style')
# print soup.div.attrs
# print soup.div.string
#
# print soup.div.contents
# for child in soup.descendants:
#     print child
# file_object = open('thefile.txt', 'wb')
# file_object.write(webcontext)
# file_object.close( )