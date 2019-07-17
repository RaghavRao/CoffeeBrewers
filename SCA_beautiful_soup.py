#!/usr/bin/python3
import urllib.request
from bs4 import BeautifulSoup as bs

HTML_FILE = urllib.request.urlopen('https://sca.coffee/certified-home-brewer')
OUTPUT_FILE = open('coffeelist.txt', 'w')
SOUP = bs(HTML_FILE, 'html.parser')
DIVS = SOUP.findAll("div", {"class": "image-slide-title"})
for div in DIVS:
    OUTPUT_FILE.write(div.text + '\n')
HTML_FILE.close()
OUTPUT_FILE.close()
