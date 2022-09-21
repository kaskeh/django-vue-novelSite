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
    novelCate = scrapy.Field() # 小说分类拼音缩写
    novelCateText = scrapy.Field() # 小说分类名称
    novelStatus = scrapy.Field() # 小说状态：完结，连载

class novel_content(scrapy.Item):
    novelId = scrapy.Field()    # 到时从链接上截取当前章节对应的小说编号
    novelChapterTitle = scrapy.Field() # 小说章节名称
    novelChapterNumber = scrapy.Field() # 小说章节编号
    novelContent = scrapy.Field()   # 小说内容