# import pymssql
#
# conn = pymssql.connect(host='127.0.0.1',password='123456',user='sa',database='urls')
# coursor = conn.cursor()
# # sql = "insert into url(urls) values('{}')".format('http://www.cswef.cn/Home/Donquery/index/status/2/p/2.html')
# # coursor.execute(sql)
# # conn.commit()
# item = {}
# sql = """insert into data(DonationNumber,InvoiceNumber,
#                DonorName,DonationAmount,
#                DonationProject,PayMethod,
#                DonationType,DonationTime,
#                PayPlatform,DonorType,
#                Recipient,Note,
#                InstitutionName,InsertTime)
#                values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""" .format(
# 18602414,
#                     None,
#                     '华刚',
#                     '20.0元',
#                     '重症孤儿救助',
#                     '财付通',
#                     None,
#                     '2017-02-28 19:23:01',
#                     None,
#                     None,
#                     None,
#                     None,
#                     None,
#                     '2019-3-11'
#                     )
# coursor.execute(sql)
# conn.commit()
# sql = """select * from data """
# coursor.execute(sql)
# all = coursor.fetchall()
# for r in all:
#     print(r)
# print(all)
# #
# #
# # # list1 = [119,122,126,130,134,138,118,121,125,129,133,137,141,120,123,127,131,135,139,143,124,128,132,136,140,144,148,138,142,146,150,154,158,162,141,145,149,153,157,161,165,148,152,156,160,164,143,147,151,155,159,163]
# # # list1.sort()
# # # print(list1)
#
# # import hashlib
# item = {}
#
# # sql = """insert into data(DonationNumber,InvoiceNumber,
# #        DonorName,DonationAmount,
# #        DonationProject,PayMethod,
# #        DonationType,DonationTime,
# #        PayPlatform,DonorType,
# #        Recipient,Note,
# #        InstitutionName,InsertTime)
# #        values({},{},{},{},{},{},{},{},{},{},{},{},{},{})"""\
# #     .format(item['DonationNumber'],
# #         item['InvoiceNumber'],
# #         item['DonorName'],
# #         item['DonationAmount'],
# #         item['DonationProject'],
# #         item['PayMethod'],
# #         item['DonationType'],
# #         item['DonationTime'],
# #         item['PayPlatform'],
# #         item['DonorType'],
# #         item['Recipient'],
# #         item['Note'],
# #         item['InstitutionName'],
# #         item['InsertTime']
# # )
#
# import datetime
#
# print(datetime.datetime.now().strftime("%Y-%m-%d"))




# times = '2017-02-2819:21:43'
# list2 = list(times)
# list2.insert(10,' ')
#
# print(''.join(list2))

# a = '20.0元'
# print(a.split('元')[0])


# a = 'http://www.cswef.cn/Home/Donquery/index/status/2/p/1.html'
#
# l = a.split('/')
# print(l)












# judge = db.select(i.url)
#                 if judge:
#                     parr = re.compile('\d+.html')
#                     urls = re.search(parr, i.url).group()
#                     urls = urls.split('.')[0]
#                     while True:
#                         urls = int(urls) + 1
#                         o = 'http://www.cswef.cn/Home/Donquery/index/status/2/p/' + str(urls) + '.html'
#
#
#                         url = db.select(o)
#                         if not url:
#                             db.insert(o)
#                             yield Request(url=o)
#                             break
#
#                 else:
#                     db.insert(i.url)
#                     yield i




# class A(object):
#     # def __init__(self,a):
#     #     self.a = a
#     #     # if self.a == 1:
#     #     #     self.s(self.a)
#     #     self.s(self.a)
#     def s(self,a):
#         print(a)
#         print('ssssss')


# import re
# url = 'http://www.ccafc.org.cn/templates/DonationSearch/index.aspx?nodeid=106&name=&DonationNum=&MinAmount=&MaxAmount=&Payment=&starttime=2009-01-01&endtime=2019-03-06&Project=0&recipients=&type=0&pagesize=1&pagenum=20'
#
# parr = re.compile('pagesize=\d+')
# p = re.search(parr,url).group()
# s = p.split('=')[1]
# print(s)



# import re
# # a = '\xa0希望早日康复'
# list1 = ['\xa0fdsfsadf','','dfsafds','\xa0ddfsafsadfsdafdsafwqerqwe']
# parr = re.compile('\xa0')
# for a in list1:
#     if "\xa0" in a:
#         print(re.sub(parr,'',a))

# print(len("\xa0"))


# a = 'http://www.ccafc.org.cn/templates/DonationSearch/index.aspx?nodeid=106&name=&DonationNum=&MinAmount=&MaxAmount=&Payment=&starttime=2009-01-01&endtime=2019-03-13&Project=0&recipients=&type=%E4%B8%AA%E4%BA%BA&pagesize=2&pagenum=20'
# import re
# parr = re.compile('pagesize=\d+')
# print(re.search(parr,a).group())


# import pymssql
#
# conn = pymssql.connect(host='127.0.0.1',password='123456',database='urls',user='sa')
# cur = conn.cursor()
# sql = """select urls from url where id = (select max(id) from url)"""
# cur.execute(sql)
# print(cur.fetchone()[0])


# import difflib
# import jieba
#
#
# query_str = '中国工商银行'
# str_2 = '中国工商银行(北京分行)'
# str_3 = '中国农业银行'
# str_4 = '中国工农银行'



# import datetime
# old_day = datetime.datetime(2012,1,1)
# new_day = datetime.datetime.now()
# day = (new_day-old_day).days
#
# class A(object):
#     def a(self):
#         global day
#         day -= 1
#         tim=datetime.datetime.now()
#         tiem = (tim+datetime.timedelta(days=-day)).strftime("%Y-%m-%d")
#         print(tiem)
#
# for i in range(10):
#     A.a(A())




# import re
# #
# # url = 'http://www.cfpa.org.cn/information/donationlist.aspx?billdate=2019-02-01&page=2'
# #
# # parr = re.compile('page=\d+')
# # part = re.compile('billdate=\d+-\d+-\d+')
# # times = re.search(part,url).group()
# # pagrs = re.search(parr,url).group()
# # page = pagrs.split('=')[1]
# # time = times.split('=')[1]
# # print(page)
# # print(time)


# import pymssql
#
# conn = pymssql.connect(host='127.0.0.1',user='sa',password='123456',database='ccadc')
# cur = conn.cursor()
# # sql = """insert into times(times) values('2012-02-01')"""
# sql = """select max(times) from times"""
# cur.execute(sql)
# # if cur.fetchone():
# time = cur.fetchone()[0]
# if time:
#     print(time)
# conn.commit()



# import datetime
# tims='2019-03-13'
# tim = datetime.datetime.strptime(tims,'%Y-%m-%d')
# tiem = (tim+datetime.timedelta(days=-5)).strftime("%Y-%m-%d")
# print(tiem)
# print(tiem)

#
# import datetime
#
# old_day = datetime.datetime(2012,1,1)
# new_day = datetime.datetime.now()
# day = (new_day-old_day).days
# print(day)


# import datetime
#
# tim=datetime.datetime.now()
# iem = (tim+datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
# time = datetime.datetime.strptime(iem,'%Y-%m-%d')
# print((time+datetime.timedelta(days=1)).strftime("%Y-%m-%d"))


''' sql = """select max(times) from times"""
                # max_time = db.select_time(sql)
                # if max_time:
                #     time = datetime.datetime.strptime(max_time, '%Y-%m-%d')
                #     print("我这次走这里了"*10)
                #     time = (time + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
                #     db.insert(time)
                # else:
                #     times = datetime.datetime.strptime(tiem,'%Y-%m-%d')
                #     tim = (times+datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
                # db.insert(tim)'''


# import pymssql
# import datetime
# conn = pymssql.connect(host='127.0.0.1',password='123456',user='sa',database='ccadc')
# cur = conn.cursor()
#
# tim=datetime.datetime.now()
# day = 26
# tiem = (tim+datetime.timedelta(days=-day)).strftime("%Y-%m-%d")
# time = datetime.datetime.strptime(tiem,'%Y-%m-%d')
# tims = (time + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
# sql = """select times from times where times='2012-01-15'"""
#
# cur.execute(sql)
# print(cur.fetchone())
# import time
# time.sleep(20)


# import re
# a = 'http://www.cfpa.org.cn/information/donationlist.aspx?billdate=2012-01-17&page=44'
# parr = re.compile('page=\d+')
#
# b = re.search(parr,a).group()
# c = b.split('=')[1]
# c = int(c)
# c += 1
# print(c)
# o = re.sub('page=\d+','page={}'.format(c),a)
# print(o)




'''

 data = db.select(url)
            
            if data:
                print("就一次也没有走这里吗？？？？？？"*10)
                #获取当前url的天数
                # max_time = db.select_time("""select times from times where times='{}'""")
                # if max_time:
                #     print(max_time)
                #     page = 1
                #     max_time = datetime.datetime.strptime(max_time, '%Y-%m-%d')
                #     time = (max_time + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
                #     while True:
                #         sql = """select times from times where times='{}'""".format(time)
                #         data_time = db.select_time(sql)
                #         print(data_time)
                #         if data_time:
                #             time = (max_time + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
                #         else:
                #             break
                #     print(time)
                #     print('真的求求你了'*10)
                #     while True:
                # 
                #         o = "http://www.cfpa.org.cn/information/donationlist.aspx?billdate=" + str(time)+"&page=" + str(page)
                #         print(o)
                #         page += 1
                #         data = db.select(o)
                #         print(data)
                #         if not data:
                #             db.insert(o)
                #             return Request(url=o)
            else:
                page = 1
                while True:
                    o = 'http://www.cfpa.org.cn/information/donationlist.aspx?billdate=2012-01-01&page='+str(page)
                    page += 1
                    data = db.select(o)
                    print(data)
                    if not data:
                        print('没有走这里吗')
                        db.insert(o)
                        return Request(url=o)
'''




"""


# data = db.select(url)
#         if data:
#             sql = '''select max(times) from times'''
#             max_time = db.select_time(sql)
# 
#             if max_time:
#                 page = 1
#                 max_time = datetime.datetime.strptime(max_time,'%Y-%m-%d')
#                 time = (max_time + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
#                 print(time)
#                 while True:
#                     sql = '''select times from times where times='{}'''.format(time)
#                     data_time = db.select_time(sql)
#                     print(data_time)
#                     if data_time:
#                         time = (max_time + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
#                     else:
#                         break
#                 while True:
#                     o = "http://www.cfpa.org.cn/information/donationlist.aspx?billdate=" + str(time) + "&page=" + str(page)
#                     page += 1
#                     data = db.select(o)
#                     if not data:
#                         db.insert(o)
#                         return Request(url=o)
#             else:
#                 page = 1
#                 while True:
#                     o = 'http://www.cfpa.org.cn/information/donationlist.aspx?billdate=2012-01-01&page=' + str(page)
#                     page += 1
#                     data = db.select(o)
#                     if not data:
#                         db.insert(o)
#                         return Request(url=o)
#         else:
#             db.insert(url)
#             return i
# 
# 
# """

# day = 200
# class A():
#     def parse(self):
#         global day
#         day -= 1
#         print(day)
# a = A()
# a.parse()
# from urllib.parse import unquote
# a = 'http://www.ccafc.org.cn/templates/DonationSearch/index.aspx?nodeid=106&name=&DonationNum=&MinAmount=&MaxAmount=&Payment=&starttime=2009-01-01&endtime=2019-03-13&Project=0&recipients=&type=%E4%B8%AA%E4%BA%BA&pagesize=1&pagenum=20'
# res = unquote(a,encoding='utf-8')
# print(res)
# import pymssql
#
# conn = pymssql.connect(host='127.0.0.1',password='123456',database='ccadc',user='sa')
#
# cur = conn.cursor()
#
# sql = """select times from times where times='{}'""".format('2012-01-02')
# cur.execute(sql)
# print(cur.fetchone()[0])

# a = 'type=%E4%B8%AA%E4%BA%BA'
# import re
#
# parr = re.compile('type=\S+')
# res = re.search(parr,a).group()
# print(res)





# import pymssql
# conn = pymssql.connect(host='39.107.232.213',user='yishan',password='!QAZxsw2',database='YISHAN_Collection')
#
# cur = conn.cursor()
#
# sql = """select * from urlsss"""
#
# cur.execute(sql)
# print(cur.fetchone())


# def we():
#     a = "aaa"
#
# class A():
#     _a = '你好'
#     def stop(self):
#         return self._a
#
# a = A()
# b = a.stop()
# print(b)


# from scrapy import log
# import logging
#
# logging.basicConfig(filename='example.log', filemode='a', level=logging.DEBUG)
# logging.debug('This is debug')


# import logging
# from logging import handlers
#
# class Logger(object):
#     level_relations = {
#         'debug':logging.DEBUG,
#         'info':logging.INFO,
#         'warning':logging.WARNING,
#         'error':logging.ERROR,
#         'crit':logging.CRITICAL
#     }#日志级别关系映射
#
#     def __init__(self,filename,level='info',when='D',backCount=3,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
#         self.logger = logging.getLogger(filename)
#         format_str = logging.Formatter(fmt)#设置日志格式
#         self.logger.setLevel(self.level_relations.get(level))#设置日志级别
#         sh = logging.StreamHandler()#往屏幕上输出
#         sh.setFormatter(format_str) #设置屏幕上显示的格式
#         th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
#         th.setFormatter(format_str)#设置文件里写入的格式
#         self.logger.addHandler(sh) #把对象加到logger里
#         self.logger.addHandler(th)
# log = Logger(r'C:\spider\charitable',level='debug')
# log.logger.debug('debug')
# log.logger.info('info')
# log.logger.warning('警告')
# log.logger.error('报错')
# log.logger.critical('严重')
# Logger('error.log', level='error').logger.error('error')

# try:
#     a = 'fsddfs'
#     a += 1
# except Exception as e:
#     print(e)



#以后又需要的
# sql = """select DonationNumber from data where DonationNumber='{}'""".format(item['DonationNumber'])
# print(sql)
# self.cur.execute(sql)
# DonationNumber = self.cur.fetchone()
# if not DonationNumber:



# a = '9,0000'
# if ',' in a:
#     print(a.replace(',',''))


# import json
# import requests
#
# def sendmessage(message):
#     url = 'https://oapi.dingtalk.com/robot/send?access_token=ae03cc317ed7391e2f655cb7b27f84c1f2c7b1c96aaebfb52a71cf41532d6055'
#     headers = {
#         "Content-Type": "application/json ;charset=utf-8 "
#     }
#     message = message
#     String_textMsg = {
#         'msgtype':'text',
#         'text':{"content":message},
#         "at":{
#             'atMobiles':[
#                 '15237774366'
#             ],
#             'isAtAll':False
#         }
#     }
#     string_textmsg = json.dumps(String_textMsg)
#     res = requests.post(url,data=string_textmsg,headers=headers)


# import datetime
# a = datetime.datetime.now()
#
# a = a.strftime("%Y-%m-%d %H:%M:%S")
# print(a)

# import requests
#
# response = requests.get('http://www.baidu.com')
# print(response)


a = '3,0000'
a = a.replace(',','')
print(a)