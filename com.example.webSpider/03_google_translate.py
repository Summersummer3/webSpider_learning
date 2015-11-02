__author__ = 'summer'
import urllib2
import urllib
import json
import time
import random

while True:
    content = raw_input("input your want to translate(enter 'exit' to exit):")

    if content == 'exit':
        break

    ip_list = ['111.23.10.8', '218.200.66.198', '124.88.67.14']

    proxy_support = urllib2.ProxyHandler({'http': random.choice(ip_list)})

    opener = urllib2.build_opener(proxy_support)
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36')]

    urllib2.install_opener(opener)

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&' \
          'smartresult=rule&smartresult=ugc&sessionFrom=http://dict.youdao.com/'
    data={
    'type':'AUTO',
    'i':content,
    'doctype':'json',
    'xmlVersion':'1.8',
    'keyfrom':'fanyi.web',
    'ue':'UTF-8',
    'action':'FY_BY_ENTER',
    'typoResult':'true'
    }

    data = urllib.urlencode(data).encode('UTF-8')

    req = urllib2.Request(url,data)

    response = urllib2.urlopen(req)
    html = response.read().decode('UTF-8')


    target = json.loads(html)
    if target.has_key('smartResult'):
        print("result: %s") % (target['smartResult']['entries'][1])
    else:
        print("result: %s") % (target['translateResult'][0][0]['tgt'])

    time.sleep(2)