# -*- coding: utf-8 -*-
import scrapy
import json
from time import sleep


class OpenSpider(scrapy.Spider):
    name = 'open'
    # allowed_domains = ['games.crossfit.com/competitions/api/v1/competitions/open/2020/leaderboards?view=0']
    # start_urls = ['https://games.crossfit.com/competitions/api/v1/competitions/open/2020/leaderboards?view=0&division=1&scaled=0&sort=0']

    def start_requests(self):
        yield scrapy.Request(
            url='https://games.crossfit.com/competitions/api/v1/competitions/open/2020/leaderboards?view=0&division=1&scaled=0&sort=0&page=1',
            callback=self.parse_athlete,
            meta={
                'current_page': 1
            }
        )

    def parse_athlete(self, response):
        data = json.loads(response.body)
        # last_page = data.get('pagination').get('totalPages')
        athletes = data.get("leaderboardRows")

        for athlete in athletes:
        	try:
	            name = athlete.get('entrant').get('competitorName')
	            sex = athlete.get('entrant').get("gender")
	            country_code = athlete.get('entrant').get("countryOfOriginCode")
	            country = athlete.get('entrant').get("countryOfOriginName")
	            affiliate_name = athlete.get('entrant').get("affiliateName")
	            age = athlete.get('entrant').get("age")
	            height = athlete.get('entrant').get("height")
	            weight = athlete.get('entrant').get("weight")
	            countryChampion = athlete.get('ui').get('countryChampion')
	            overallRank = athlete.get('overallRank')
	            overallScore = athlete.get('overallScore')

	            yield {
	                'name': name,
	                'sex': sex,
	                'country_cod)': country_code,
	                'country': country,
	                'affiliate_name': affiliate_name,
	                'age': age,
	                'height': height,
	                'weight': weight,
	                'countryChampion': countryChampion,
	                'overallRank': overallRank,
					'overallScore': overallScore

	            }
        	except:
        		pass
        
        sleep(3)

        last_page = 10
        current_page = response.request.meta['current_page'] + 1

        if last_page >= current_page:
        	yield scrapy.Request(
        		url=f'https://games.crossfit.com/competitions/api/v1/competitions/open/2020/leaderboards?view=0&division=1&scaled=0&sort=0&page={current_page}',
	            callback=self.parse_athlete,
	            meta={'current_page': current_page})
	    

	    
