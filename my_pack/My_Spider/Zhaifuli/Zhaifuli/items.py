# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhaifuliItem(scrapy.Item):
    # define the fields for your item here like:
    img_url = scrapy.Field()
    image_path = scrapy.Field()
