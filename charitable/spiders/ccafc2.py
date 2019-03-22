# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from charitable.Dingding import sendmessage
from charitable.items import CharitableItem

class CcafcSpider(scrapy.Spider):
    name = 'ccafc2'
    allowed_domains = ['ccafc.org.cn']

    start_urls = ['http://www.ccafc.org.cn/templates/DonationSearch/index.aspx?nodeid=106&name=&DonationNum=&MinAmount=&MaxAmount=&Payment=&starttime=2009-01-01&endtime=2019-03-13&Project=0&recipients=&type=%E4%B8%AA%E4%BA%BA&pagesize=1&pagenum=20']
    def parse(self, response):

        i = 0
        #删除时间字段的\r\n
        parr = re.compile('\d+-\d+-\d+')
        #删除留言字段的\xa0
        part = re.compile('\xa0')
        item = CharitableItem()
        Divs = response.xpath("//div[@class='skcx_B']//tr")
        for tr in Divs[1:]:
            #捐赠号
            item['DonationNumber'] = tr.xpath("./td[1]/div/text()").extract_first()
            #捐赠时间
            item['DonationTime'] = re.search(parr,tr.xpath("./td[2]/div/text()").extract_first()).group()
            #捐款人
            item['DonorName'] = tr.xpath("./td[3]/div/text()").extract_first()
            #捐助项目
            item['DonationProject'] = tr.xpath("./td[4]/div/text()").extract_first()
            #受助人
            item['Recipient'] = tr.xpath("./td[5]/div/text()").extract_first()
            if item['Recipient'] == '-':
                item['Recipient'] = ''
            #支付方式
            item['PayMethod'] = tr.xpath("./td[6]/div/text()").extract_first()
            #捐款数
            item['DonationAmount'] = tr.xpath("./td[7]/div/text()").extract_first()
            if ',' in item["DonationAmount"]:
                item["DonationAmount"] = item["DonationAmount"].replace(',','')
            #留言  判断留言是否为None
            item['Note'] = tr.xpath("./td[8]/div/img/@title").extract_first()
            if item['Note']:
                item['Note'] = re.sub(part,'',item['Note'])
            else:
                item['Note'] = ''
            #机构名称
            item['InstitutionName'] = '中国少年儿童慈善救助基金会'
            #捐赠方类型
            item['DonorType'] = '个人'
            #发票号
            item['InvoiceNumber'] = ''
            #捐赠分类
            item['DonationType'] = ''
            #支付平台
            item['PayPlatform'] = ''
            #插入时间
            item['InsertTime'] = datetime.datetime.now().strftime("%Y-%m-%d")

            item['page'] = response.url
            if item['DonationNumber']  and item['DonationAmount']:
                i += 1
            yield item
        # 如果获取的数据量夏小于2就发送一个错误给钉钉
        if i < 2:
          sendmessage('时间-{} 机构-{} 姓名-{}  数据数据量为0  url地址-{}'.format(datetime.datetime.now().strftime("%T-%m-%d %H:%M:%S"),
                                                                  item["InstitutionName"], '王钰清',response.url))

        next_page = response.xpath("//div[@class='skcx_C']//a[last()-1]/img/@title").extract_first()

        if next_page == '下一页':
            next_url = response.xpath("//div[@class='skcx_C']//a[last()-1]/@href").extract_first()

            yield scrapy.Request(url=next_url,callback=self.parse,dont_filter=False)



