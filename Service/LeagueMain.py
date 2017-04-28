# coding:utf-8
'''
联赛的主页信息获取
'''
from BEANS.LeagueYearInfo import *
from BEANS.MatchUrl import *
from BEANS.League import *
from bs4 import BeautifulSoup
from MySqlDB.MySqlConn import Mysql
import bs4
import urllib
import ConfigStart
import string
import re
import sys
import threading
import time
from MySqlDB.MySqlConn import Mysql
reload(sys)
sys.setdefaultencoding('utf-8')
class LeagueMain():
    def __init__(self):
        print "开始抓取联赛信息"
        pass
    '''
    获取互斥锁
    '''
    def startLeagueMain(self,mutex):
        #获取数据库资源
        mysql = Mysql()
        p_id,p_name,p_type,p_country,p_main_url=0,'',0,'',''
        if mutex.acquire():
            sqlString = ConfigStart.SELECTFROMLEAGUECRAWLER
            result=mysql.getOne(sqlString)
            if isinstance(result,bool):
                print "分析完毕"
                mutex.release()
                mysql.dispose()
                return
                pass
            else:
                mysql.update(ConfigStart.UPDATELEAGUESETCRAWLER,result[League.p_id])
                print result[League.p_name]
                p_id,p_name,p_type,p_country,p_main_url=result[League.p_id],\
                                                        result[League.p_name],result[League.p_type],result[League.p_country],result[League.p_main_url]
            mutex.release()
            pass
        #获取每个联赛现存所有赛季并得到对应的url
        print "正在获取联赛___(%s)___的所有赛季信息获取的url为:%s " % (p_name,p_main_url)
        webfile = urllib.urlopen(p_main_url)
        webContent = webfile.read()
        webfile.close()
        webContent=unicode(webContent,ConfigStart.GBK)
        soup = BeautifulSoup(webContent, ConfigStart.PARSEMETHOD)
        leagueYears=soup.find_all(class_=ConfigStart.DROPLISTCLASS)
        for leagueYear in leagueYears[0].children:
            if(type(leagueYear)== bs4.element.Tag):
                print leagueYear.a[ConfigStart.STRINGTITLE]
                print leagueYear.a[ConfigStart.HREF]
                #print re.findall(r'\b\d+\b',leagueYear.a['title'])
                l = [[p_id, ConfigStart.STARTURL+leagueYear.a[ConfigStart.HREF],leagueYear.a[ConfigStart.STRINGTITLE], leagueYear.a.string]]
                sqlInsert = ConfigStart.INSERTINTOLEAGUEYEARINFO
                result = mysql.insertMany(sqlInsert, l)
                print result
        pass
        mysql.dispose()
    def getWaitCrawler(self):
        mysql = Mysql()
        sqlString = ConfigStart.SELECTCOUNTFROMLEAGUECRAWLER
        result = mysql.getOne(sqlString)
        mysql.dispose()
        return result[ConfigStart.RESULT]
        pass
    pass
pass
if __name__ == ConfigStart.MAIN:
    test=LeagueMain()
    print  test.getWaitCrawler()