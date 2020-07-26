import requests
from lxml import etree



url = 'http://www.wpsseo.cn/'
headers = {
    
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"
    
    }

parse_url = requests.get(url=url,headers=headers)
parse_url.encoding ='utf-8'
get_html= parse_url.text

tree = etree.HTML(get_html)

jiexi_urls = tree.xpath('//*[@id="jk"]')




for jiexi_url in jiexi_urls:

    jiexi_url = jiexi_url.xpath(".//@value")

print(jiexi_url[0])




