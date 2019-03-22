# from scrapy.crawler import CrawlerProcess
# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.triggers.cron import CronTrigger
# from scrapy.utils.project import get_project_settings
#
# from charitable.spiders.ccf import CcfSpider
#
# def api(crawler,spider):
#     try:
#         crawler.crawl(spider)
#         crawler.start()
#     except:
#         pass
# if __name__ == '__main__':
#     settings = get_project_settings()
#     crawler = CrawlerProcess(settings)
#     spider = CcfSpider()
#     scheduler = BackgroundScheduler()
#     cron = CronTrigger(second='*/20')
#     scheduler.add_job(func=api,trigger=cron,args=[crawler,spider])
#     scheduler.start()



from apscheduler.schedulers.blocking import BlockingScheduler
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from charitable.spiders.ccf import CcfSpider

def run_spider(crawler,spider):
    crawler.crawl(spider)
    crawler.start(stop_after_crawl=False)

scheduler = BlockingScheduler()
spider = CcfSpider()
settings = get_project_settings()
crawler = CrawlerProcess(settings)
scheduler.add_job(func=run_spider,trigger='cron',hour='17',minute='15',args=[crawler,spider])
scheduler.start()



