# coding:utf-8
''''
主程序启动开始
1.先加载配置文件

'''
from Service.MainToSecond import *
from Service.LeagueMain import *
from Service.SecondToJifen import *
from Service.JifenToMatchUrl import *
from Service.AnalysisDataAll import *
from MySqlDB.MySqlConn import Mysql
import threading
import threadPoolBase
import ConfigStart
mutex = threading.Lock()
if __name__ == ConfigStart.MAIN:
    mysql = Mysql()
    pool = threadPoolBase.ThreadPool(ConfigStart.THREADCOUNT)
    if(MainToSecond.getSecondUrl() ==ConfigStart.TRUE):
        # leagueMain=LeagueMain()
        # while leagueMain.getWaitCrawler()>ConfigStart.NULL:
        #     func_var = []
        #     for i in  range(ConfigStart.THREADCOUNT):
        #         #只使用一个数据库连接时会出现mysql崩溃
        #         func_var.append(([mutex],None))
        #         pass
        #     requests = threadPoolBase.makeRequests(leagueMain.startLeagueMain, func_var)
        #     [pool.putRequest(req) for req in requests]
        #     pool.wait()
        #     pass
        #
        # sqlAll = ConfigStart.LEAGUEYEARINFO_COUNT
        # resultSelect = mysql.getOne(sqlAll)
        # threadCount = int(resultSelect[ConfigStart.RESULT]) / ConfigStart.THREADCOUNT + 1
        # secondToJifen = SecondToJifen()
        # func_var = []
        # for i in range(threadCount):
        #     func_var.append(([i * ConfigStart.THREADCOUNT], None))
        #     pass
        # requests = threadPoolBase.makeRequests(secondToJifen.getJifen, func_var)
        # [pool.putRequest(req) for req in requests]
        # pool.wait()
        # jifenToMatchUrl=JifenToMatchUrl()
        # requests=threadPoolBase.makeRequests(jifenToMatchUrl.getMatchUrl, func_var)
        # [pool.putRequest(req) for req in requests]
        # pool.wait()
        #
        # sqlAll = ConfigStart.MATCHURL_COUNT
        # resultSelect = mysql.getOne(sqlAll)
        # threadCount = int(resultSelect[ConfigStart.RESULT]) / ConfigStart.THREADCOUNT + 1
        # secondToJifen = SecondToJifen()
        # func_var = []
        # for i in range(threadCount):
        #     func_var.append(([i * ConfigStart.THREADCOUNT], None))
        #     pass
        # requests = threadPoolBase.makeRequests(jifenToMatchUrl.getMatchInfo, func_var)
        # [pool.putRequest(req) for req in requests]
        # pool.wait()
        # mysql.dispose()
        #判断已经获取到哪里
        try:
            analysisData = AnalysisData()
            sqlAll = ConfigStart.SELECTFROMMATCHINFO
            resultSelect = mysql.getOne(sqlAll)
            threadCount = int(resultSelect[ConfigStart.RESULT]) / ConfigStart.THREADCOUNT + 1
            secondToJifen = SecondToJifen()
            func_var = []
            for i in range(threadCount):
                func_var.append(([i * ConfigStart.THREADCOUNT], None))
                pass
            requests = threadPoolBase.makeRequests(analysisData.getDataFromMatchInfo, func_var)
            [pool.putRequest(req) for req in requests]
            pool.wait()
            mysql.dispose()
            pass
        except Exception,e:
            file = open('main.log','wb+')
            file.write("%s\r\n"%e)
            file.close()


