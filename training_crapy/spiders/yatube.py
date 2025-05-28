import scrapy


class YatubeSpider(scrapy.Spider):
    name = "yatube"
    allowed_domains = ["158.160.177.221"]
    start_urls = ["http://158.160.177.221/"]

    def parse(self, response):
        for quote in response.css('div.card-body'):
            text = ' '.join(
                t.strip() for t in quote.css('p::text').getall()
            ).strip()
            yield {
                'author': quote.css('strong::text').get(),
                'text': text,
                'date': quote.css('small.text-muted::text').get(),
            }

        next_page = response.css('li.page-item a::attr(href)').getall()[-1]
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
