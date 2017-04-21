# -*- coding: utf-8 -*-
import threadPoolBase
def hello(m, n, o):
    print "m = %s, n = %s, o = %s \r\n" % (m, n, o)
if __name__ == '__main__':
    lst_vars_1 = ['1', '2', '3']
    lst_vars_2 = ['4', '5', '6']
    func_var = [(lst_vars_1, None), (lst_vars_2, None)]

    dict_vars_1 = {'m': '1', 'n': '2', 'o': '3'}
    dict_vars_2 = {'m': '4', 'n': '5', 'o': '6'}
    func_var = [(None, dict_vars_1), (None, dict_vars_2)]
    pool = threadPoolBase.ThreadPool(2)

    requests = threadPoolBase.makeRequests(hello, func_var)
    [pool.putRequest(req) for req in requests]
    pool.wait()