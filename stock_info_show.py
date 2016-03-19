#!/usr/bin/env python
#--*--coding:utf8--*--

__author__ = 'cjm'
__version__ = '0.1'

import urllib2
import argparse

code = []

def get_stock_info(code):
    url = "http://hq.sinajs.cn/list=%s" % code
    response = urllib2.urlopen(url)
    javascriptInfo = response.read()
    pythonInfo = javascriptInfo[4:]
    exec(pythonInfo)
    company = "hq_str_" + code
    companyInfo = eval(company)
    companyInfo = companyInfo.split(",")
    return companyInfo

def print_info(index):
    print '-'*80
    companyInfo = get_stock_info(code[index])
    if index+1 == len(code):
        print 'now:',companyInfo[3],'\tkai:',companyInfo[1],'\tshou:',companyInfo[2]
        print 'rate:',format(float(companyInfo[3])/float(companyInfo[2])-1, '.2%'),'\thigh:',companyInfo[4],'\tlow:',companyInfo[5]
        print '-'*30
        print 'chu5:',companyInfo[29],'\t',companyInfo[28][:-2]
        print 'chu4:',companyInfo[27],'\t',companyInfo[26][:-2]
        print 'chu3:',companyInfo[25],'\t',companyInfo[24][:-2]
        print 'chu2:',companyInfo[23],'\t',companyInfo[22][:-2]
        print 'chu1:',companyInfo[21],'\t',companyInfo[20][:-2]
        print '-'*30
        print 'jin1:',companyInfo[11],'\t',companyInfo[10][:-2]
        print 'jin2:',companyInfo[13],'\t',companyInfo[12][:-2]
        print 'jin3:',companyInfo[15],'\t',companyInfo[14][:-2]
        print 'jin4:',companyInfo[17],'\t',companyInfo[16][:-2]
        print 'jin5:',companyInfo[19],'\t',companyInfo[18][:-2]
    else:
        companyInfo_r = get_stock_info(code[index+1])
        print 'now:',companyInfo[3],'\tkai:',companyInfo[1],'\tshou:',companyInfo[2],'\t|','now:',companyInfo_r[3],'\tkai:',companyInfo_r[1],'\tshou:',companyInfo_r[2]
        print 'rate:',format(float(companyInfo[3])/float(companyInfo[2])-1, '.2%'),'\thigh:',companyInfo[4],'\tlow:',companyInfo[5],'\t|','rate:',format(float(companyInfo_r[3])/float(companyInfo_r[2])-1, '.2%'),'\thigh:',companyInfo_r[4],'\tlow:',companyInfo_r[5]
        print '-'*30,'\t\t\t|','-'*30
        print 'chu5:',companyInfo[29],'\t',companyInfo[28][:-2],'\t\t\t\t|','chu5:',companyInfo_r[29],'\t',companyInfo_r[28][:-2]
        print 'chu4:',companyInfo[27],'\t',companyInfo[26][:-2],'\t\t\t\t|','chu4:',companyInfo_r[27],'\t',companyInfo_r[26][:-2]
        print 'chu3:',companyInfo[25],'\t',companyInfo[24][:-2],'\t\t\t\t|','chu3:',companyInfo_r[25],'\t',companyInfo_r[24][:-2]
        print 'chu2:',companyInfo[23],'\t',companyInfo[22][:-2],'\t\t\t\t|','chu2:',companyInfo_r[23],'\t',companyInfo_r[22][:-2]
        print 'chu1:',companyInfo[21],'\t',companyInfo[20][:-2],'\t\t\t\t|','chu1:',companyInfo_r[21],'\t',companyInfo_r[20][:-2]
        print '-'*30,'\t\t\t|','-'*30
        print 'jin1:',companyInfo[11],'\t',companyInfo[10][:-2],'\t\t\t\t|','jin1:',companyInfo_r[11],'\t',companyInfo_r[10][:-2]
        print 'jin2:',companyInfo[13],'\t',companyInfo[12][:-2],'\t\t\t\t|','jin2:',companyInfo_r[13],'\t',companyInfo_r[12][:-2]
        print 'jin3:',companyInfo[15],'\t',companyInfo[14][:-2],'\t\t\t\t|','jin3:',companyInfo_r[15],'\t',companyInfo_r[14][:-2]
        print 'jin4:',companyInfo[17],'\t',companyInfo[16][:-2],'\t\t\t\t|','jin4:',companyInfo_r[17],'\t',companyInfo_r[16][:-2]
        print 'jin5:',companyInfo[19],'\t',companyInfo[18][:-2],'\t\t\t\t|','jin5:',companyInfo_r[19],'\t',companyInfo_r[18][:-2]

if __name__ == "__main__":

    args_obj = argparse.ArgumentParser(description='show stock info')
    args_obj.add_argument('code', action='store', nargs='+', help='Add your favorite stock codes')
    args = args_obj.parse_args()
    code = args.code

    # 上证 深成
    shzs = get_stock_info('sh000001')
    print 'now:',shzs[3],'rate:',format(float(shzs[3])/float(shzs[2])-1, '.2%'),'\tkai:',shzs[1],'\tshou:',shzs[2]
    szzs = get_stock_info('sz399001')
    print 'now:',szzs[3],'rate:',format(float(szzs[3])/float(szzs[2])-1, '.2%'),'\tkai:',szzs[1],'\tshou:',szzs[2]
    # 自选
    for index in range(0,len(code),2):
        #print index
        print_info(index)