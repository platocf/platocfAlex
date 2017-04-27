# coding:utf-8
from MySqlDB.MySqlConn import Mysql
from bs4 import BeautifulSoup
import bs4
import ConfigStart
import urllib
import json
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
    def getMatchInfo(self,limit):
        mysql = Mysql()
        sqlAll = "select * from matchurl limit %s,10"
        resultSelect = mysql.getAll(sqlAll, limit)
        if resultSelect == False:
            return
        for resultChild in resultSelect:
            webfile = urllib.urlopen(resultChild['p_url'])
            webcontext = webfile.read()
            webfile.close()
            webContent = unicode(webcontext, 'gbk')
            soup = BeautifulSoup(webContent, ConfigStart.PARSEMETHOD)
            listInfo=soup.find_all(id='div_group_list')
            rounds=[] #当前第几回合或第几组
            stid=resultChild['p_url'].split("jifen-")[1].split("/")[0]
            c = 'score'
            a = 'getmatch'
            if(listInfo.__len__()>0):
                for listChild in listInfo[0].children:
                    if(type(listChild) == bs4.element.Tag):
                        if (listChild['data-group'] != 'all'):
                            rounds.append(listChild['data-group'])
                            pass
                    pass
                pass
            pass
            listInfo=soup.find_all(id='match_group')
            if (listInfo.__len__() > 0):
                for listChild in listInfo[0].children:
                    if (type(listChild) == bs4.element.Tag):
                        if (listChild.a['data-group'] != 'all'):
                            rounds.append(listChild.a['data-group'])
                            pass
                    pass
                pass
            pass
            #lmb3
            listInfo = soup.find_all(class_='lmb3')
            asc=0
            for listC in  listInfo:
                asc +=1
                rounds.append(asc)
                pass
            pass
            urlInfo ="http://liansai.500.com/index.php?"
            if(rounds.__len__()==0):
                insertContext = []
                sqlInsert = "INSERT INTO `matchinfo` (`p_leagueid`, `fid`, `ghalfscore`, `gid`, `gname`, `gscore`, `gstanding`, `gsxname`, `handline`, `hhalfscore`, `hid`, `hname`, `hscore`, `hstanding`, `hsxname`, `round`, `status`, `stime`) VALUES "
                urlInfo += "c="+c
                urlInfo += "&a="+a
                urlInfo += "&stid="+stid
                jsonContext = urllib.urlopen(urlInfo)
                jsonData = jsonContext.read()
                jsonContext.close()
                jsonData = unicode(jsonData, 'gbk')
                jsonData = json.loads(jsonData)
                index=0
                for jsonDataChild in jsonData:
                    print jsonDataChild
                    if index==0:
                        sqlInsert += "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        index=1
                    else:
                        sqlInsert += ",(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        pass
                    insertContext.append(resultChild['pid'])
                    insertContext.append(jsonDataChild['fid'])
                    insertContext.append(jsonDataChild['ghalfscore'])
                    insertContext.append(jsonDataChild['gid'])
                    insertContext.append(jsonDataChild['gname'])
                    insertContext.append(jsonDataChild['gscore'])
                    insertContext.append(jsonDataChild['gstanding'])
                    insertContext.append(jsonDataChild['gsxname'])
                    insertContext.append(jsonDataChild['handline'])
                    insertContext.append(jsonDataChild['hhalfscore'])
                    insertContext.append(jsonDataChild['hid'])
                    insertContext.append(jsonDataChild['hname'])
                    insertContext.append(jsonDataChild['hscore'])
                    insertContext.append(jsonDataChild['hstanding'])
                    insertContext.append(jsonDataChild['hsxname'])
                    insertContext.append(jsonDataChild['round'])
                    insertContext.append(jsonDataChild['status'])
                    insertContext.append(jsonDataChild['stime'])
                    pass
                if index==0:
                    continue
                resInfo=mysql.update(sqlInsert,insertContext)
                print resInfo
            else:
                for roundChild in rounds:
                    insertContext = []
                    sqlInsert = "INSERT INTO `matchinfo` (`p_leagueid`, `fid`, `ghalfscore`, `gid`, `gname`, `gscore`, `gstanding`, `gsxname`, `handline`, `hhalfscore`, `hid`, `hname`, `hscore`, `hstanding`, `hsxname`, `round`, `status`, `stime`) VALUES "
                    urlInfo += "c=" + c
                    urlInfo += "&a=" + a
                    urlInfo += "&stid=" + stid
                    urlInfo += "&round="+str(roundChild)
                    jsonContext = urllib.urlopen(urlInfo)
                    jsonData = jsonContext.read()
                    jsonContext.close()
                    jsonData = unicode(jsonData, 'gbk')
                    jsonData = json.loads(jsonData)
                    index = 0
                    for jsonDataChild in jsonData:
                        print jsonDataChild
                        if index == 0:
                            sqlInsert += "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            index = 1
                        else:
                            sqlInsert += ",(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            pass
                        insertContext.append(resultChild['pid'])
                        insertContext.append(jsonDataChild['fid'])
                        insertContext.append(jsonDataChild['ghalfscore'])
                        insertContext.append(jsonDataChild['gid'])
                        insertContext.append(jsonDataChild['gname'])
                        insertContext.append(jsonDataChild['gscore'])
                        insertContext.append(jsonDataChild['gstanding'])
                        insertContext.append(jsonDataChild['gsxname'])
                        insertContext.append(jsonDataChild['handline'])
                        insertContext.append(jsonDataChild['hhalfscore'])
                        insertContext.append(jsonDataChild['hid'])
                        insertContext.append(jsonDataChild['hname'])
                        insertContext.append(jsonDataChild['hscore'])
                        insertContext.append(jsonDataChild['hstanding'])
                        insertContext.append(jsonDataChild['hsxname'])
                        insertContext.append(jsonDataChild['round'])
                        insertContext.append(jsonDataChild['status'])
                        insertContext.append(jsonDataChild['stime'])
                        pass
                    if index == 0:
                        continue
                    resInfo = mysql.update(sqlInsert, insertContext)
                    print resInfo
                    pass
                pass
                #INSERT INTO `matchinfo` (`p_leagueid`, `fid`, `ghalfscore`, `gid`, `gname`, `gscore`, `gstanding`, `gsxname`, `handline`, `hhalfscore`, `hid`, `hname`, `hscore`, `hstanding`, `hsxname`, `round`, `status`, `stime`) VALUES ('1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2017-04-21 17:24:58')

        pass
        mysql.dispose()
    pass
pass
if __name__ == '__main__':
    test = JifenToMatchUrl()
    test.getMatchInfo(10)