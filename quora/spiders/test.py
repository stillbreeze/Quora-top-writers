
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from quora.items import QuoraItem

class MySpider(CrawlSpider):
	name = "quora"
	allowed_domains = ["https://www.quora.com/"]
	start_urls = [
	"https://www.quora.com/Adam-DAngelo/following",
	]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		path = '//div'
		links = hxs.select(path)
		items = []
		for link in links:
			item = QuoraItem()
#			item['title'] = ''
			item['link'] = link.extract()
			items.append(item)
		return items

"""
	def parse(self, response):
		path = ''
		item = QuoraItem()
		item['link'] = response.xpath("//span[contains(@class,'truncated')]").extract()
		return item
"""