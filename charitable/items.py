# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CharitableItem(scrapy.Item):
    # 捐赠号 对应 DonationNumber 字段
    DonationNumber = scrapy.Field()
    # 发票号 对应 InvoiceNumber 字段
    InvoiceNumber = scrapy.Field()
    # 捐款方 对应 DonorName 字段
    DonorName = scrapy.Field()
    # 捐赠金额 对应 DonationAmount 字段
    DonationAmount = scrapy.Field()
    # 捐赠项目 对应 DonationProject 字段
    DonationProject = scrapy.Field()
    # 支付渠道  对应 PayMethod 字段
    PayMethod = scrapy.Field()
    # 捐赠分类 对应 DonationType 字段
    DonationType = scrapy.Field()
    # 捐赠时间 对应 DonationTime 字段
    DonationTime = scrapy.Field()
    # 支付平台 对应 PayPlatform 字段
    PayPlatform = scrapy.Field()
    # 捐赠方类型 对应 DonorType 字段
    DonorType = scrapy.Field()
    # 受助方 对应 Recipient 字段
    Recipient = scrapy.Field()
    # 备注 对应 Note
    Note = scrapy.Field()
    #机构名称
    InstitutionName = scrapy.Field()
    #插入时间
    InsertTime = scrapy.Field()
    page = scrapy.Field()

