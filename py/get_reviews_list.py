# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 18:51:55 2022

@author: fonts
"""

import requests
from bs4 import BeautifulSoup


# Defino la url del sitemap
sitemap = "https://mishigeek.com/sitemap.xml"

# Capturo la cabezera de la petición HTTP
headers = requests.utils.default_headers()

# Modifico el User Agent para evitar el bloqueo
headers.update(
    {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
     }
    )

# Petición a la url usando requests
sitemap_page = requests.get(sitemap, headers=headers)

# Compruebo que la petición se ha resuelto OK
if sitemap_page.ok:
    print("URL " + sitemap_page.url + " was reached succesfully!")
    

sitemap_soup = BeautifulSoup(sitemap_page.content)
print(sitemap_soup.prettify())

# Obtengo todos los enlaces del sitemap
sitemap_list = sitemap_soup.find_all('loc')