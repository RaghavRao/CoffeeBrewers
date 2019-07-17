#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from bs4 import BeautifulSoup as bs

f = open('certified-home-brewer', 'r')
g = open('coffeelist.txt', 'w')
soup = bs(f, 'html.parser')
mydivs = soup.findAll("div", {"class": "image-slide-title"})
for div in mydivs:
    g.write(div.text.encode('utf-8') + '\n')
f.close()
g.close()

