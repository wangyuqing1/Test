from scrapy.http.request import Request
import pymssql
import datetime
from urllib.parse import unquote
import re


class pink_DB(object):
    def __init__(self):
        self.conn = pymssql.connect(host='39.107.232.213',user='yishan',password='!QAZxsw2',database='YISHAN_Collection')
        self.cur = self.conn.cursor()

    def insert(self,values):
        try:
            # sql = """insert into urlsss(url) values('{}')""".format(values)
            self.cur.execute(values)
            self.conn.commit()
        except:

            self.conn.rollback()

    def select(self,values):
        # sql = """select url from urlsss where url='{}'""".format(values)

        self.cur.execute(values)
        urls = self.cur.fetchone()
        if urls:
            # print("我进来了")
            # print(urls)
            return True
        return False
    # def select_time(self,sql):
    #     self.cur.execute(sql)
    #     time = self.cur.fetchone()
    #     if not time:
    #         return False
    #     else:
    #         return time[0]
    # def insert_time(self,time):
    #     try:
    #         sql = """insert into times(times) values('{}')""".format(time)
    #         self.cur.execute(sql)
    #         self.conn.commit()
    #     except:
    #         self.conn.rollback()

    def close(self):
        self.conn.close()
        # self.cur.close()
db = pink_DB()

class Website(object):
    #中国社会福利基金会
    def cswefs(self,url,i):
        #判断数据库有没有这个url
        sql = """select url from urls where url='{}'""".format(url)
        judge = db.select(sql)
        if judge:
            parr = re.compile('\d+.html')
            urls = re.search(parr, url).group()
            urls = urls.split('.')[0]
            while True:
                urls = int(urls) + 1
                o = 'http://www.cswef.cn/Home/Donquery/index/status/2/p/' + str(urls) + '.html'
                sql = """select url from urls where url='{}'""".format(o)
                data = db.select(sql)
                if not data:
                    sql = """insert into urls(url) values('{}')""".format(o)
                    db.insert(sql)

                    return Request(url=o)

        else:
            sql = """insert into urls(url) values('{}')""".format(url)
            db.insert(sql)
            return i

    #中国少年儿童慈善救助基金会
    def ccafc(self,url,i):
        #判断数据有没有这个url
        sql = """select url from urlsss where url='{}'""".format(url)
        judge = db.select(sql)
        if judge:
            part = re.compile('type=\S+')

            parr = re.compile('pagesize=\d+')
            urls = re.search(parr, url).group()
            urls = urls.split('=')[1]

            # 类型数据
            type_url = re.search(part, url).group()
            type = type_url.split("=")[1]
            type = type.split("&")[0]
            type = unquote(type, encoding='utf-8')
            while True:
                if type == '个人':
                    urls = int(urls) + 1
                    o = 'http://www.ccafc.org.cn/templates/DonationSearch/index.aspx?nodeid=106&name=&DonationNum=&MinAmount=&MaxAmount=&Payment=&starttime=2009-01-01&endtime=2019-03-13&Project=0&recipients=&type=%E4%B8%AA%E4%BA%BA&pagesize='+str(urls)+'&pagenum=20'


                    sql = """select url from urlsss where url='{}'""".format(o)
                    data = db.select(sql)
                    if not data:
                        sql = """insert into urlsss(url) values('{}')""".format(o)
                        db.insert(sql)

                        return Request(url=o)
                else:
                    urls = int(urls) + 1
                    o = 'http://www.ccafc.org.cn/templates/DonationSearch/index.aspx?nodeid=106&name=&DonationNum=&MinAmount=&MaxAmount=&Payment=&starttime=2009-01-01&endtime=2019-03-13&Project=0&recipients=&type=%E4%BC%81%E4%B8%9A&pagesize=' + str(
                        urls) + '&pagenum=20'

                    sql = """select url from urlsss where url='{}'""".format(o)
                    data = db.select(sql)
                    if not data:
                        sql = """insert into urlsss(url) values('{}')""".format(o)
                        db.insert(sql)
                        return Request(url=o)
        else:
            sql = """insert into urlsss(url) values('{}')""".format(url)
            db.insert(sql)
            return i



    #中国扶贫基金会
    # def cfpa(self,url,i):
    #     parr = re.compile('billdate=\d+-\d+-\d+')
    #     day_url = re.search(parr, url).group()
    #     day = day_url.split('=')[1]
    #     sql = """select times from times where times='{}'""".format(day)
    #
    #     days = db.select_time(sql)
    #     if days:
    #
    #         urls = 'http://www.cfpa.org.cn/information/donationlist.aspx?billdate=' + str(day) + '&page=1'
    #         pages = db.select(urls)
    #         if pages:
    #             parr = re.compile('page=\d+')
    #             page_url = re.search(parr, urls).group()
    #             page = page_url.split('=')[1]
    #             while True:
    #                 page = int(page) + 1
    #                 o = 'http://www.cfpa.org.cn/information/donationlist.aspx?billdate=' + str(
    #                     day) + '&page=' + str(page)
    #                 data = db.select(o)
    #                 # print("是在这个里面吗？？"*10)
    #                 # print(data)
    #                 if not data:
    #                     db.insert(o)
    #                     return Request(url=o)
    #         else:
    #             db.insert(urls)
    #             return Request(url=urls)
    #     else:
    #         print("那么你是不是第一次一直走的就是这个地方那  是的话就赶快给我打印出来号让我看到啊   不是的话你到是不走这里啊")
    #         db.insert_time(day)
    #         db.insert(i.url)
    #         return i

