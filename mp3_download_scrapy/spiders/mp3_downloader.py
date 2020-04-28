# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from mp3_download_scrapy.items import Mp3DownloadScrapyItem


class Mp3DownloaderSpider(scrapy.Spider):
    name = 'downloader'
    start_urls = ['http://hcmaslov.d-real.sci-nnov.ru/public/mp3/Metallica/Albums/1996%20-%20Load']

    def parse(self, response):
        for link in response.xpath("//following::tr[4]/td[2]/a[contains(@href,'mp3')]"):
            loader = ItemLoader(item=Mp3DownloadScrapyItem(),selector=link)
            relative_url = link.xpath(".//@href").extract_first()
            absolute_url = response.urljoin(relative_url)
            loader.add_value('file_urls',absolute_url)
            yield loader.load_item()
