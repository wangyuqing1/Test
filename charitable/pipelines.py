# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymssql
from charitable.log import Logger
from charitable.Dingding import sendmessage
import datetime




class CharitablePipeline(object):

    def open_spider(self,spider):
        self.conn = pymssql.connect(host='39.107.232.213',user='yishan',password='!QAZxsw2',database='YISHAN_Collection')
        self.cur = self.conn.cursor()


    def process_item(self, item, spider):
        if item['DonorName'] == None or item['DonorName'] == '' or item['DonationProject'] == None:
            pass
        else:
            # if DonationNumber:
            #     pass
            # else:
            try:

                sql = """insert into donation_data(DonationNumber,InvoiceNumber,
                   DonorName,DonationAmount,
                   DonationProject,PayMethod,
                   DonationType,DonationTime,
                   PayPlatform,DonorType,
                   Recipient,Note,
                   InstitutionName,InsertTime)
                   values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""" .format(item['DonationNumber'],
                        item['InvoiceNumber'],
                        item['DonorName'],
                        item['DonationAmount'],
                        item['DonationProject'],
                        item['PayMethod'],
                        item['DonationType'],
                        item['DonationTime'],
                        item['PayPlatform'],
                        item['DonorType'],
                        item['Recipient'],
                        item['Note'],
                        item['InstitutionName'],
                        item['InsertTime']
                        )
                self.cur.execute(sql)
                self.conn.commit()
            except Exception as e:
                sendmessage('时间-{} 机构-{} 姓名-{}  插入数据时出现错误'.format(datetime.datetime.now().strftime("%T-%m-%d %H:%M:%S"),item["InstitutionName"],'王钰清'))
                log = Logger(r'log\all.log',level='debug')
                log.logger.error(" 插入数据错误  time-{}  机构名称-{}  名字-{} 错误详情-{}".format(datetime.datetime.now(),item["InstitutionName"],"王钰清",e))
                self.conn.rollback()



            return item
        # else:
        #     pass

    def close_spider(self,spider):
        self.cur.close()
        self.conn.close()

