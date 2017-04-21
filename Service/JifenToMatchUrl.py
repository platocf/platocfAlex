# coding:utf-8
from MySqlDB.MySqlConn import Mysql
from bs4 import BeautifulSoup
import ConfigStart
import urllib
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')
class JifenToMatchUrl():
    def __init__(self):
        pass
    pass
    def getMatchUrl(self,limit):
        mysql = Mysql()
        sqlAll = "select * from leagueyearinfo limit %s,10 "
        resultSelect = mysql.getAll(sqlAll, limit)
        if resultSelect==False:
            return
        for resultChild in  resultSelect:
            webfile=urllib.urlopen(resultChild['p_jifen_url'])
            webcontext = webfile.read()
            webfile.close()
            webContent = unicode(webcontext, 'gbk')
            soup = BeautifulSoup(webContent, ConfigStart.PARSEMETHOD)
            getUrls=soup.find_all(class_="ltab_btn")
            sqlInsert ="INSERT INTO matchurl(p_leagueyearinfoid,p_url,p_property) VALUES "
            l=[]
            i=0
            print resultChild['p_jifen_url']
            for getUrl in  getUrls:
                if getUrl.string.find("赛制")>=0:
                    # resultOne=mysql.getOne("select * from institution where p_matchid=%s",resultChild['p_leagueid'])
                    # if resultOne == False:
                    #     t=[]
                    #     t.append(resultChild['p_leagueid'])
                    #     mysql.insertOne("INSERT INTO institution(p_matchid,p_institution) VALUES (%s,%s) ",t)
                    #     pass
                    break
                if i==0:
                    sqlInsert +="(%s,%s,%s)"
                    i=1
                    pass
                else:
                    sqlInsert +=",(%s,%s,%s)"
                    pass
                l.append(resultChild['p_id'])
                l.append(ConfigStart.STARTURL+getUrl['href'])
                l.append(getUrl.string)
                pass
            if l.__len__()==0:
                continue
            resultInsert = mysql.update(sqlInsert,l)
            print resultInsert
            pass

        pass
    pass
pass
if __name__ == '__main__':
    test = JifenToMatchUrl()
    test.getMatchUrl(10)