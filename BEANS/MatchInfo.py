class MatchInfo():
    tablename='matchinfo'
    p_leagueid, fid, ghalfscore, gid, gname, gscore, gstanding, gsxname, \
    handline,hhalfscore, hid, hname, hscore, hstanding, hsxname, round, \
    status, stime='p_leagueid', 'fid', 'ghalfscore', 'gid', 'gname',\
                  'gscore', 'gstanding','gsxname', 'handline', 'hhalfscore',\
                  'hid', 'hname', 'hscore', 'hstanding', 'hsxname', 'round',\
                  'status', 'stime'
    def __init__(self):
        pass
    pass
if __name__ == '__main__':
    print MatchInfo.p_leagueid