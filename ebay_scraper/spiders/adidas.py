import scrapy
from scrapy_splash import SplashRequest

class EbaySpider(scrapy.Spider):
    name = 'adidas'
    allowed_domains = ['ebay.com.au']
    start_urls = [
        'https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2380057.m570.l2632&_nkw=adidas&_sacat=93427'
    ]

    # Set custom User-Agent for this spider
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy.downloadermiddlewares.offsite.OffsiteMiddleware': None,  # Disable offsite filtering
        },
    }

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 1})   

    def parse(self, response):
        # Extract product details using updated XPath
        for item in response.xpath('//li[contains(@class, "s-item")]'):
            title = item.xpath('.//div[contains(@class, "s-item__title")]/span/text()').get(default="N/A")
            price = item.xpath('.//span[contains(@class, "s-item__price")]/text()').get(default="N/A")
            image = item.xpath('.//div[contains(@class, "s-item__image-wrapper")]/img/@src').get(default="N/A")
            relative_link = item.xpath('.//a[contains(@class, "s-item__link")]/@href').get()
            absolute_link = response.urljoin(relative_link) if relative_link else "N/A"

            yield {
                'title': title,
                'price': price,
                'image': image,
                'link': absolute_link,
            }

        # Handle pagination
        next_page_relative = response.xpath('//a[contains(@class, "pagination__next")]/@href').get()
        if next_page_relative:
            next_page_absolute = response.urljoin(next_page_relative)
            yield SplashRequest(next_page_absolute, self.parse, args={'wait': 1})
