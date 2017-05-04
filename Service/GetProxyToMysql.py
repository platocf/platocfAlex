# -*- coding: utf-8 -*-
from MySqlDB.MySqlConn import Mysql
from bs4 import BeautifulSoup
import urllib2
import random
import time
import StringIO,gzip
class GetProxyToMysql():
    def __init__(self):
        pass
    pass
    def getData(self):
       # url ='http://www.kuaidaili.com/free/inha/%s/'
        mysql = Mysql()
        s=1
        while s<=50:
            url = 'http://www.kuaidaili.com/free/inha/%s/'%(s)
            insertSql = "insert into proxyip(address,port) values"
            request = urllib2.Request(url)
            request.add_header("User-Agent",
                               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s.%s Safari/537.36" % (
                               random.uniform(1, 1000), random.uniform(0, 8000)))
            request.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
            request.add_header("Accept-Encoding", "gzip, deflate, sdch")
            webfile = urllib2.urlopen(request)
            webcontext = webfile.read()
            webcontext = gzip.GzipFile(fileobj=StringIO.StringIO(webcontext), mode="r")
            webcontext = webcontext.read().decode('utf8')
            soup = BeautifulSoup(webcontext, "html.parser")
            resultTr=soup.find_all('tr')
            l=[]
            i=0
            for trChild in resultTr:
                print trChild
                res=trChild.find_all('td')
                if res.__len__()>0:
                    if i==0:
                        insertSql += '(%s,%s)'
                    else:
                        insertSql += ',(%s,%s)'
                    i +=1
                else:
                    continue
                l.append(res[0].string)
                l.append(res[1].string)
            print webcontext
            print mysql.update(insertSql,l)
            s +=1
            time.sleep(1)
            pass
    pass
    def check_proxy(self,protocol, pip):
        try:
            ip_check_url = 'http://www.500.com'
            proxy_handler = urllib2.ProxyHandler({protocol: pip})
            opener = urllib2.build_opener(proxy_handler)
            # opener.addheaders = [('User-agent', user_agent)] #这句加上以后无法正常检测，不知道是什么原因。
            urllib2.install_opener(opener)
            req = urllib2.Request(ip_check_url)
            time_start = time.time()
            conn = urllib2.urlopen(req)
            # conn = urllib2.urlopen(ip_check_url)
            time_end = time.time()
            detected_pip = conn.read()
            proxy_detected = True
        except urllib2.HTTPError, e:
            print "ERROR: Code ", e.code
            return False
        except Exception, detail:
            print "ERROR: ", detail
            return False

        return proxy_detected
pass
if __name__ == '__main__':
    getProxy = GetProxyToMysql()
    #getProxy.getData()
    protocol = "http"
    current_proxy = "115.213.161.105:808"
    print getProxy.check_proxy(protocol,current_proxy)