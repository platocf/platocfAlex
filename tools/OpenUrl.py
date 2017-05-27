# -*- coding: utf-8 -*-
import urllib,urllib2
import gzip, StringIO
from MySqlDB.MySqlConn import Mysql
from Service.ShowCharType import *
import random
import cookielib
import time
import datetime
import os
import json
import ConfigStart
import sys
reload(sys)
sys.setdefaultencoding(ConfigStart.UTF8)
angenlist =['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60                                                                             ',
'Opera/8.0 (Windows NT 5.1; U; en)                                                                                                                                                                         ',
'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50                                                                                                                     ',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50                                                                                                                                         ',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0                                                                                                                                  ',
'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10                                                                                              ',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2                                                                                                ',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36                                                                                              ',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11                                                                                                  ',
'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16                                                                                  ',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36                                                                                             ',
'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko                                                                                                                                      ',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11                                                                               ',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER                                                                                      ',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)             ',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)"                                                                                                   ',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)                                                                                                               ',
'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0                                                                                    ',
'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)                                                                               ',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36                                                                          ',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36                                                                         ',
'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5                                                      ',
'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5                                                        ',
'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5                                                             ',
'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5                                                               ',
'Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1                                                       ',
'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1                                                                 ',
'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1                                        ',
'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10                                                                                                     ',
'Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13                                                                             ',
'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+                                                                            ',
'Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0                                                                   ',
'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124                                            ',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)                                                                                                           ',
'UCWEB7.0.2.37/28/999                                                                                                                                                                                      ',
'NOKIA5700/ UCWEB7.0.2.37/28/999                                                                                                                                                                           ',
'Openwave/ UCWEB7.0.2.37/28/999                                                                                                                                                                            ',
'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999']
#设置503错误打上标记默认15分钟以后解除使用 e.code
#设置502错误打上标记默认5分钟以后使用      e.code
#设置You need to purchase or upgrade your license标记10分钟以后使用
class OpenUrls():
    def __init__(self):
        pass
    pass
    def getWebContent(self,url,mysql,i,reduce):
        #每个连接当前使用次数
        perCountList=[]
        perIPPort=[]
        #print url
        webcontext=''
        while True:
            try:
                # #print time.time()
                # test1 = time.time()
                # #print "%.10f"%(random.random())
                # test2=str(test1).replace('.','')+str(random.randint(0,10))
                # test3=test1+4000
                # test3=str(test3).replace('.','')+str(random.randint(0,10))
                #cookie = cookielib.MozillaCookieJar()
                # 从文件中的读取cookie内容到变量
                # cookie.load(os.path.dirname(os.path.realpath(__file__))+'\\cookies.txt', ignore_discard=True, ignore_expires=True)
                # for item in cookie:
                #     #TODO:修改session值
                #     if item.name == 'sdc_userflag':
                #         item.value ="%s::%s::%s"%(test2,test3,random.randint(0,10))
                #     if item.name =='sdc_session':
                #         item.value=test2
                #     if item.name == 'motion_id':
                #         item.value=test2+("%.10f"%(random.random()))
                    ##print 'name:' + item.name + '-value:' + item.value
                #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
                request = urllib2.Request(url)
                #agentSingle = random.choice(angenlist)
                request.add_header("User-Agent",
                                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36" )
                request.add_header("Accept",
                                   "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
                request.add_header("Accept-Encoding", "gzip, deflate, sdch")
                #request.add_header("Upgrade-Insecure-Requests","1")
                #request.add_header("X-Requested-With","XMLHttpRequest")
                #webfile=opener.open(request)
                webfile = urllib2.urlopen(request).read()
                #webcontext = webfile.read()
                useCharset = chardet_detect_str_encoding(webfile)
                if useCharset==None or useCharset == '':
                    if i == 0:
                        useCharset = 'gbk'
                        pass
                    else:
                        useCharset = 'utf8'
                webfile = gzip.GzipFile(fileobj=StringIO.StringIO(webfile), mode="r")
                webfile = webfile.read().decode(useCharset)
                webcontext=webfile
                time.sleep(1)
                pass
                break
            except Exception, e:
                #print '%stry again....从本机切换到代理中.....'%e
                webcontext=self.useProxy(url,mysql,i,reduce)
                break

        pass
        ##print webcontext
        return webcontext
    pass
    def getWebContentJson(self,url):
        request = urllib2.Request(url)
        request.add_header("User-Agent",
                           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36")
        request.add_header("Accept", "application/json, text/javascript, */*")
        request.add_header("Accept-Encoding", "gzip, deflate, sdch")
        request.add_header("X-Requested-With","XMLHttpRequest")
        webfile = urllib2.urlopen(request)
        webcontext = webfile.read()
        webcontext = gzip.GzipFile(fileobj=StringIO.StringIO(webcontext), mode="r")
        webcontext = webcontext.read().decode('gbk')
        return webcontext
        pass

    pass
    #根据获取到的评分数去得到概率值，最终返回数据
    def getProxyIP(self,mysql):
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        resultIP = mysql.getAll(
            "SELECT *,(proxyip.accessible/proxyip.usecount) as score FROM proxyip WHERE DATE_ADD(proxyip.time,interval 15 minute)<%s AND proxyip.accessible/proxyip.usecount>0 order by (proxyip.accessible/proxyip.usecount) desc limit 0,100",
            now_time)
        #每个评分数精确三位小数
        sumCount =0
        for resultIPChild in  resultIP:
            sumCount += int(resultIPChild['score']*10000)
            pass
        pass
        curIndex = random.randint(0, sumCount - 1)
        #可用inner join去累计数据
        resCount=0
        result =0
        for resultIPChild in  resultIP:
            resCount += int(resultIPChild['score']*10000)
            if resCount>=curIndex:
                result=resultIPChild
                break
                pass
            pass
        pass
        #print '=========================================================当前随机数为%s，返回的IP：%s================================================================='%(curIndex,resultIPChild['address_port'])
        return result
    pass
    # '211.159.220.48','808'      '84.244.7.32','8081'   '222.85.39.16','808'
    #reduce=0表示为返回需要json格式
    def useProxy(self,url,mysql,i,reduce=0):
        proxyIP=""
        webcontext=''
        #当前IP尝试次数
        tryIndex=0
        changeProxyCount=0
        while True:
            # 添加异常标志
            exceptFlag = 0
            resultIPChild = self.getProxyIP(mysql)
            proxyIP=resultIPChild['address_port']
            while True:
                try:
                    #更新代理使用次数

                    mysql.update('UPDATE proxyip SET `usecount`=`usecount`+1 where p_id=%s', resultIPChild['p_id'])
                    mysql.end()
                    cookies = urllib2.HTTPCookieProcessor()
                    proxyHandler = urllib2.ProxyHandler({"http": '%s' % (proxyIP)})
                    opener = urllib2.build_opener(cookies, proxyHandler)
                    agentSingle = random.choice(angenlist)
                    opener.addheaders = [('User-Agent',
                                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'),
                                         ("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"),("Accept-Encoding", "gzip, deflate, sdch"),("X-Requested-With","XMLHttpRequest")]
                    tryIndex +=1

                    req = opener.open(url,timeout=5)
                    webcontext = req.read()
                    useCharset=chardet_detect_str_encoding(webcontext)
                    if useCharset==None or useCharset=='':
                        if i==0:
                            useCharset='gbk'
                            pass
                        else:
                            useCharset='utf8'
                    ##print webcontext
                    #if(useCharset == 'GB2312' or useCharset == 'gb2312'):
                        #print useCharset
                    if(useCharset!='ascii'):
                        webcontext = gzip.GzipFile(fileobj=StringIO.StringIO(webcontext), mode="r")
                        webcontext = webcontext.read().decode(useCharset)
                        pass
                    else:
                        pass
                    #测试是否为json
                    if reduce==0:
                        json.loads(webcontext)
                        pass
                    pass
                    pass
                    ##print webcontext
                    mysql.update('UPDATE proxyip SET `accessible`=`accessible`+1 where p_id=%s', resultIPChild['p_id'])
                    mysql.end()
                    exceptFlag=0
                    break
                except Exception, e:
                    exceptFlag = 1
                    message ='%s'%e
                    now_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    if(message.find('503')!=-1 or message.find('500')!=-1 or message.find('501')!=-1):
                        #更新时间数据
                        updateSql_s = "UPDATE proxyip SET proxyip.time=%s where p_id=%s"
                        lList=[]
                        lList.append(now_time)
                        lList.append(resultIPChild['p_id'])
                        mysql.update(updateSql_s,lList)
                        #print "当前代理不可用，正在切换.....%s" % e
                        break
                    if tryIndex >=1:
                        tryIndex=0
                        #print "当前代理不可用，正在切换.....%s"%e
                        break
                        pass
                    else:
                        #print "当前继续尝试此链接,第%s次.....url:%s"%(tryIndex,url)
                        if i==0:
                            i=1
                            pass
                        else:
                            i=0
                            pass
                        continue
            if webcontext!='' and exceptFlag==0:
                #print type(webcontext) == str
                #print "返回%s"%webcontext
                break
                pass
            pass
            if type(webcontext) == gzip.GzipFile :
                if i == 0:
                    i = 1
                    pass
                else:
                    i = 0
                    pass
                pass
            pass
            changeProxyCount +=1
            #print "当前代理不可用，正在第%s次切换.....url:%s"%(changeProxyCount,url)
        # if(changeProxyCount>=(resultIP.__len__() -1)):
        #     self.useProxy(url,mysql,i)
        return webcontext
    pass

    def saveCookie(self):
        # 设置保存cookie的文件
        filename = 'cookie.txt'
        # 声明一个MozillaCookieJar对象来保存cookie，之后写入文件
        cookie = cookielib.MozillaCookieJar(filename)
        # 创建cookie处理器
        handler = urllib2.HTTPCookieProcessor(cookie)
        # 构建opener
        opener = urllib2.build_opener(handler)
        # 创建请求
        res = opener.open('http://odds.500.com/fenxi/ouzhi-607189.shtml')
        # 保存cookie到文件
        # ignore_discard的意思是即使cookies将被丢弃也将它保存下来
        # ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入
        cookie.save(ignore_discard=True, ignore_expires=True)
if __name__ == '__main__':
    #mysql =Mysql()
    openUrl = OpenUrls()
    #openUrl.saveCookie()
    #openUrl.getWebContent("http://192.168.9.33/Smartbj/index.html",1)
    openUrl.useProxy("http://odds.500.com/fenxi1/json/ouzhi.php?_=1493729244144&fid=449834&cid=513&r=1&type=europe",0)