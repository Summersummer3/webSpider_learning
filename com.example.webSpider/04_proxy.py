import urllib2
import random

url = 'http://www.whatismyip.com.tw'

ip_list = ['111.23.10.8', '218.200.66.198', '124.88.67.14']

proxy_support = urllib2.ProxyHandler({'http': random.choice(ip_list)})

opener = urllib2.build_opener(proxy_support)
opener.addheaders = \
    [('User-Agent',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit'
      '/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36')]

urllib2.install_opener(opener)

response = urllib2.urlopen(url)

html = response.read()

print(html)
