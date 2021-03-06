# coding:utf-8
'''
配置文件信息
'''
from BEANS.LeagueYearInfo import *
from BEANS.MatchUrl import *
from BEANS.League import *
from BEANS.MatchInfo import *
#主程序起始搜索url
STARTURL="http://liansai.500.com/"
#beautifulSoup的解析方式
PARSEMETHOD="html.parser"
#所有国家的各大联赛对应的class
ALLLEAGUECLASS_1="lallrace_main_list"
ALLLEAGUECLASS_2="clearfix"
#所有联赛的主页的url所在div为allraceMainWrap 当变动时可以在此修改
LEAGUESDIV="allraceMainWrap"
#所有杯赛的主页的url所在tag
CPUMATCHTAG="lrace_bei"
#获取div所含联赛内容的div索引
DIVTOPINDEX=0
#联赛<a href>内的id匹配字段
AHREFTOPID="link"
#通用的一些标签
HREF='href'
A='a'
#获取积分页正则过滤
COMPILEJIFEN="jifen-"
#积分过滤字符串
STRINGJIFEN="赛程积分榜"
STRINGTITLE='title'
#下拉列表的class
DROPLISTCLASS='ldrop_list'

'''
国际赛事
欧洲赛事
美洲赛事
亚洲赛事
非洲赛事
'''
#赛事分区
MATCHPARTION=['国际赛事','欧洲赛事','美洲赛事','亚洲赛事','非洲赛事']
#杯赛
CUPMATCH=['欧洲杯赛','美洲杯赛','亚洲杯赛','非洲杯赛']
#线程池数量及分线程mysql查询分页数据每页数据量
THREADCOUNT=1000
#查询总数命名
RESULT ='result'
#查询每个联赛各赛季数据  所有总数量 查询表leagueyearinfo
LEAGUEYEARINFO_COUNT= "select count(*) as "+RESULT+" from "+LeagueYearInfo.tablename+" "
#查询leagueyearinfo  limit
SELECTFROMLEAGUEYEARINFOLIMIT ="select * from "+LeagueYearInfo.tablename+" limit %s,10"
#插入一条数据到leagueyearinfo中
INSERTINTOLEAGUEYEARINFO ="insert into "+LeagueYearInfo.tablename+"("+LeagueYearInfo.p_leagueid+","\
                          +LeagueYearInfo.p_league_url+","+LeagueYearInfo.p_league_year+","+LeagueYearInfo.p_name+") values(%s,%s,%s,%s) "
#更新多条leagueyearinfo表数据
UPDATELEAGUEYEARINFO_TOP="INSERT INTO "+LeagueYearInfo.tablename+"("+LeagueYearInfo.p_id+","+LeagueYearInfo.p_jifen_url+") VALUES "
UPDATELEAGUEYEARINFO_BOTTOM=" ON DUPLICATE KEY UPDATE "+LeagueYearInfo.p_jifen_url+"=VALUES("+LeagueYearInfo.p_jifen_url+") "
#查询matchurl表的总数量
MATCHURL_COUNT ="select count(*) as "+RESULT+" from "+MatchUrl.tablename+" where p_use=0"
#插入matchurl
INSERTINTOMATCHURL_TOP ="INSERT INTO "+MatchUrl.tablename+"("+MatchUrl.p_leagueyearinfoid+","+MatchUrl.p_url+","+MatchUrl.p_property+") VALUES "
#插入一条数据到league表中
INSERTINTOLEAGUETABLE="insert into "+League.tablename+"("+League.p_name+","+League.p_type+\
                      ","+League.p_country+","+League.p_sport_type+","+League.p_main_url+") values(%s,%s,%s,%s,%s)"

#查询一条数据从league表中
SELECTCOUNTFROMLEAGUETABLE="select count(*) as "+RESULT+" from "+League.tablename+\
                           " where "+League.p_name+"=%s and "+League.p_type+"=%s and "+League.p_country+"=%s ;"
#查询数据从league表中条件为p_crawler=0
SELECTFROMLEAGUECRAWLER="select * from "+League.tablename+" where "+League.p_crawler+"=0"
#查询共有多少条数从league表中条件为p_crawler=0
SELECTCOUNTFROMLEAGUECRAWLER="select count(*) as "+RESULT+" from "+League.tablename+" where "+League.p_crawler+"=0"
#更新p_crawler从league表中
UPDATELEAGUESETCRAWLER="update "+League.tablename+" set "+League.p_crawler+"=1 where "+League.p_id+"=%s"
#查询matchinfo分页10 limit
SELECTFROMMATCHINFOLIMIT="select * from "+MatchInfo.tablename+" where used=0 limit %s,10"
#查询matchinfo不分页
SELECTFROMMATCHINFO="select count(*) as result from "+MatchInfo.tablename+" where used=0"

#int为整数零
NULL=0
TRUE=1
INC=1
FALSE=0
NULLSTRING=''
SPACESTRING=' '
#main值
MAIN='__main__'
'''
字符编码格式定义
'''
UTF8='utf-8'
GBK='gbk'
GB2312='gb2312'

'''
两球队的对战分析数据页
'''
#两队对战分析
ANALYSISDATAURL = "http://odds.500.com/fenxi/shuju-%s.shtml"
#两对欧指分析
ANALYSISOUZHIURL='http://odds.500.com/fenxi1/ouzhi.php?id=%s&ctype=1&start=%s&r=1&style=0&guojia=0&chupan=1'
#欧指各公司数据
ANALYSISOUZHIDATAURL='http://odds.500.com/fenxi1/json/ouzhi.php?_=1493729244144&fid=%s&cid=%s&r=1&type=europe'
#欧指各公司凯利指数
ANALYSISOUZHIKELLYURL='http://odds.500.com/fenxi1/json/ouzhi.php?_=1493807219440&fid=%s&cid=%s&r=1&type=kelly'
#让球指数分析
ANALYSISRANGQIU='http://odds.500.com/fenxi1/rangqiu.php?id=%s&ctype=1&start=%s&r=1&style=0&guojia=0&chupan=1&lot=all'
#让球各公司指数
ANALYSISRANGQIUDATAURL='http://odds.500.com/fenxi1/json/rspf.php?_=1493773551248&fid=%s&cid=%s&r=1&handicapline=%s&type=rspf'
#亚盘对比
ANALYSISYAZHI='http://odds.500.com/fenxi1/yazhi.php?id=%s&ctype=1&start=%s&r=1&style=0&guojia=0'
#亚盘各公司分析
ANALYSISYAZHIDATAURL='http://odds.500.com/fenxi1/inc/yazhiajax.php?fid=%s&id=%s&t=1493777167209&r=1'
#大小指数分析
ANALYSISDAXIAO='http://odds.500.com/fenxi1/daxiao.php?id=%s&ctype=1&start=%s&r=1&style=0&guojia=0'
#大小指数各公司分析
ANALYSISDAXIAODATAURL='http://odds.500.com/fenxi1/inc/daxiaoajax.php?fid=%s&id=%s&t=1493778774481'
#比分指数分析
ANALYSISBIFEN='http://odds.500.com/fenxi/bifen-%s.shtml'
#进球指数对比分析
ANALYSISJINQIUZHISHU='http://odds.500.com/fenxi/jqs-%s.shtml'
#单双进球指数对比分析
ANALYSISDANSHUANGJINQIUZHISHU='http://odds.500.com/fenxi/ds-%s.shtml'
#半全场进球指数对比分析
ANALYSISBQCZHISHU='http://odds.500.com/fenxi/bqc-%s.shtml'
#技术统计
ANALYSISJISHU='http://odds.500.com/fenxi/stat-%s.shtml'
if __name__ == '__main__':
    #testurl = ANALYSISDATAURL%(55)
    print ''



