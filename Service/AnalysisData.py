# coding:utf-8
'''
获取所有的数据对应页面的数据
'''
from MySqlDB.MySqlConn import Mysql
import ConfigStart
import urllib
import gzip
import json
import StringIO
from bs4 import BeautifulSoup
import sys
import urllib2
from tools.OpenUrl import *
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
            i = 0
            '''
            =====================================欧赔开始================================================
            '''
            while True:
                url = ConfigStart.ANALYSISOUZHIURL % (fid,i * 30)
                openUrls = OpenUrls()
                webcontext = openUrls.getWebContent(url, i)
                soup = BeautifulSoup(webcontext, "html.parser")
                ouzhiData1 = soup.find_all(ttl='zy')
                if ouzhiData1.__len__() == 0:
                    print '获取完毕'
                    break
                j = 0
                for ouzhiDataChild in ouzhiData1:
                    print "------------------------%s------------------------" % (i * 30 + j)
                    print ouzhiDataChild['id']
                    print ouzhiDataChild.contents[3]['title']
                    webjson = openUrls.getWebContent(ConfigStart.ANALYSISOUZHIDATAURL%(fid,ouzhiDataChild['id']),1)
                    webjson=json.loads(webjson)
                    print webjson
                    for webjsonChild in webjson:
                        print webjsonChild[0]
                        #开始写入数据到库中 TODO:
                    j += 1
                    pass
            '''
            ===========================欧赔结束=================================================
            '''
            i += 1
            pass
        pass
        pass
    pass
pass
if __name__ == '__main__':
    analysis = AnalysisData()
    analysis.getDataFromMatchInfo(5000)