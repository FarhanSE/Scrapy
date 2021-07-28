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

            yield response.follow(country_link, callback=self.country_data, meta = {"country_name":country_name})
    def country_data(slef, response):
        name = response.request.meta["country_name"]
        row = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for r in row:
            year = r.xpath(".//td[1]/text()").get()
            population = r.xpath(".//td[2]/text()").get()
            yield {
                "Country name":name,
                "Year": year,
                "Population": population
            }
