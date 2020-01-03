# -*- coding: utf-8 -*-
import scrapy
import json


class OpenSpider(scrapy.Spider):
    name = 'open'
    #allowed_domains = ['games.crossfit.com/competitions/api/v1/competitions/open/2020/leaderboards?view=0']
    #start_urls = ['https://games.crossfit.com/competitions/api/v1/competitions/open/2020/leaderboards?view=0&division=1&scaled=0&sort=0']

    def start_requests(self):
        yield scrapy.Request(
            url='https://games.crossfit.com/competitions/api/v1/competitions/open/2020/leaderboards?view=0&division=1&scaled=0&sort=0',
            callback=self.parse_athlete,
            meta={
                'current_page': 1,
                'last_page': 2678
            }
        )

    def parse_athlete(self, response):
        data = json.loads(response.body)
        athletes = data.get("leaderboardRows")[0]
        for athlete in athletes.get('entrant'):
            name = athlete.get('competitorName')

            yield {
            	'name': name
            }
            
