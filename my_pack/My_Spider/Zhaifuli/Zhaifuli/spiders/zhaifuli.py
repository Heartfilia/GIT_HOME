# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

import re

from Zhaifuli.items import ZhaifuliItem
base_url = ''    # 这个是主要的页面信息


class ZhaifuliSpider(scrapy.Spider):
    name = 'zhaifuli'
    allowed_domains = [base_url, '']   # 这里面是允许爬取的域名范围[注意第二个哪个是图片的url域,和主页不一样]
    start_urls = [f'https://{base_url}/luyilu/list_5_1.html']

    def parse(self, response):
        urls = response.xpath('/html/body/section/div/div/article/header/h2/a/@href').extract()
        for url in urls:
            full_url = f'https://{base_url}/{url}'
            yield Request(full_url, callback=self.second_page)

        next_page = response.xpath('/html/body/section/div/div/div[2]/ul/li[6]/a/@href').extract_first()
        if next_page:
            next_url = f'https://{base_url}/luyilu/{next_page}'
            yield Request(next_url, callback=self.parse)

    def second_page(self, response):
        img_urls = response.xpath('/html/body/section/div/div/article/p/img/@src').extract()
        item = ZhaifuliItem()

        item['img_url'] = img_urls
        yield item

        next_page = response.xpath(
            '/html/body/section/div/div/div[2]/ul/li[@class="next-page"]/a/@href').extract_first()
        if next_page:
            head_url = re.findall(r'(.*)/\d+\.html|(.*)/\d+_\d+\.html', response.url)[0]
            html_url = head_url[0] + head_url[1]
            next_url = f'{html_url}/{next_page}'
            yield Request(next_url, callback=self.second_page)
