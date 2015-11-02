__author__ = 'summer'

import urllib2
import re

def url_open(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit'
                                '/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36')
    response = urllib2.urlopen(req)
    return response.read()


def get_IP(url):
    html = url_open(url)
    c = re.compile(r"""
    (?:(?:[1]?\d?\d|
    2[0-4]\d|
    25[0-5]
    )\.){3}
    (?:[1]?\d?\d|
    2[0-4]\d|
    25[0-5]
    )
    """, re.VERBOSE)
    IPlist = c.findall(html)
    return IPlist

if __name__ == '__main__':
    for i in range(1,6):
        url = "http://www.kuaidaili.com/proxylist/%s/" % str(i)
        for each_ip in get_IP(url):
            print each_ip