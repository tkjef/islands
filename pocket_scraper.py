from bs4 import BeautifulSoup
import urllib2
import sys
import socket

url_list=[]
count=0

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

with open(sys.argv[1]) as f:
    for line in f:
        url_list.append(line)

for url in url_list:
    count = count + 1
    
    req = urllib2.Request(url, headers=hdr)

    try:
        urllib2.urlopen(req, timeout = 12)
    except urllib2.URLError as e:
        continue
    
    try:
        page = urllib2.urlopen(req, timeout = 12)
    except urllib2.HTTPError, e:
        print e.fp.read()

    content = page.read()
    soup = BeautifulSoup(content,"lxml")
    if soup.title:
        title = soup.title.string
    else:
        title = url
    title_no_slash = title.replace("/","")
    title_no_colon = title_no_slash.replace(":","")
    title_no_question = title_no_colon.replace("?","")
    title_no_space = title_no_question.replace(" ","")
    title_no_left = title_no_space.replace("(","")
    title_no_right = title_no_left.replace(")","")
    title_no_excl = title_no_right.replace("!","")
    file = open(title_no_excl,"w")
    file.write(content)
    file.close()
    print(count)
