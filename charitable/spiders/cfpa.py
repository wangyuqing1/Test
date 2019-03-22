# # -*- coding: utf-8 -*-
# import scrapy
# import datetime
# import pymssql
# from charitable.items import CharitableItem
# from scrapy import Spider
# # old_day = datetime.datetime(2012,1,1)
# # new_day = datetime.datetime.now()
# # day = (new_day-old_day).days
#
#
# class pink_DB(object):
#     def __init__(self):
#         self.conn = pymssql.connect(host='127.0.0.1',user='sa',password='123456',database='ccadc')
#         self.cur = self.conn.cursor()
#
#     def insert_time(self,time):
#         try:
#             sql = """insert into times(times) values('{}')""".format(time)
#             self.cur.execute(sql)
#             self.conn.commit()
#         except:
#             self.conn.rollback()
#
#     def select_time(self,time):
#         sql = """select times from times where times='{}'""".format(time)
#         self.cur.execute(sql)
#         day = self.cur.fetchone()
#         if day:
#             return True
#         return False
#
# db = pink_DB()
# class CfpasSpider(Spider):
#
#     name = 'cfpa'
#     allowed_domains = ['cfpa.org.cn']
#     start_urls = ['http://www.cfpa.org.cn/information/donationlist.aspx?billdate=2012-01-01&page=1']
#     day = 2629
#     def parse(self, response):
#         Data_List = response.xpath("//table[@class='list']/tr")
#         Item = CharitableItem()
#         for Data in Data_List:
#             #捐赠人
#             Item['DonorName'] = Data.xpath('./td[1]/text()').extract_first()
#             #捐款数
#             Item['DonationAmount'] = Data.xpath('./td[2]/text()').extract_first()
#             #捐款项目
#             Item['DonationProject'] = Data.xpath('./td[4]/text()').extract_first()
#             #捐款时间
#             Item['DonationTime'] = Data.xpath('./td[3]/text()').extract_first()
#             #捐赠号
#             Item['DonationNumber'] = ''
#             #发票号
#             Item['InvoiceNumber'] = ''
#             #支付渠道
#             Item['PayMethod'] = ''
#             #捐赠分类
#             Item['DonationType'] = ''
#             #支付平台
#             Item['PayPlatform'] = ''
#             #捐赠方类型
#             Item['DonorType'] = ''
#             #受助方
#             Item['Recipient'] = ''
#             #备注
#             Item['Note'] = ''
#             #插入时间
#             Item['InsertTime'] = datetime.datetime.now().strftime("%Y-%m-%d")
#             #机构名称
#             Item['InstitutionName'] = '中国扶贫基金会'
#
#             Item['page'] = response.url
#
#
#             yield Item
#         next = response.xpath('//div[@class="page"]/a[last()-1]')
#
#         if  next:
#             next_text = next.xpath('./text()').extract_first()
#             # print(next_text)
#             if next_text == '下一页':
#
#                 next_url = next.xpath('./@href').extract_first()
#                 # print(next_url)
#                 print(response.urljoin(next_url))
#                 yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse,dont_filter=False)
#             else:
#                 # global day
#                 print(self.day)
#                 self.day -= 1
#                 print(self.day)
#                 tim=datetime.datetime.now()
#                 tiem = (tim+datetime.timedelta(days=-self.day)).strftime("%Y-%m-%d")
#                 print(tiem)
#                 while True:
#                     day = db.select_time(tiem)
#                     if day:
#                         tiems = datetime.datetime.strptime(tiem,'%Y-%m-%d')
#                         tiem = (tiems + datetime.timedelta(days = 1)).strftime("%Y-%m-%d")
#                     elif not day:
#                         db.insert_time(tiem)
#                         break
#                 str = "http://www.cfpa.org.cn/information/donationlist.aspx?billdate={}&page=1".format(tiem)
#                 print(str)
#                 yield scrapy.Request(url=str, callback=self.parse, dont_filter=False)
#                         # break
