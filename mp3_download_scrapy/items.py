# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Mp3DownloadScrapyItem(scrapy.Item):
    file_urls = scrapy.Field() # download Url
    files = scrapy.Field() # Save Downloaded files
