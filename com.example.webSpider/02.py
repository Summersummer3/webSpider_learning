__author__ = 'summer'
import urllib2

url = 'http://placekitten.com/g/500/600'

response = urllib2.urlopen(url)
print(response.info())
cat_img = response.read()

with open('cat_500_600.jpg','wb') as f:
    f.write(cat_img)
