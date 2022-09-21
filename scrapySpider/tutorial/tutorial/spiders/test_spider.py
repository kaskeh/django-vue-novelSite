from ..items import TutorialItem, novel_content

import scrapy

# 翻页方法二的全局变量 count
count = 1

class testSpider(scrapy.Spider):
    name = "test_spider"
    # 是允许爬取的域名，防止爬虫爬到其他网站
    allowed_domains = ["www.biquge7.top"]
    start_urls = ["https://www.biquge7.top/"]
    root_url = "https://www.biquge7.top/"
    # headers = {
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    #     'Cookie': 'Hm_lvt_bfe6b19ea4d61a4b723235442982102c=1596154422,1596699752,1597652311,1598425017; Hm_lpvt_bfe6b19ea4d61a4b723235442982102c=1598425038'
    # }

    custom_settings = {
        'ITEM_PIPELINES': {
            'tutorial.pipelines.novelChapterPipeline': 300}
    }

    def parse(self, response):

        # 获取当前分类
        cateList = response.xpath("//ul[@class='nav']/li")
        for index in range(1, len(cateList) - 2):
            # 分类链接
            cate_url = cateList[index].xpath("./a/@href").extract()[0]
            # 分类名称拼音首字母
            cata = cate_url[-2:]
            # 分类名称
            cata_text = cateList[index].xpath("./a/text()").extract()[0]
            yield scrapy.Request(url = cate_url,
                                 callback = self.parse_chapter,
                                 meta={"cata": cata, "cata_text": cata_text, "page_count": 1}
                                 )

    # 每个分类下所有分页的小说入口信息
    def parse_chapter(self, response):
        # print("当前url,", response.url)

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
            item = TutorialItem(imgLink="https://www.biquge7.top/" + imgLink,
                                title=title,
                                author=author,
                                descp=descp,
                                novelLink=novelLink,
                                novelCate = response.meta['cata'],
                                novelCateText = response.meta['cata_text']
                                )

            # 为什么使用yield而不是return
            #
            # 不能使用return这个无容置疑，因为要翻页，使用return直接退出函数；而对于yield:在调用for的时候，函数内部不会立即执行，只是返回了一个生成器对象。
            # 在迭代的时候函数会开始执行，当在yield的时候，会返回当前值(i)。之后的这个函数会在循环中进行，直到没有下一个值。
            yield scrapy.Request(
                url = novelLink,
                callback =  self.parse_novel_mes,
                meta={"item": item}
            )
        #
        # # # 翻页方法一：定位到下一页按钮，获取下一页url， 然后编写如下代码，在for循环完毕后
        # # # 获取下一页的url
        # # 经查看，当处在第一页时，上一页的按钮不是a标签，而下方的xpath路径设置选取的为只有一个a的，跳转到第二页的时候，就直接选取到上一页的url了
        # # next_href = response.xpath("//div[2]/div[4]/a/@href").extract_first()
        # # if next_href:
        # #     next_url = response.urljoin(next_href)
        # #     print("*" * 60)
        # #     print(next_url)
        # #     print("*" * 60)
        # #     # scrapy.Request(): 把下一页的url传递给Request函数,进行翻页循环数据采集。
        # #     request = scrapy.Request(next_url)
        # #     yield request
        #
        #
        # # 方法二：定义一个全局变量count = 0,每爬取一页数据，令其加一，构建新的url,再使用scrapy.Request() 发起请求。
        # next_url = "https://www.biquge7.top/{}?page={}".format(response.meta['novel_class'], count)
        # yield scrapy.Request(next_url)


        # next_page_url = response.xpath("//div[@class='page']/a[2]/@href").extract_first()
        # max_page = response.xpath("//div[@class='page']/text()").extract_first().split("/")[1]
        max_page = response.xpath("//div[@class='page']/@data-max").extract_first()
        page_count = response.meta["page_count"]

        if int(max_page) >= page_count:
            # print("当前有下一页", next_page_url)
            page_count += 1
            next_page_url = "https://www.biquge7.top/{}?page={}".format(response.meta["cata"], page_count)
            yield scrapy.Request(next_page_url, callback = self.parse_chapter,
            meta = {"cata": response.meta["cata"],
                    "cata_text": response.meta["cata_text"],
                    "page_count": page_count
                    }
            )
        else:
            print("没有下一页了")

    # 小说章节页
    def parse_novel_mes(self, response):
        # 小说状态
        novel_status = response.xpath("//div[@class='up']/span[2]/text()").extract()[0].split("：")[1]
        item = response.meta["item"]
        # 而外添加一个标记小说状态的属性
        item["novelStatus"] = novel_status
        # 保存小说信息
        yield item

        # 开始循环获取每个章节页链接
        chapterList = response.xpath("//div[@class='list']/ul")
        for li in chapterList:
            # 章节链接
            chapterLink = li.xpath(".//a/@href").extract()[0]    # 有点问题，不时出现，IndexError: list index out of range
            # 章节名称
            chapterTitle = li.xpath(".//a/text()").extract()[0]
            # 章节编号
            chapterNumber = li.xpath(".//a/@href").extract()[0].split("/")[-1]
            # 关联的作品id
            novelNumber = response.url.split("/")[-1]

            # 开始对内容进行抓取
            yield scrapy.Request(url = chapterLink,
                                 meta={
                                     "chapterTitle": chapterTitle,
                                     "chapterNumber": chapterNumber,
                                     "novelNumber": novelNumber
                                 },
                                 callback = self.parse_content
                                 )

    # 小说内容页
    def parse_content(self, response):
        # print("到达了最后的流程", response.meta["chapterTitle"])

        # 小说内容
        novelContent = response.xpath("//div[@class='text']/text()")

        item = novel_content(
                            novelId=response.meta["novelNumber"],
                            novelChapterNumber=response.meta["chapterNumber"],
                            novelChapterTitle=response.meta["chapterTitle"],
                            novelContent=novelContent
                             )
        yield item