# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class ZhaifuliPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        url_name = request.url.split('/')
        file_name = url_name[-2] + url_name[-1]
        return file_name

    def get_media_requests(self, item, info):
        for url in item['img_url']:
            yield Request(url)

    def item_completed(self, results, item, info):
        item = super(ZhaifuliPipeline, self).item_completed(results, item, info)

        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        return item
