# coding:utf-8
'''
配置文件信息
'''
#主程序起始搜索url
STARTURL="http://liansai.500.com/"
#beautifulSoup的解析方式
PARSEMETHOD="html.parser"
#所有联赛的主页的url所在div为allraceMainWrap 当变动时可以在此修改
LEAGUESDIV="allraceMainWrap"
#所有杯赛的主页的url所在tag
CPUMATCHTAG="lrace_bei"
#获取div所含联赛内容的div索引
DIVTOPINDEX=0
#联赛<a href>内的id匹配字段
AHREFTOPID="link"
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
#线程池数量
THREADCOUNT=8