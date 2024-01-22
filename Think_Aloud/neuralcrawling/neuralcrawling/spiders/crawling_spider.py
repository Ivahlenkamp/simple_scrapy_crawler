#https://www.youtube.com/watch?v=m_3gjHGxIJc

from scrapy.spiders import CrawlSpider, Rule

from scrapy.linkextractors import LinkExtractor


class CrawlingSpider(CrawlSpider):
      name = "mycrawler"
      allow_domains = ["toscrape.com"]
      start_urls = ["http://books.toscrape.com/"]

      rules = (
            Rule(LinkExtractor(allow = "catalogue/category")),
      )