import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countires = response.xpath("//td/a")
        for country in countires:
            country_name = country.xpath("./text()").get()
            country_link = country.xpath("./@href").get()
            # ful_url = f"https://www.worldometers.info{country_link}"
            # ful_url = response.urljoin(country_link)

            yield response.follow(country_link)
