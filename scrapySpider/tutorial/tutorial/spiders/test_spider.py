from ..items import TutorialItem

import scrapy

# 翻页方法二的全局变量 count
count = 1

class testSpider(scrapy.Spider):
    name = "test_spider"
    start_urls = ["https://www.biquge7.top/xh"]

    def parse(self, response):
        # 方法二中进行页数的累加操作
        global count
        count += 1
        print("当前处在第{}页".format(count))

        divList = response.xpath("//div[@class='tui_1 fenlei']/div")
        # print(len(divList))

        for div in divList:
            # 封面图片链接
            imgLink = div.xpath("./a/img/@src").extract()[0]
            # 小说名称
            title = div.xpath("./div//a/@title").extract()[0]
            # 作者
            author = div.xpath("./div//span/text()").extract()[0]
            # 小说简介
            descp = div.xpath("./div/p/text()").extract()[0]
            # 小说链接
            novelLink = div.xpath("./div//a/@href").extract()[0]

            # print("novelLink", novelLink)
            # 无任何方法的，数据对象，类似基础库中的collections库
            item = TutorialItem(imgLink = "https://www.biquge7.top/" + imgLink,
                                    title = title,
                                    author = author,
                                    descp = descp,
                                    novelLink = novelLink
                                )

            # print(item)

            # 为什么使用yield而不是return
            #
            # 不能使用return这个无容置疑，因为要翻页，使用return直接退出函数；而对于yield:在调用for的时候，函数内部不会立即执行，只是返回了一个生成器对象。
            # 在迭代的时候函数会开始执行，当在yield的时候，会返回当前值(i)。之后的这个函数会在循环中进行，直到没有下一个值。
            yield item

        # # 翻页方法一：定位到下一页按钮，获取下一页url， 然后编写如下代码，在for循环完毕后
        # # 获取下一页的url
        # 经查看，当处在第一页时，上一页的按钮不是a标签，而下方的xpath路径设置选取的为只有一个a的，跳转到第二页的时候，就直接选取到上一页的url了
        # next_href = response.xpath("//div[2]/div[4]/a/@href").extract_first()
        # if next_href:
        #     next_url = response.urljoin(next_href)
        #     print("*" * 60)
        #     print(next_url)
        #     print("*" * 60)
        #     # scrapy.Request(): 把下一页的url传递给Request函数,进行翻页循环数据采集。
        #     request = scrapy.Request(next_url)
        #     yield request


        # # 方法二：定义一个全局变量count = 0,每爬取一页数据，令其加一，构建新的url,再使用scrapy.Request() 发起请求。
        next_url = "https://www.biquge7.top/xh?page={}".format(count)
        yield scrapy.Request(next_url)
