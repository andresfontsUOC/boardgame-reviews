# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 17:48:02 2022

@author: fonts
"""

import requests
from bs4 import BeautifulSoup
from pprint import pprint
#from bs4 import BeautifulSoup

#uci_url = "https://archive.ics.uci.edu/ml/index.php"

# Defino las url que uso en este ejemplo
url = "https://mishigeek.com/churchill-resena-en-espanol-es-un-wargame/"
#sitemap = "https://mishigeek.com/sitemap.xml"

# Capturo la cabezera de la petición HTTP
headers = requests.utils.default_headers()

# Modifico el User Agent para evitar el bloqueo
headers.update(
    {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
     }
    )

# Petición a la url usando requests
page = requests.get(url, headers=headers)
page.close()
# Compruebo que la petición se ha resuelto OK
if page.ok:
    print("URL " + page.url + " was reached succesfully!")
    
# Imprimo el contendio de la url consultada con pprint (pretty print)
pprint(page.content)

soup = BeautifulSoup(page.content)
mydivs = soup.find_all("div", {"class": "lets-review-block__conclusion__title lets-review-block__title lr-font-h"})
