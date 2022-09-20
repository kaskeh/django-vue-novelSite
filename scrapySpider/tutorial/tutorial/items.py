# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # 定义scrapy items的模块
    # define the fields for your item here like:
    # name = scrapy.Field()

    imgLink = scrapy.Field() # 小说封面图片链接
    title = scrapy.Field()  # 小说名称
    # type = scrapy.Field()   # 小说类型
    author = scrapy.Field() # 小说作者
    descp = scrapy.Field()  # 小说简介
    novelLink = scrapy.Field() # 小说入口链接
