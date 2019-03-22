import pymssql
import re
from urllib.parse import unquote
import datetime
from scrapy.http.request import Request


class pink_DB(object):
    #打开数据库
    def __init__(self):
        self.conn = pymssql.connect(host='39.107.232.213',user='yishan',password='!QAZxsw2',database='YISHAN_Collection')
        self.cur = self.conn.cursor()

    # url插入数据库
    def insert(self,values):
        try:
            # sql = """insert into urlsss(url) values('{}')""".format(values)
            self.cur.execute(values)
            self.conn.commit()
        except:
            self.conn.rollback()

    # 判断数据库中有没有这个url
    def select(self,values):
        # sql = """select url from urlsss where url='{}'""".format(values)
        self.cur.execute(values)
        urls = self.cur.fetchone()
        if urls:
            return True
        return False

    #找出数据库中最大的时间
    def select_max(self, sql):
        self.cur.execute(sql)
        urls = self.cur.fetchone()

        if not urls:
            return False
        else:
            return urls[0]

    #判断数据库中有没有这一天的数据
    def select_time(self,sql):
        self.cur.execute(sql)
        time = self.cur.fetchone()
        if not time:
            return False
        else:
            return time[0]

    #在数据库中插入时间
    def insert_time(self,time):
        try:
            sql = """insert into times(times) values('{}')""".format(time)
            self.cur.execute(sql)
            self.conn.commit()
        except:

            self.conn.rollback()

    #关闭数据库
    def close(self):
        self.conn.close()
        self.cur.close()
db = pink_DB()



class Before_Reqest(object):

    #  中国社会福利基金会

    def cswef(self,url,r):
        #判断请求的url 是否存在数据库
        sql = """select url from urls where url='{}'""".format(url)
        data = db.select(sql)
        if data:
            #正则匹配出 分页数据
            parr = re.compile('\d+.html')
            urls = re.search(parr, url).group()
            urls = urls.split('.')[0]
            urls = 44559
            while True:
                urls = int(urls) + 1
                o = 'http://www.cswef.cn/Home/Donquery/index/status/2/p/' + str(urls) + '.html'
                sql = """select url from urls where url='{}'""".format(o)
                url = db.select(sql)
                if not url:
                    sql = """insert into urls(url) values('{}')""".format(o)
                    db.insert(sql)
                    return Request(url=o)
        else:
            sql = """insert into urls(url) values('{}')""".format(url)
            db.insert(sql)
            return r

    #中国少年儿童慈善基金会
    def ccafc(self,url,r):
        sql = """select url from urlsss where url='{}'""".format(url)
        data = db.select(sql)
        if data:
            # url = db.select_max("""select url from urlsss where id = (select max(id) from urlsss)""")
            # 分页的正则
            parr = re.compile('pagesize=\d+')
            # 判断是个人还是企业的正则
            part = re.compile('type=\S+')

            #分页数据
            urls = re.search(parr, url).group()
            urls = urls.split('=')[1]


            #类型数据
            type_url = re.search(part,url).group()
            type = type_url.split("=")[1]
            type = type.split("&")[0]
            type = unquote(type,encoding='utf-8')

            urls = 11500
            while True:
                if type == '个人':
                    urls = int(urls) + 1
                    o = 'http://www.ccafc.org.cn/templates/DonationSearch/index.aspx?nodeid=106&name=&DonationNum=&MinAmount=&MaxAmount=&Payment=&starttime=2009-01-01&endtime=2019-03-13&Project=0&recipients=&type=%E4%B8%AA%E4%BA%BA&pagesize=' + str(
                        urls) + '&pagenum=20'


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
            return r

    #中国扶贫基金会
    # def cfpa(self,url,r):
    #     parr = re.compile('billdate=\d+-\d+-\d+')
    #     day_url = re.search(parr,url).group()
    #     day = day_url.split('=')[1]
    #     sql = """select times from times where times='{}'""".format(day)
    #     print(sql)
    #     days = db.select_time(sql)
    #     if days:
    #         max_sql = """select max(times) from times"""
    #         max_dasy = db.select_max(max_sql)
    #
    #         tiems = datetime.datetime.strptime(max_dasy, '%Y-%m-%d')
    #         max_day = (tiems + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    #
    #         urls = 'http://www.cfpa.org.cn/information/donationlist.aspx?billdate='+ str(max_day)+'&page=1'
    #         pages = db.select(urls)
    #         if pages:
    #             parr = re.compile('page=\d+')
    #             page_url = re.search(parr, urls).group()
    #             page = page_url.split('=')[1]
    #             while True:
    #                 page = int(page) + 1
    #                 o = 'http://www.cfpa.org.cn/information/donationlist.aspx?billdate=' + str(max_day) + '&page=' + str(page)
    #                 data = db.select(o)
    #                 if not data:
    #                     # db.insert(o)
    #                     return Request(url=o)
    #         else:
    #             # db.insert(urls)
    #             return Request(url=urls)
    #     else:
    #         # db.insert(r.url)
    #         return r

