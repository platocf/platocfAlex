# coding:utf-8
'''
获取所有的数据对应页面的数据
'''
from MySqlDB.MySqlConn import Mysql
import ConfigStart
import urllib
import gzip
import StringIO
from bs4 import BeautifulSoup
import sys
import urllib2
reload(sys)
sys.setdefaultencoding(ConfigStart.UTF8)
class AnalysisData():
    def __init__(self):
        pass
    pass
    def getDataFromMatchInfo(self,limit):
        mysql=Mysql()
        sqlAll = ConfigStart.SELECTFROMMATCHINFOLIMIT
        resultSelect = mysql.getAll(sqlAll, limit)
        if resultSelect == False:
            print "没有要查找的数据"
            return
        for resultChild in  resultSelect:
            fid = resultChild['fid']
            ouzhiUrl = ConfigStart.ANALYSISOUZHIURL%(fid)
            request = urllib2.Request(ouzhiUrl)
            request.add_header("User-Agent",
                               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36")
            request.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
            request.add_header("Accept-Encoding", "gzip, deflate, sdch")
            webfile = urllib2.urlopen(request)
            webcontext = webfile.read()
            print webcontext
            webcontext = gzip.GzipFile(fileobj=StringIO.StringIO(webcontext), mode="r")
            webcontext = webcontext.read().decode('gbk')
            print webcontext
            soup = BeautifulSoup(webcontext, ConfigStart.PARSEMETHOD)
            ouzhiData1=soup.find_all(ttl='zy')
            print ouzhiData1
            pass
        pass
        pass
    pass
pass
if __name__ == '__main__':
    analysis = AnalysisData()
    analysis.getDataFromMatchInfo(10)