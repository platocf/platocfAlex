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
    def selectRetCompanyId(self,name,mysql,fid):
        selectSql = "select p_id as result from company where company_name =BINARY%s "
        insertSql = "insert into company(company_name) values(%s)"
        try:
            resCount=mysql.getOne(selectSql,name)
            if(resCount==False):
                mysql.insertOne(insertSql,name)
                pass
            pass
            resCount = mysql.getOne(selectSql, name)
            resvalue = 0
            if resCount == False:
                print "company表的字段可能不够长"
                pass
            else:
                resvalue = resCount['result']
            return resvalue
        except Exception,e:
            file=open("6666.log",'wb+')
            file.write("%s==========错误的原因:%s--%s"%(e,fid,name))
            file.close()
            print "%s==========错误的原因:%s--%s"%(e,fid,name)
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
            fid = 445346#resultChild['fid']
            print fid
            deleteSqls = ["DELETE FROM yazhi WHERE matchinfoid=%s "," DELETE FROM oupei WHERE matchinfoid=%s "," DELETE FROM rangqiu WHERE matchinfoid=%s "," DELETE FROM daxiao WHERE matchinfoid=%s "," DELETE FROM befen WHERE matchinfoid=%s " ," DELETE FROM jinqiu WHERE matchinfoid=%s "," DELETE FROM dsjinqiu WHERE matchinfoid=%s "," DELETE FROM bqc WHERE matchinfoid=%s "," DELETE FROM teamstatistics WHERE matchinfoid=%s "," DELETE FROM playerstatistics WHERE matchinfoid=%s"]
            for deleteSqlsChild in deleteSqls:
                mysql.delete(deleteSqlsChild,fid)
                mysql.end()
            print "清理数据成功"
            i = 0
            '''
            =====================================欧赔开始================================================
            '''
            count_cursor = 0
            while False:
                if count_cursor!=i*30:
                    break
                url = ConfigStart.ANALYSISOUZHIURL % (fid,i * 30)
                print "=============================================%s==================================="%url
                openUrls = OpenUrls()
                webcontext = openUrls.getWebContent(url,mysql,i)
                if webcontext.find('500.com')==-1 and webcontext!='':
                    print "查看webcontext:%s"%webcontext
                    continue
                    pass
                else:
                    if webcontext =='':
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
                    companyId = self.selectRetCompanyId(companyName[0]['title'],mysql,fid)
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
                    mysql.end()
                    j += 1
                    pass
                i +=1
                pass
            '''
            ===========================欧赔结束===============让球指数开始==================================
            '''
            i=0
            count_cursor2=0
            while False:
                if count_cursor2!=i*30:
                    break
                url = ConfigStart.ANALYSISRANGQIU % (fid,i * 30)
                openUrls = OpenUrls()
                webcontext = openUrls.getWebContent(url,mysql,i)
                if webcontext.find('rangqiu')==-1 and webcontext!='':
                    print "查看——球指数——webcontext:%s"%webcontext
                    continue
                    pass
                else:
                    if webcontext =='':
                        break
                soup = BeautifulSoup(webcontext, "html.parser")
                ouzhiData1 = soup.find_all(ttl='zy')
                if ouzhiData1.__len__() == 0:
                    print '获取完毕'
                    break
                j = 0
                for ouzhiDataChild in ouzhiData1:
                    print "------------------------%s------------------------" % (i * 30 + j+1)
                    count_cursor2=i * 30 + j+1
                    print ouzhiDataChild['cid']
                    print ouzhiDataChild.contents[3]['title']
                    companyId = self.selectRetCompanyId(ouzhiDataChild.contents[3]['title'], mysql,fid)
                    insertSql = "INSERT INTO `rangqiu` (`matchinfoid`,`rangqiucount`,`companyid`, `rq_s`, `rq_p`, `rq_f`, `ret`,`update_time`) VALUES  "
                    insertContext = []
                    webjson = 0
                    while True:
                        try:
                            webjson = openUrls.useProxy(ConfigStart.ANALYSISRANGQIUDATAURL % (fid, ouzhiDataChild['cid'], ouzhiDataChild.contents[5].string),mysql, 1)
                            webjson = json.loads(webjson)
                            break
                            pass
                        except Exception, e:
                            continue
                            pass
                        pass
                    pass
                    print webjson
                    index=0
                    for webjsonChild in webjson:
                        print webjsonChild[0]
                        #开始写入数据到库中 TODO:
                        if index == 0:
                            insertSql += "(%s, %s, %s, %s, %s, %s, %s, %s)"
                            index += 1
                            pass
                        else:
                            insertSql += ",(%s, %s, %s, %s, %s, %s, %s, %s)"
                            pass
                        insertContext.append(fid)
                        insertContext.append(ouzhiDataChild['handicapline'])
                        insertContext.append(companyId)
                        insertContext.append(webjsonChild[0])
                        insertContext.append(webjsonChild[1])
                        insertContext.append(webjsonChild[2])
                        insertContext.append(webjsonChild[3])
                        insertContext.append(webjsonChild[4])
                        pass
                    pass
                    mysql.update(insertSql, insertContext)
                    mysql.end()
                    j += 1
                    pass
                i += 1
            pass
            '''
                        ===========================让球指数结束===============亚盘开始==================================
            '''
            i = 0
            getyear=''
            count_cursor3=0
            while False:
                if count_cursor3!=i*30:
                    break
                url = ConfigStart.ANALYSISYAZHI % (fid, i * 30)
                openUrls = OpenUrls()
                webcontext = openUrls.getWebContent(url,mysql,i)
                soup = BeautifulSoup(webcontext, "html.parser")
                if i==0:
                    getyear=re.sub("\D", "", soup.find_all(class_='game_time')[0].string.split('-')[0])
                ouzhiData1 = soup.find_all(xls='row')
                if ouzhiData1.__len__() == 0:
                    print '获取完毕'
                    break
                j = 0
                for ouzhiDataChild in ouzhiData1:
                    print "------------------------%s------------------------" % (i * 30 + j+1)
                    count_cursor3 = i * 30 + j + 1
                    print ouzhiDataChild['id']
                    print ouzhiDataChild.contents[3].a.span.string
                    webjson = 0
                    while True:
                        try:
                            webjson = openUrls.useProxy(ConfigStart.ANALYSISYAZHIDATAURL % (
                                fid, ouzhiDataChild['id']), mysql, 1)
                            webjson = json.loads(webjson)
                            break
                            pass
                        except Exception, e:
                            continue
                            pass
                        pass
                    pass
                    #soupChild = BeautifulSoup(webjson, "html.parser")
                    print webjson
                    companyId = self.selectRetCompanyId(ouzhiDataChild.contents[3].a.span.string, mysql,fid)
                    insertSql = "INSERT INTO `yazhi` (`matchinfoid`,`companyid`, `left`, `handline`, `right`, `update_time`) VALUES  "
                    insertContext = []
                    index=0
                    for webjsonChild in webjson:
                        # 开始写入数据到库中 TODO:
                        if index == 0:
                            insertSql += "(%s, %s, %s, %s, %s, %s)"
                            index += 1
                            pass
                        else:
                            insertSql += ",(%s, %s, %s, %s, %s, %s)"
                            pass
                        tdWebjsonChild = BeautifulSoup(webjsonChild, "html.parser").find_all('td')
                        insertContext.append(fid)
                        insertContext.append(companyId)
                        insertContext.append(tdWebjsonChild[0].string)
                        for _char in tdWebjsonChild[1].stripped_strings:
                            print _char
                            insertContext.append(_char)
                            break
                        insertContext.append(tdWebjsonChild[2].string)
                        try:
                            if(i!=0):
                                print i
                            insertContext.append("%s-%s"%(getyear,tdWebjsonChild[3].string))
                        except Exception,e:
                            file = open('6666.log','wb+')
                            file.write("%s-%s-%s"%(fid,tdWebjsonChild[3].string,e))
                            file.close()
                    mysql.update(insertSql, insertContext)
                    mysql.end()
                    j += 1
                    pass
                i += 1
            pass
            '''
                ===========================亚盘结束===============大小指数开始==================================
            '''
            i = 0
            getyear=''
            count_cursor4=0
            while False:
                if count_cursor4!=i*30:
                    break
                url = ConfigStart.ANALYSISDAXIAO % (fid, i * 30)
                openUrls = OpenUrls()
                webcontext = openUrls.getWebContent(url,mysql,i)
                soup = BeautifulSoup(webcontext, "html.parser")
                if i==0:
                    getyear=re.sub("\D", "", soup.find_all(class_='game_time')[0].string.split('-')[0])
                ouzhiData1 = soup.find_all(xls='row')
                if ouzhiData1.__len__() == 0:
                    print '获取完毕'
                    break
                j = 0
                for ouzhiDataChild in ouzhiData1:
                    print "------------------------%s------------------------" % (i * 30 + j+1)
                    count_cursor4=i * 30 + j+1
                    print ouzhiDataChild['id']
                    print ouzhiDataChild.contents[3].a.span.string
                    webjson = 0
                    while True:
                        try:
                            webjson = openUrls.useProxy(ConfigStart.ANALYSISDAXIAODATAURL % (
                                fid, ouzhiDataChild['id']), mysql, 1)
                            webjson = json.loads(webjson)
                            break
                            pass
                        except Exception, e:
                            continue
                            pass
                        pass
                    pass
                    print webjson
                    if webjson==None:
                        continue
                    companyId = self.selectRetCompanyId(ouzhiDataChild.contents[3].a.span.string, mysql,fid)
                    insertSql = "INSERT INTO `daxiao` (`matchinfoid`,`companyid`, `left`, `handline`, `right`, `update_time`) VALUES  "
                    insertContext = []
                    index=0
                    for webjsonChild in webjson:
                        # 开始写入数据到库中 TODO:
                        if index == 0:
                            insertSql += "(%s, %s, %s, %s, %s, %s)"
                            index += 1
                            pass
                        else:
                            insertSql += ",(%s, %s, %s, %s, %s, %s)"
                            pass
                        tdWebjsonChild = BeautifulSoup(webjsonChild, "html.parser").find_all('td')
                        insertContext.append(fid)
                        insertContext.append(companyId)
                        insertContext.append(tdWebjsonChild[0].string)
                        for _char in tdWebjsonChild[1].stripped_strings:
                            print _char
                            insertContext.append(_char)
                            break
                        insertContext.append(tdWebjsonChild[2].string)
                        insertContext.append("%s-%s" % (
                            getyear,
                        tdWebjsonChild[3].string))
                    mysql.update(insertSql, insertContext)
                    mysql.end()
                    j += 1
                    pass
                i += 1
            pass
            '''
                ===========================大小指数结束===============比分指数开始==================================
            '''
            while False:
                url = ConfigStart.ANALYSISBIFEN % (fid)
                openUrls = OpenUrls()
                #INSERT INTO `befen` (`matchinfoid`, `companyid`, `e_1_0h`, `e_1_0g`, `e_2_0h`, `e_2_0g`, `e_2_1h`, `e_2_1g`, `e_3_0h`, `e_3_0g`, `e_3_1h`, `e_3_1g`, `e_3_2h`, `e_3_2g`, `e_4_0h`, `e_4_0g`, `e_4_1h`, `e_4_1g`, `e_4_2h`, `e_4_2g`, `e_4_3h`, `e_4_3g`, `e_0_0`, `e_1_1`, `e_2_2`, `e_3_3`, `e_4_4`) VALUES ('1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1')
                webcontext = openUrls.getWebContent(url,mysql,0)
                soup = BeautifulSoup(webcontext, "html.parser")
                ouzhiData1 = soup.find_all('tr',class_=re.compile('tr'))
                if ouzhiData1.__len__() == 0:
                    print '获取完毕'
                    break
                    pass
                insertSql = "INSERT INTO `befen` (`matchinfoid`, `companyid`, `e_1_0h`, `e_1_0g`, `e_2_0h`, `e_2_0g`, `e_2_1h`, `e_2_1g`, `e_3_0h`, `e_3_0g`, `e_3_1h`, `e_3_1g`, `e_3_2h`, `e_3_2g`, `e_4_0h`, `e_4_0g`, `e_4_1h`, `e_4_1g`, `e_4_2h`, `e_4_2g`, `e_4_3h`, `e_4_3g`, `e_0_0`, `e_1_1`, `e_2_2`, `e_3_3`, `e_4_4`) VALUES "
                insertContext = []
                index=0
                for ouzhiDataChild in  ouzhiData1:
                    if index==0:
                        insertSql += "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        index+=1
                    else:
                        insertSql += ",(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    insertContext.append(fid)
                    companyId = self.selectRetCompanyId(ouzhiDataChild.a.string, mysql,fid)
                    insertContext.append(companyId)
                    tdChilds = ouzhiDataChild.find_all('td')
                    for tdChild in tdChilds:
                        if tdChild.attrs.__len__() !=0:
                            if tdChild.attrs['class'][0] == 'td_one':
                                continue
                                pass
                            if tdChild.attrs['class'][0] =='tb_plgs':
                                continue
                                pass
                        if type(None)!=type(tdChild.span):
                            if tdChild.span.string == '主胜':
                                continue
                                pass
                            pass
                        appendIndex = 0
                        for string in tdChild.strings:
                            print string
                            if string.strip() == '':
                                string = None
                            insertContext.append(string)
                            appendIndex += 1
                            pass
                        if (appendIndex == 0):
                            insertContext.append(None)
                    pass
                    print insertContext
                            #TODO:添加到数据库中
                mysql.update(insertSql, insertContext)
                mysql.end()
                break
            '''
                ===========================比分指数结束================进球指数对比开始==============================
            '''
            #http://odds.500.com/fenxi/jqs-607180.shtml
            while False:
                url = ConfigStart.ANALYSISJINQIUZHISHU % (fid)
                openUrls = OpenUrls()
                # INSERT INTO `befen` (`matchinfoid`, `companyid`, `e_1_0h`, `e_1_0g`, `e_2_0h`, `e_2_0g`, `e_2_1h`, `e_2_1g`, `e_3_0h`, `e_3_0g`, `e_3_1h`, `e_3_1g`, `e_3_2h`, `e_3_2g`, `e_4_0h`, `e_4_0g`, `e_4_1h`, `e_4_1g`, `e_4_2h`, `e_4_2g`, `e_4_3h`, `e_4_3g`, `e_0_0`, `e_1_1`, `e_2_2`, `e_3_3`, `e_4_4`) VALUES ('1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1')
                webcontext = openUrls.getWebContent(url, mysql, 0)
                soup = BeautifulSoup(webcontext, "html.parser")
                ouzhiData1 = soup.find_all('tr', class_=re.compile('tr'))
                if ouzhiData1.__len__() == 0:
                    print '获取完毕'
                    break
                    pass
                insertSql = "INSERT INTO `jinqiu` (`matchinfoid`,`companyid`,`e_0`, `e_1`, `e_2`, `e_3`, `e_4`, `e_5`, `e_6`, `e_7plus`) VALUES "
                insertContext = []
                index = 0
                for ouzhiDataChild in ouzhiData1:
                    if index == 0:
                        insertSql += "(%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
                        index += 1
                    else:
                        insertSql += ",(%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
                    insertContext.append(fid)
                    tdChilds = ouzhiDataChild.find_all('td')
                    for tdChild in tdChilds:
                        if tdChild.attrs.__len__() != 0:
                            if tdChild.attrs['class'][0] == 'td_one':
                                continue
                                pass
                            if tdChild.attrs['class'][0] == 'tb_plgs':
                                for string in tdChild.strings:
                                    companyId = self.selectRetCompanyId(string, mysql,fid)
                                    insertContext.append(companyId)
                                    break
                                continue
                                pass
                        if type(None) != type(tdChild.span):
                            if tdChild.span.string == '主胜':
                                continue
                                pass
                            pass
                        appendIndex = 0
                        for string in tdChild.strings:
                            print string
                            if string.strip() == '':
                                string = None
                            insertContext.append(string)
                            appendIndex += 1
                            break
                            pass
                        if (appendIndex == 0):
                            insertContext.append(None)
                    pass
                    print insertContext
                    # TODO:添加到数据库中
                mysql.update(insertSql, insertContext)
                mysql.end()
                break
            pass

            '''
                ===========================进球指数对比结束================单双进球指数对比开始==============================
            '''
            # http://odds.500.com/fenxi/ds-607180.shtml
            while False:
                url = ConfigStart.ANALYSISDANSHUANGJINQIUZHISHU % (fid)
                openUrls = OpenUrls()
                # INSERT INTO `dsjinqiu` (`matchinfoid`, `companyid`, `single`, `double`, `ret`, `e01`, `e23`, `e47`, `e7plus`) VALUES ('1', '1', '1', '1', '1', '1', '1', '1', '1')
                webcontext = openUrls.getWebContent(url, mysql, 0)
                soup = BeautifulSoup(webcontext, "html.parser")
                ouzhiData1 = soup.find_all('tr', class_=re.compile('tr'))
                if ouzhiData1.__len__() == 0:
                    print '获取完毕'
                    break
                    pass
                insertSql = "INSERT INTO `dsjinqiu` (`matchinfoid`, `companyid`, `single`, `double`,`singlepro`,`doublepro`, `ret`, `e01`, `e23`, `e47`, `e7plus`) VALUES "
                insertContext = []
                index = 0
                for ouzhiDataChild in ouzhiData1:
                    if index == 0:
                        insertSql += "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        index += 1
                    else:
                        insertSql += ",(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    insertContext.append(fid)
                    tdChilds = ouzhiDataChild.find_all('td')
                    for tdChild in tdChilds:
                        if tdChild.attrs.__len__() != 0:
                            if tdChild.attrs['class'][0] == 'td_one':
                                continue
                                pass
                            if tdChild.attrs['class'][0] == 'tb_plgs':
                                for string in tdChild.strings:
                                    companyId = self.selectRetCompanyId(string, mysql,fid)
                                    insertContext.append(companyId)
                                    break
                                continue
                                pass
                        if type(None) != type(tdChild.span):
                            if tdChild.span.string == '主胜':
                                continue
                                pass
                            pass
                        appendIndex=0
                        for string in tdChild.strings:
                            print string
                            if string.find('%')!=-1:
                                string=string.split('%')[0]
                            if string.strip()=='':
                                string=None
                            insertContext.append(string)
                            appendIndex +=1
                            break
                            pass
                        if(appendIndex==0):
                            insertContext.append(None)
                    pass
                    print insertContext
                    # TODO:添加到数据库中
                mysql.update(insertSql, insertContext)
                mysql.end()
                break
            pass
            '''
                ===========================单双进球指数对比结束================半全场指数对比开始==============================
            '''
            # http://odds.500.com/fenxi/bqc-565613.shtml
            while False:
                url = ConfigStart.ANALYSISBQCZHISHU % (fid)
                openUrls = OpenUrls()
                # INSERT INTO `bqc` (`matchinfoid`, `companyid`, `e11`, `e10`, `e1-1`, `e01`, `e00`, `e0-1`, `e-11`, `e-10`, `e-1-1`) VALUES ('1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1')
                webcontext = openUrls.getWebContent(url, mysql, 0)
                soup = BeautifulSoup(webcontext, "html.parser")
                ouzhiData1 = soup.find_all('tr', class_=re.compile('tr'))
                if ouzhiData1.__len__() == 0:
                    print '获取完毕'
                    break
                    pass
                insertSql = "INSERT INTO `bqc` (`matchinfoid`, `companyid`, `e11`, `e10`, `e1-1`, `e01`, `e00`, `e0-1`, `e-11`, `e-10`, `e-1-1`) VALUES "
                insertContext = []
                index = 0
                for ouzhiDataChild in ouzhiData1:
                    if index == 0:
                        insertSql += "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        index += 1
                    else:
                        insertSql += ",(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    insertContext.append(fid)
                    tdChilds = ouzhiDataChild.find_all('td')
                    for tdChild in tdChilds:
                        if tdChild.attrs.__len__() != 0:
                            if tdChild.attrs['class'][0] == 'td_one':
                                continue
                                pass
                            if tdChild.attrs['class'][0] == 'tb_plgs':
                                for _name in tdChild.p.strings:
                                    companyId = self.selectRetCompanyId(_name, mysql,fid)
                                    insertContext.append(companyId)
                                    break
                                continue
                                pass
                        if type(None) != type(tdChild.span):
                            if tdChild.span.string == '主胜':
                                continue
                                pass
                            pass
                        appendIndex = 0
                        for string in tdChild.strings:
                            print string
                            if string.strip() == '':
                                string = None
                            insertContext.append(string)
                            appendIndex += 1
                            break
                            pass
                        if (appendIndex == 0):
                            insertContext.append(None)
                    pass
                    print insertContext
                    # TODO:添加到数据库中
                mysql.update(insertSql, insertContext)
                mysql.end()
                break
            pass
            '''
                ===========================半全场指数对比结束================数据统计开始==============================
            '''
            url = ConfigStart.ANALYSISJISHU % (fid)
            openUrls = OpenUrls()
            webcontext = openUrls.getWebContent(url,mysql,0)
            soup = BeautifulSoup(webcontext, "html.parser")
            ouzhiData1 = soup.find_all(class_=re.compile('team-statis'))
            if ouzhiData1.__len__() == 0:
                print '获取完毕'
                pass
            insertSql = "INSERT INTO `teamstatistics` (`matchinfoid`,`horg`, `static_attack`, `static_dattack`, `static_shoot`, `static_shootz`, `static_freekick`, `static_corner`, `static_offside`, `static_foul`, `static_yelcrad`, `static_redcrad`, `static_control`) VALUES "
            insertContext = []
            insertContext2 = []
            insertContext.append(fid)
            insertContext2.append(fid)
            insertContext.append('h')
            insertContext2.append('g')
            # for ouzhiDataChild in ouzhiData1:
            #     print ouzhiDataChild
            iLoop=0
            insertSql2=insertSql
            index=0
            insertSql += "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insertSql2 += "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            allDataArray=ouzhiData1[0].find_all('td')
            while index*5+4<allDataArray.__len__():
                value1=allDataArray[index*5+2].string
                value2=allDataArray[index*5+4].string
                if value1.find('%') != -1:
                    value1 = value1.split('%')[0]
                if value2.find('%') != -1:
                    value2 = value2.split('%')[0]
                insertContext.append(value1)
                insertContext2.append(value2)
                index += 1
                pass
            # mysql.update(insertSql, insertContext)
            # mysql.end()
            # mysql.update(insertSql, insertContext2)
            # mysql.end()
            '''
            球员信息
            '''
            playerInfo=soup.find_all(class_='player-box')
            isHost=0
            for playerInfoChild in playerInfo:
                insertSql = "INSERT INTO `playerstatistics` (`matchinfoid`, `number`, `name_c`, `position`, `type`, `time`, `goal`, `assists`, `shoot`, `shootz`, `pass`, `steals`, `foul`, `befoul`, `offside`, `rescue`, `yelcrad`, `redcrad`, `saves`,`horg`) VALUES "
                insertContext = []
                singleInfo =playerInfoChild.find_all('tr')
                index=0
                for singleInfoChild in singleInfo:
                    singletdInfo=singleInfoChild.find_all('td')
                    if singletdInfo.__len__()==0:
                        continue
                    if index == 0:
                        insertSql += "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        index += 1
                    else:
                        insertSql += ",(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    insertContext.append(fid)
                    for singletdInfoChild in singletdInfo:
                        print singletdInfoChild.string
                        insertContext.append(singletdInfoChild.string)
                    if(isHost==0):
                        insertContext.append('h')
                    else:insertContext.append('g')
                    pass
                #print insertSql
                if (index != 0):
                    mysql.update(insertSql, insertContext)
                    mysql.end()
            '''
                ==========================数据统计结束==============================
            '''
            # 设置use已经抓取标志
            useSql = "update matchinfo set used=1 where fid = %s"
            mysql.update(useSql, fid)
            mysql.end()
            print "matchurl更新成功"
        pass
        mysql.dispose()
        pass
    pass
pass
if __name__ == '__main__':
    analysis = AnalysisData()
    analysis.getDataFromMatchInfo(2000)
    #analysis.selectRetCompanyId("立博")