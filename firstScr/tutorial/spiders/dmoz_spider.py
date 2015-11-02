# -*- coding: utf-8 -*-
# __author__ = 'summer'
import scrapy
from tutorial.items import DmozItem  #pycharm导入报错问题暂时无法解决

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org/"]
    start_urls = [
    "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
    "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"
    ]

    def parse(self, response):
        sel = scrapy.selector.Selector(response)      #选择器中需要将downloader中回传的response传入 很重要
        sites = sel.xpath('//ul[@class="directory-url"]/li')  #xpath的结尾不能出现'/' 很容易遗漏!
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('text()').extract()
            items.append(item)

        return items
