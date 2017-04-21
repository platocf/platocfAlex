# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import json
import logging
import MySQLdb
import time
import datetime
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')
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
webfile=urllib.urlopen("http://liansai.500.com/index.php?c=score&a=getmatch&stid=11389&round=1")
webcontext = webfile.read()
soup = BeautifulSoup(webcontext,"html.parser")
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