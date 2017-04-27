# coding:utf-8
''''
主程序启动开始
1.先加载配置文件

'''
from Service.MainToSecond import *
from Service.LeagueMain import *
from Service.SecondToJifen import *
from Service.JifenToMatchUrl import *
from MySqlDB.MySqlConn import Mysql
import threading
import threadPoolBase
import ConfigStart
mutex = threading.Lock()
if __name__ == '__main__':
    mysql = Mysql()
    pool = threadPoolBase.ThreadPool(ConfigStart.THREADCOUNT)
    if(MainToSecond.getSecondUrl() ==1):
        # leagueMain=LeagueMain()
        # while leagueMain.getWaitCrawler()>0:
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
        # sqlAll = "select count(*) as result from leagueyearinfo "
        # resultSelect = mysql.getOne(sqlAll)
        # threadCount = int(resultSelect['result']) / 10 + 1
        # secondToJifen = SecondToJifen()
        # func_var = []
        # for i in range(threadCount):
        #     func_var.append(([i * 10], None))
        #     pass
        # requests = threadPoolBase.makeRequests(secondToJifen.getJifen, func_var)
        # [pool.putRequest(req) for req in requests]
        # pool.wait()
        jifenToMatchUrl=JifenToMatchUrl()
        # requests=threadPoolBase.makeRequests(jifenToMatchUrl.getMatchUrl, func_var)
        # [pool.putRequest(req) for req in requests]
        # pool.wait()

        sqlAll = "select count(*) as result from matchurl "
        resultSelect = mysql.getOne(sqlAll)
        threadCount = int(resultSelect['result']) / 10 + 1
        secondToJifen = SecondToJifen()
        func_var = []
        for i in range(threadCount):
            func_var.append(([i * 10], None))
            pass
        requests = threadPoolBase.makeRequests(jifenToMatchUrl.getMatchInfo, func_var)
        [pool.putRequest(req) for req in requests]
        pool.wait()
        mysql.dispose()
        pass


