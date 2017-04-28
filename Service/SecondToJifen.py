# coding:utf-8
'''
获取积分页面并写入
'''
from BEANS.LeagueYearInfo import *
from BEANS.MatchUrl import *
from BEANS.League import *
from MySqlDB.MySqlConn import Mysql
from bs4 import BeautifulSoup
import ConfigStart
import urllib
import sys
import re
reload(sys)
sys.setdefaultencoding(ConfigStart.UTF8)
class SecondToJifen():
    def __init__(self):
        pass
    def getJifen(self,limit):
        mysql = Mysql()
        sqlAll = ConfigStart.SELECTFROMLEAGUEYEARINFOLIMIT
        resultSelect=mysql.getAll(sqlAll,limit)
        l = []
        i = 0
        if resultSelect==False:
            return
        sqlInsert=ConfigStart.UPDATELEAGUEYEARINFO_TOP
        for resultChild in  resultSelect:
            webfile=urllib.urlopen(resultChild[LeagueYearInfo.p_league_url])
            webcontext = webfile.read()
            webfile.close()
            webContent = unicode(webcontext, ConfigStart.GBK)
            soup = BeautifulSoup(webContent, ConfigStart.PARSEMETHOD)
            jifenUrl =soup.find_all(href=re.compile(ConfigStart.COMPILEJIFEN))
            for getJifen in jifenUrl:
                if(getJifen.string == ConfigStart.STRINGJIFEN):
                    print getJifen[ConfigStart.HREF]
                    l.append(resultChild[LeagueYearInfo.p_id])
                    l.append(ConfigStart.STARTURL+getJifen[ConfigStart.HREF])
                    if i==ConfigStart.FALSE:
                        sqlInsert += "(%s,%s)"
                        i=1
                    else:
                        sqlInsert += ",(%s,%s)"
            pass
        sqlInsert += ConfigStart.UPDATELEAGUEYEARINFO_BOTTOM
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
    for i in range(40):
        test.getJifen(32000+i*10)