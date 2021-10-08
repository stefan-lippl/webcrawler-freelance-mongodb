import datetime
from scrapy import Spider
from scrapy.http import Request
from pymongo import MongoClient

connection = MongoClient(
            "mongodb+srv://stefan-lippl:Windows64bit$@cluster0.kkskd.mongodb.net/Freelance?retryWrites=true&w=majority")
db = connection.Freelance
collection = db.projects


class FreelanceSpider(Spider):
    name = 'freelance_mongo'
    start_urls = [
        'https://freelance.de/search/project.php?p&__search_sort_by=1&__search_method=off&_offset=0']

    def parse(self, response):
        jobs = response.xpath(
            '//h3[@class="action-icons-overlap"]/a/@href').extract()

        for job in jobs:
            absolute_job_url = f"https://www.freelance.de{job}"
            yield Request(absolute_job_url,
                          callback=self.parse_job)

        next_page = response.xpath(
            '//li/a[@aria-label="Next"]/@href').extract_first()
        absolute_next_page = f"https://freelance.de{next_page}"

        if next_page:
            yield Request(absolute_next_page, self.parse)

    def parse_job(self, response):
        job_title = response.xpath(
            '//h1[@class="margin-bottom-xs"]/text()').extract()

        try:
            job_id = response.xpath(
                '//li/i[@data-original-title="Referenz-Nummer"]/following-sibling::text()').extract_first().strip()
        except:
            job_id = 'None'

        try:
            date_job_posted = response.xpath(
                '//li/i[@data-original-title="Letztes Update"]/following-sibling::text()').extract_first().strip()
        except:
            date_job_posted = 'None'
        try:
            job_duration = response.xpath(
                '//div[contains(@class, "project-detail-title") and text() = "Dauer:"]/following-sibling::div/text()').extract_first().strip()
        except:
            job_duration = 'None'

        try:
            tags = response.xpath(
                '//div[@class="cat_object"]/a/text()').extract()
        except:
            tags = 'None'
        try:
            job_description = response.xpath(
                '//div[@class="panel-body highlight-text"]/text()').extract()
        except:
            job_description = 'None'

        try:
            job_location = response.xpath(
                '//li/i[@data-original-title="Projektort"]/following-sibling::text()').extract_first().strip()
        except:
            job_location = 'None'

        try:
            must_haves = response.xpath(
                '//div[@class="panel-body highlight-text"]/ul/li/text()').extract()
        except:
            must_haves = 'None'

        try:
            project_url = str(response)
        except:
            project_url = 'None'

        collection.insert_one({
            'job_id': job_id,
            'date_posted': date_job_posted,
            'job_title': job_title,
            'job_duration': job_duration,
            'tags': must_haves,
            'company': 'None',
            'job_location': job_location,
            'job_description': job_description,
            'project_url': project_url,
            'category': 'data science',
            'website': 'freelance.de',
            'date': datetime.datetime.now()
        })
