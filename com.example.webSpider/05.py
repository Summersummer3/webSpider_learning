__author__ = 'summer'
import urllib2
import os
import time
import random
import httplib

def open_url(url):

    ip_list = ['111.23.10.8', '218.200.66.198', '124.88.67.14']

    proxy_support = urllib2.ProxyHandler({'http': random.choice(ip_list)})

    opener = urllib2.build_opener(proxy_support)
    opener.addheaders = \
        [('User-Agent',
          'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit'
          '/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36')]

    urllib2.install_opener(opener)
    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        html = response.read()
    except httplib.BadStatusLine:
        pass
    return html


def get_img_src(url):
    img_addrs = []
    html = open_url(url).decode('utf-8')
    print html
    start = html.find('img src=')
    while start != -1:
        start += 9
        end = html.find('.jpg', start, start+255)
        if end != -1:
            end += 4
            img_addrs.append(html[start:end])
        else:
            end = start
        start = html.find('img src=', end)
    return img_addrs

def save_img(img_addrs):
    img_name = ''
    for each_url in img_addrs:
        print each_url
        img_name = each_url.split('/')[-1]
        print img_name
        response = urllib2.urlopen(each_url)
        with open(img_name,'wb') as f:
            f.write(response.read())
            print "download 1 pic"

def download_pic(folder = 'img', pages = 10):

    os.mkdir(folder)
    os.chdir(folder)
    for page in range(1,pages):

        url = 'http://jandan.net/page/%s' % str(page)
        save_img(get_img_src(url))

if __name__ == '__main__':
    folder = str(time.time())
    download_pic(folder,2)

