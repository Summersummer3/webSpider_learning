__author__ = 'summer'
import urllib2

response = urllib2.urlopen("http://www.fishc.com")
print type(response)
html = response.read()
print html