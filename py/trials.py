# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 17:48:02 2022

@author: fonts
"""

import requests
from bs4 import BeautifulSoup

uci_url = "https://archive.ics.uci.edu/ml/index.php"

url = "https://mishigeek.com"
sitemap = "https://mishigeek.com/sitemap.xml"


headers = requests.utils.default_headers()

headers.update(
    {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
     }
    )


page = requests.get(sitemap, headers=headers)

if page.ok:
    print("URL " + page.url + " was reached succesfully!")
    

