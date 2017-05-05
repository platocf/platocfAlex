# coding:utf-8
import ConfigStart
import urllib
import gzip
import json
import StringIO
from bs4 import BeautifulSoup
from MySqlDB.MySqlConn import Mysql
import sys
import urllib2
import re
from tools.OpenUrl import *
reload(sys)
sys.setdefaultencoding(ConfigStart.UTF8)
class AnalysisData():
    def __init__(self):
        pass
    pass
    def selectRetCompanyId(self,name,mysql):
        selectSql = "select p_id as result from company where company_name =BINARY%s "
        insertSql = "insert into company(company_name) values(%s)"
        resCount=mysql.getOne(selectSql,name)
        if(resCount==False):
            mysql.insertOne(insertSql,name)
            pass
        pass
        resCount = mysql.getOne(selectSql, name)
        resvalue=0
        if resCount==False:
            print "company表的字段可能不够长"
            pass
        else:
            resvalue=resCount['result']
        return resvalue
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
            print fid
            i = 0
            '''
            =====================================欧赔开始================================================
            '''
            count_cursor = 0
            while True:
                if count_cursor!=i*30:
                    break
                url = ConfigStart.ANALYSISOUZHIURL % (fid,i * 30)
                print "=============================================%s==================================="%url
                openUrls = OpenUrls()
                while True:
                    webcontext = openUrls.getWebContent(url,mysql,i)
                    if webcontext.find('500.com')==-1:
                        continue
                        pass
                    else:
                        break
                soup = BeautifulSoup(webcontext, "html.parser")
                ouzhiData1 = soup.find_all(ttl='zy')
                if ouzhiData1.__len__() == 0:
                    print '获取完毕'
                    break
                j = 0
                for ouzhiDataChild in ouzhiData1:
                    print "------------------------%s------------------------" % (i * 30 + j+1)
                    count_cursor=i * 30 + j+1
                    print ouzhiDataChild['id']
                    insertSql ="INSERT INTO `oupei` (`matchinfoid`, `companyid`, `op_s`, `op_p`, `op_f`, `ret`, `kl_s`, `kl_p`, `kl_f`, `update_time`) VALUES  "
                    insertContext = []
                    companyName = ouzhiDataChild.find_all('td',class_='tb_plgs')
                    print companyName[0]['title']
                    companyId = self.selectRetCompanyId(companyName[0]['title'],mysql)
                    webjson=0
                    while True:
                        try:
                            webjson = openUrls.useProxy(ConfigStart.ANALYSISOUZHIDATAURL%(fid,ouzhiDataChild['id']),mysql,0)
                            webjson=json.loads(webjson)
                            break
                            pass
                        except Exception, e:
                            continue
                            pass
                        pass
                    pass
                    print webjson
                    if webjson.__len__()==0:
                        continue
                    kellyjson=0
                    while True:
                        try:
                            kellyjson = openUrls.useProxy(ConfigStart.ANALYSISOUZHIKELLYURL % (fid, ouzhiDataChild['id']), mysql, 0)
                            kellyjson = json.loads(kellyjson)
                            break
                            pass
                        except Exception, e:
                            continue
                            pass
                        pass
                    pass
                    index=0
                    for webjsonChild in webjson:
                        indexT=0
                        for kellyjsonChild in kellyjson:
                            if index ==indexT:
                                #TODO:添加数据到数据库中
                                if index==0:
                                    insertSql += "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                    pass
                                else:
                                    insertSql += ",(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                    pass
                                insertContext.append(fid)
                                insertContext.append(companyId)
                                insertContext.append(webjsonChild[0])
                                insertContext.append(webjsonChild[1])
                                insertContext.append(webjsonChild[2])
                                insertContext.append(webjsonChild[3])
                                insertContext.append(kellyjsonChild[0])
                                insertContext.append(kellyjsonChild[1])
                                insertContext.append(kellyjsonChild[2])
                                insertContext.append(kellyjsonChild[3])
                                pass
                                break
                                pass
                            pass
                            indexT+=1
                        pass
                        index +=1
                    pass
                    mysql.update(insertSql,insertContext)
                    j += 1
                    pass
                i +=1
                pass
            '''
            ===========================欧赔结束===============让球指数开始==================================
            '''
            i=0
            while False:
                url = ConfigStart.ANALYSISRANGQIU % (fid,i * 30)
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
                    print ouzhiDataChild['cid']
                    print ouzhiDataChild.contents[3]['title']
                    webjson = openUrls.getWebContent(ConfigStart.ANALYSISRANGQIUDATAURL%(fid,ouzhiDataChild['cid'],ouzhiDataChild.contents[5].string),1)
                    webjson=json.loads(webjson)
                    print webjson
                    for webjsonChild in webjson:
                        print webjsonChild[0]
                        #开始写入数据到库中 TODO:
                    j += 1
                    pass
                i += 1
            pass
            '''
                        ===========================让球指数结束===============亚盘开始==================================
            '''
            i = 0
            while False:
                url = ConfigStart.ANALYSISYAZHI % (fid, i * 30)
                openUrls = OpenUrls()
                webcontext = openUrls.getWebContent(url, i)
                soup = BeautifulSoup(webcontext, "html.parser")
                ouzhiData1 = soup.find_all(xls='row')
                if ouzhiData1.__len__() == 0:
                    print '获取完毕'
                    break
                j = 0
                for ouzhiDataChild in ouzhiData1:
                    print "------------------------%s------------------------" % (i * 30 + j)
                    print ouzhiDataChild['id']
                    print ouzhiDataChild.contents[3].a.span.string
                    webjson = openUrls.getWebContentJson(ConfigStart.ANALYSISYAZHIDATAURL % (
                    fid, ouzhiDataChild['id']))
                    soupChild = BeautifulSoup(webjson, "html.parser")
                    webjson = json.loads(webjson)
                    print webjson
                    for webjsonChild in webjson:
                        print webjsonChild[0]
                        # 开始写入数据到库中 TODO:
                    j += 1
                    pass
                i += 1
            pass
            '''
                ===========================亚盘结束===============大小指数开始==================================
            '''
            i = 0
            while False:
                url = ConfigStart.ANALYSISDAXIAO % (fid, i * 30)
                openUrls = OpenUrls()
                webcontext = openUrls.getWebContent(url, i)
                soup = BeautifulSoup(webcontext, "html.parser")
                ouzhiData1 = soup.find_all(xls='row')
                if ouzhiData1.__len__() == 0:
                    print '获取完毕'
                    break
                j = 0
                for ouzhiDataChild in ouzhiData1:
                    print "------------------------%s------------------------" % (i * 30 + j)
                    print ouzhiDataChild['id']
                    print ouzhiDataChild.contents[3].a.span.string
                    webjson = openUrls.getWebContentJson(ConfigStart.ANALYSISDAXIAODATAURL % (
                        fid, ouzhiDataChild['id']))
                    webjson = json.loads(webjson)
                    print webjson
                    for webjsonChild in webjson:
                        soupChild = BeautifulSoup(webjsonChild, "html.parser")
                        print webjsonChild[0]
                        # 开始写入数据到库中 TODO:
                    j += 1
                    pass
                i += 1
            pass
            '''
                ===========================大小指数结束===============比分指数开始==================================
            '''
            # url = ConfigStart.ANALYSISBIFEN % (535904)
            # openUrls = OpenUrls()
            # webcontext = openUrls.getWebContent(url, 0)
            # soup = BeautifulSoup(webcontext, "html.parser")
            # ouzhiData1 = soup.find_all('tr',class_=re.compile('tr'))
            # if ouzhiData1.__len__() == 0:
            #     print '获取完毕'
            #     pass
            # for ouzhiDataChild in  ouzhiData1:
            #     tdChilds = ouzhiDataChild.find_all('td')
            #     for tdChild in tdChilds:
            #         if tdChild.attrs.__len__() !=0:
            #             if tdChild.attrs['class'][0] == 'td_one':
            #                 continue
            #                 pass
            #             if tdChild.attrs['class'][0] =='tb_plgs':
            #                 continue
            #                 pass
            #         if tdChild.span.string == '主胜':
            #             continue
            #             pass
            #         pass
            #         for string in tdChild.stripped_strings :
            #             print string
            #             #TODO:添加到数据库中
            '''
                ===========================比分指数结束================技术统计开始==============================
            '''
            # url = ConfigStart.ANALYSISJISHU % (535904)
            # openUrls = OpenUrls()
            # webcontext = openUrls.getWebContent(url, 0)
            # soup = BeautifulSoup(webcontext, "html.parser")
            # ouzhiData1 = soup.find_all(class_=re.compile('team-statis'))
            # if ouzhiData1.__len__() == 0:
            #     print '获取完毕'
            #     pass
        pass
        pass
    pass
pass
if __name__ == '__main__':
    analysis = AnalysisData()
    analysis.getDataFromMatchInfo(2000)
    #analysis.selectRetCompanyId("立博")