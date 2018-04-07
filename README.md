# movie_top250
crawl douban movie top250

Reference: [Scrapy爬虫框架教程（二）-- 爬取豆瓣电影TOP250](http://woodenrobot.me/2017/01/07/Scrapy%E7%88%AC%E8%99%AB%E6%A1%86%E6%9E%B6%E6%95%99%E7%A8%8B%EF%BC%88%E4%BA%8C%EF%BC%89-%E7%88%AC%E5%8F%96%E8%B1%86%E7%93%A3%E7%94%B5%E5%BD%B1TOP250/)

#### File structure

```
movie_top250——.idea
                 scrapy.cfg
                 movie_top_english.csv
                 DataExcavate——_init_.py
                                 item.py
                                 middlewares.py
                                 pipelines.py
                                 settings.py
                                 spiders——_init_.py
                                            movie_spider.py
```
Among them, item.py is used to define the data ; movie_spider.py is used to crawl data;  movie_top_english.csv is the result.

#### Code analysis

```
# coding=utf-8  //Used to identify Chinese
```
Add request header to ensure that they can be responded:

```
def start_requests(self):
    url = 'https://movie.douban.com/top250'
    yield Request(url, headers=self.headers)
```
For each movie, the elements of the page are extracted as divs into the corresponding data names in the item:

```
for movie in movies:
    item['ranking'] = movie.xpath('.//div[@class="pic"]/em/text()').extract()[0]
    item['movie_name'] = movie.xpath(
        './/div[@class="hd"]/a/span[1]/text()').extract()[0]
    item['movie_englishname'] = movie.xpath(
        './/div[@class="hd"]/a/span[2]/text()').extract()
    item['score'] = movie.xpath(
        './/div[@class="star"]/span[@class="rating_num"]/text()'
    ).extract()[0]
    item['score_num'] = movie.xpath(
        './/div[@class="star"]/span/text()').re(ur'(\d+)人评价')[0]
```
Automatic crawling of the next page through next_url:

```
next_url = response.xpath('//span[@class="next"]/a/@href').extract()
if next_url:
    next_url = 'https://movie.douban.com/top250' + next_url[0]
    yield Request(next_url, headers=self.headers)
```

#### Attention
1. cmd:Enter the corresponding folder, input: 
> scrapy crawl movie_top -o movie_top_english.csv.

movie_top is the name of the class,it can alse be another name; -o means the data saved in csv format.

2. Csv file which containing Chinese characters directly opened with excel will be garbled. You can set excel with reference to [the document](https://blog.csdn.net/leonzhouwei/article/details/8447643)
