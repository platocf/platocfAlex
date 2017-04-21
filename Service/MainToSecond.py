# coding:utf-8
'''
从开始的主页跳到第二页
'''
from bs4 import BeautifulSoup
from MySqlDB.MySqlConn import Mysql
import bs4
import urllib
import ConfigStart
import string
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class MainToSecond():
    def __init__(self):
        #init something
        pass
    @staticmethod
    def getSecondUrl():
        # allraceMainWrap
        try:
            webfile = urllib.urlopen(ConfigStart.STARTURL)
            webContent=webfile.read()
            webfile.close()
            soup = BeautifulSoup(webContent,ConfigStart.PARSEMETHOD)
            allraceMainWrap=soup.find_all(id=ConfigStart.LEAGUESDIV)
            #获取到网页后开始分配数据库资源
            mysql = Mysql()
            #i为分区赛事
            i=-1;
            # 数据模型为p_name p_type p_country p_sport_type p_main_type
            p_name = ''
            p_type = 1
            p_country = ''
            p_sport_type = 1
            p_main_type = ''
            sqlAll = "insert into league(p_name,p_type,p_country,p_sport_type,p_main_url) values(%s,%s,%s,%s,%s)"
            for child in allraceMainWrap[ConfigStart.DIVTOPINDEX].children:
                if(type(child)==bs4.element.Tag):
                    i = i+1
                    #print child
                    singleUrl=child.find_all(class_=["lallrace_main_list","clearfix"])
                    #print singleUrl
                    for psingleUrl in singleUrl:
                        #print psingleUrl
                        for getUrlTag in psingleUrl:
                            if (type(getUrlTag) == bs4.element.Tag):

                                if(type(getUrlTag.div) == type(None)):
                                    print getUrlTag.a['href']
                                    print getUrlTag.span.string.encode('utf-8').replace(' ','')
                                    p_name = getUrlTag.span.string.encode('utf-8').replace(' ','')
                                    p_type =i+1
                                    p_country=''
                                    p_main_type= ConfigStart.STARTURL+getUrlTag.a['href']
                                    sqlString = "select count(*) as count from league where p_name=%s and p_type=%s and p_country=%s ;"
                                    lSelect=[p_name, p_type, p_country]
                                    resultSelect = mysql.getOne(sqlString,lSelect)
                                    if resultSelect['count']==0:
                                        l = [[p_name, p_type, p_country, p_sport_type, p_main_type]]
                                        result = mysql.insertMany(sqlAll, l)
                                        print result
                                        pass
                                else:
                                    #获取到国家
                                    print getUrlTag.span.string.encode('utf-8').replace(' ','')
                                    #获取联赛及各个Url
                                    for leagueInfo in getUrlTag.div.children:
                                        if (type(leagueInfo) == bs4.element.Tag):
                                            print leagueInfo.string
                                            print leagueInfo['href']
                                            p_name=leagueInfo.string.encode('utf-8').replace(' ','')
                                            p_main_type=ConfigStart.STARTURL+leagueInfo['href']
                                            p_type=i+1
                                            p_country=getUrlTag.span.string.encode('utf-8').replace(' ','')
                                            sqlString = "select count(*) as count from league where p_name=%s and p_type=%s and p_country=%s ;"
                                            lSelect = [p_name, p_type, p_country]
                                            resultSelect = mysql.getOne(sqlString,lSelect)
                                            if resultSelect['count'] == 0:
                                                l = [[p_name, p_type, p_country, p_sport_type, p_main_type]]
                                                result = mysql.insertMany(sqlAll, l)
                                                print result
                                                pass
                                        pass
                                print ConfigStart.MATCHPARTION[i]
                        pass
                    pass
                pass
            pass
            #各洲的杯赛 lrace_bei
            allraceCup = soup.find_all(class_=ConfigStart.CPUMATCHTAG)
            for cup in allraceCup:
                i=i+1
                print cup
                print cup.a.string
                print cup.a['href']

                for cupChild in cup.find_all('a'):
                    print cupChild
                    p_name = cupChild.string.encode('utf-8').replace(' ', '')
                    p_type = i + 1
                    p_country = ''
                    p_main_type = ConfigStart.STARTURL + cupChild['href']
                    sqlString = "select count(*) as count from league where p_name=%s and p_type=%s and p_country=%s ;"
                    lSelect = [p_name, p_type, p_country]
                    resultSelect = mysql.getOne(sqlString, lSelect)
                    if resultSelect['count'] == 0:
                        l = [[p_name, p_type, p_country, p_sport_type, p_main_type]]
                        result = mysql.insertMany(sqlAll, l)
                        mysql.end()
                        print result
                        pass
                pass
            mysql.dispose()
        except Exception, e:
            print Exception, ":", e
            pass
        pass
        return 1
    pass

pass