from scrapy import cmdline


zfl = 'scrapy crawl zhaifuli --nolog'
# zfl = 'scrapy crawl zhaifuli'

cmdline.execute(zfl.split())
