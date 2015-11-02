# -*- coding: utf-8 -*-

# __author__ = 'summer'


c = 10
c += 10
print c

addr = 'http://tankr.net/s/custom/XTV4.jpg'

a = 'abc/abc/abc/abc'


start = a.find('abc')
while start != -1:
    end = a.find('/',start)
    print(a[start:end])
    start = a.find('abc',end)

import urllib2
response = urllib2.urlopen('http://img.tankr.net/s/custom/OUU8.jpg')
with open('test.jpg','wb') as f:
    f.write(response.read())

addr_1 = "http://www.shjaoiho.com"

try:
    urllib2.urlopen(addr_1)
except urllib2.URLError as e:
    print e.reason
print "你好"