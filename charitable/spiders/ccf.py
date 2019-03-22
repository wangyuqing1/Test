# -*- coding: utf-8 -*-

'''总数据已经抓完  剩下要做更新数据'''
import scrapy
import re
import datetime
from charitable.items import CharitableItem


class CcfSpider(scrapy.Spider):
    name = 'ccf'
    # allowed_domains = ['http://www.chinacharityfederation.org/']
    start_urls = ['http://www.chinacharityfederation.org/PublicExchange/144/1.html?p=1&di=1997-03-01&da=2019-03-19']

    def parse(self, response):
        tr_list = response.xpath("//div[@class='news_center_list']/table/tr")
        item = CharitableItem()

        #分割钱数
        parr = re.compile("\r|\n|\t")
        i = 1
        for tr in tr_list[1:]:
            #捐赠时间
            item["DonationTime"] = tr.xpath("td[1]/text()").extract_first()
            #捐赠项目
            item["DonationProject"] = tr.xpath("td[2]/text()").extract_first()
            #捐款金额
            item["DonationAmount"] = re.sub(parr,"",tr.xpath("td[3]/span/text()").extract_first().split("+")[1])
            #捐款人名字
            item["DonorName"] = tr.xpath("td[4]/text()").extract_first()
            #留言
            item["Note"] = re.sub(parr,"",tr.xpath("td[5]/text()").extract_first())
            #支付平台
            item["PayPlatform"] = tr.xpath("td[6]/img/@title").extract_first()
            #支付渠道
            if "微信" in item["PayPlatform"]:
                item["PayMethod"] = "微信支付"
            elif "CMP" in item["PayPlatform"]:
                item["PayMethod"] = "支付宝"
            else:
                item["PayMethod"] = "其他"

            #捐赠分类
            item["DonationType"] = ''
            #捐赠方类型
            item["DonorType"] = ''
            #受助方
            item["Recipient"] = ''
            #机构名称
            item['InstitutionName'] = "中华慈善总会"
            #插入时间
            item["InsertTime"] = datetime.datetime.now().strftime("%Y-%m-%d")
            #捐赠好
            item["DonationNumber"] = ''
            #发票号
            item["InvoiceNumber"] = ''
            yield item

        next_page = response.xpath("//div[@class='news_center']/div[@class='page']/a[last()]/text()").extract_first()
        print(next_page)
        if next_page == '下一页»':
            next_url = response.xpath("//div[@class='news_center']/div[@class='page']/a[last()]/@href").extract_first()
            url = "http://www.chinacharityfederation.org" + next_url

            yield scrapy.Request(url=url,callback=self.parse)