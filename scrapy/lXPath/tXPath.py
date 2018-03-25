from scrapy.selector import Selector
with open('../superHero.xml','r') as fp:
    body = fp.read()
print(Selector(text = body).xpath('/*').extract())
print(Selector(text = body).xpath('/html/body/superhero/class[1]').extract())

subBody = Selector(text = body).xpath('/html/body/superhero/class[last()-1]')
print(subBody)
