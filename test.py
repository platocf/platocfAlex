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
# reload(sys)
# sys.setdefaultencoding('gbk')
s=datetime.datetime.strptime("2011-1-1 3:00", '%Y-%m-%d %H:%M')
print s
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
request=urllib2.Request("http://odds.500.com/fenxi1/ouzhi.php?id=607184&ctype=1&start=30&r=1&style=0&guojia=0&chupan=1")
request.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36")
request.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
request.add_header("Accept-Encoding","gzip, deflate, sdch")
#request.add_header("Content-Type","application/x-www-form-urlencoded")
#request.add_header("X-Requested-With","XMLHttpRequest")
webfile=urllib2.urlopen(request)
webcontext = webfile.read()
chardet_detect_str_encoding(webcontext)
print webcontext
webcontext=gzip.GzipFile(fileobj=StringIO.StringIO(webcontext),mode="r")
webcontext=webcontext.read().decode('utf8')
print webcontext
soup = BeautifulSoup(webcontext,"html.parser")
ouzhiData1=soup.find_all(ttl='zy')
res=json.loads(webcontext)
for listvalue in res:
    print listvalue
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