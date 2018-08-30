import scrapy
from tutorial.items import zhdj_cms_content
from datetime import datetime


class CPCSpider(scrapy.Spider):
    name = "cpc.cms"

    def start_requests(self):
        urls = [
            'http://cpc.people.com.cn/GB/64093/64094/index1.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        global content
        for node in response.css("div.fl ul>li"):
            content = zhdj_cms_content()
            content['title'] = node.css("a::text").extract_first()
            content['time'] = node.css("i::text").extract_first()
            content['created_at'] = datetime.now()
            content['url'] = response.urljoin(node.css("a::attr(href)").extract_first())
            # 请求详情页，二级流程
            yield scrapy.Request(url=content['url'], callback=self.parse_detail, meta={'data': content})

        nodes = response.css("div.fl > div > a")
        is_have_next = nodes[-1].css("a::text").extract_first() == '下一页' if isinstance(nodes, list) and nodes else False
        next_page = nodes[-1].css("a::attr(href)").extract_first()
        if is_have_next:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_detail(self, response):
        content = response.meta['data']
        # 如果详情页404，content和details都不会存在
        content['detail'] = response.css("div.show_text").extract_first()

        yield content
