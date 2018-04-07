# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DataExcavateItem(scrapy.Item):
    # define the fields for your item here like:
    ranking = scrapy.Field()
    movie_name = scrapy.Field()
    movie_englishname = scrapy.Field()
    score = scrapy.Field()
    score_num = scrapy.Field()



    # pass
