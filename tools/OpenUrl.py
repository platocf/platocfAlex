# -*- coding: utf-8 -*-
import urllib,urllib2
import gzip, StringIO
class OpenUrls():
    def __init__(self):
        pass
    pass
    def getWebContent(self,url,i):
        request = urllib2.Request(url)
        request.add_header("User-Agent",
                           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36")
        request.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
        request.add_header("Accept-Encoding", "gzip, deflate, sdch")
        webfile = urllib2.urlopen(request)
        webcontext = webfile.read()
        webcontext = gzip.GzipFile(fileobj=StringIO.StringIO(webcontext), mode="r")
        if i == 0:
            webcontext = webcontext.read().decode('gbk')
        else:
            webcontext = webcontext.read().decode('utf8')
        pass
        return webcontext
