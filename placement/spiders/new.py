import re
# import os
# import json
import scrapy
# from cerberus import Validator
from placement.items import Product

class PlacementSpider(scrapy.Spider):
    name = "new"
    start_urls = ['https://amity.edu/placement/upcoming-recruitment.asp']

    def parse(self, response):
        lists = response.xpath("//div[@class='content-wrapper']//li")

        x = Product()
        for ilist in lists:
            x['link'] = "https://amity.edu/placement/" + ilist.xpath("./a/@href").extract_first()
            x['name'] = ilist.xpath(".//strong/text()").extract_first().strip()
            year = re.findall(r'(20\w{2})', ilist.xpath(".//strong/text()").extract_first())
            x['year'] = int(year[0])

            yield x

            # Validation with Cerberus
            # with open(os.path.abspath("schema.json")) as f:
            #     schema = json.loads(f.read())

            # validator = Validator()
            # validator.validate(x, schema)

            # if validator.errors:
            #     exit(f"Validation failed: {validator.errors}")
            #     print()
            # else:
            #     print("No validation errors")
            #     print()
