# coding:utf-8
'''
获取积分页面并写入
'''
from MySqlDB.MySqlConn import Mysql
from bs4 import BeautifulSoup
import ConfigStart
import urllib
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')
class SecondToJifen():
    def __init__(self):
        pass
    def getJifen(self,limit):
        mysql = Mysql()
        sqlAll = "select * from leagueyearinfo limit %s,10 "
        resultSelect=mysql.getAll(sqlAll,limit)
        l = []
        i = 0
        sqlInsert="INSERT INTO leagueyearinfo(p_id,p_jifen_url) VALUES "
        for resultChild in  resultSelect:
            webfile=urllib.urlopen(resultChild['p_league_url'])
            webcontext = webfile.read()
            webfile.close()
            webContent = unicode(webcontext, 'gbk')
            soup = BeautifulSoup(webContent, ConfigStart.PARSEMETHOD)
            jifenUrl =soup.find_all(href=re.compile("jifen-"))

            for getJifen in jifenUrl:
                if(getJifen.string == "赛程积分榜"):
                    print getJifen['href']
                    #ls =[resultChild['p_id'],ConfigStart.STARTURL+getJifen['href']]
                    l.append(resultChild['p_id'])
                    l.append(ConfigStart.STARTURL+getJifen['href'])
                    if i==0:
                        sqlInsert += "(%s,%s)"
                        i=1
                    else:
                        sqlInsert += ",(%s,%s)"
            pass
        sqlInsert += " ON DUPLICATE KEY UPDATE p_jifen_url=VALUES(p_jifen_url)"
        print sqlInsert
        result = mysql.update(sqlInsert, l)
        print result
        pass
        mysql.dispose()
    pass
pass
if __name__ == '__main__':
    #测试
    test = SecondToJifen()
    test.getJifen(0)