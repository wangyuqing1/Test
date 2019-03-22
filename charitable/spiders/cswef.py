# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from charitable.items import CharitableItem
from charitable.Dingding import sendmessage
class CswefSpider(scrapy.Spider):
    name = 'cswef'
    allowed_domains = ['cswef.cn']
    start_urls = ['http://www.cswef.cn/Home/Donquery/index/status/2/p/1.html']

    def parse(self, response):
        #去除  换行  空格
        pattern = re.compile('\t|\n| ')
        i = 0
        #注释里面的内容
        parr = re.compile('\d+')
        item = CharitableItem()
        tr_list = response.xpath("//table[@class='donaInquTable']/tr")
        for tr in tr_list[1:]:

            #项目名称
            item["DonationProject"] = re.sub(pattern,'',tr.xpath("./td[1]/text()").extract_first())
            #捐款方
            item["DonorName"] = re.sub(pattern,'',tr.xpath("./td[2]/text()").extract_first())
            #捐款金额
            item["DonationAmount"] = re.sub(pattern,'',tr.xpath("./td[3]/text()").extract_first()).split('元')[0]
            if ',' in item["DonationAmount"]:
                item["DonationAmount"] = item["DonationAmount"].replace(',','')
            #捐款时间
            item["DonationTime"] = re.sub(pattern,'',tr.xpath("./td[4]/text()").extract_first())
            list1 = list(item["DonationTime"])
            list1.insert(10,' ')
            item["DonationTime"] = ''.join(list1)
            #支付渠道
            item['PayMethod'] = re.sub(pattern,'',tr.xpath('./td[5]/text()').extract_first())
            #捐赠号
            item['DonationNumber'] = re.search(parr,tr.xpath("./node()[6]").extract_first()).group()
            #发票号
            item['InvoiceNumber'] = ''
            #捐赠分类
            item['DonationType'] = ''
            #支付平台
            item['PayPlatform'] = ''
            #捐赠方类型
            item['DonorType'] = ''
            #受助方
            item['Recipient'] = ''
            #备注
            item['Note'] = ''
            #机构名称
            item['InstitutionName'] = '中国社会福利基金会'
            #插入时间
            item['InsertTime'] = datetime.datetime.now().strftime("%Y-%m-%d")
            if item["DonationProject"] and item["DonationAmount"]:
                i += 1
            yield item
        # 如果获取的数据量夏小于2就发送一个错误给钉钉
        if i < 2:
            sendmessage('时间-{} 机构-{} 姓名-{}  数据数据量为0  url地址-{}'.format(datetime.datetime.now().strftime("%T-%m-%d %H:%M:%S"),
            item["InstitutionName"], '王钰清',response.url))

        next_page = response.xpath("//div[@class='green']/div/a[@class='next']/text()").extract_first()
        if next_page == '下一页':
            next_url = 'http://www.cswef.cn' + response.xpath("//div[@class='green']/div/a[@class='next']/@href").extract_first()
            yield scrapy.Request(url=next_url,callback=self.parse)

