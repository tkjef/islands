import json
import sys
from pprint import pprint
from bs4 import BeautifulSoup
import urllib2
import socket

url_list={}
count=0

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


with open(sys.argv[1]) as data_file:
    data = json.load(data_file)

for i in data['list']:
    print(data["list"][i]["resolved_title"])
    print(data["list"][i]["resolved_url"])
    #url_list[data["list"][i]["resolved_title"]] = data["list"][i]["resolved_url"]

print(url_list)
