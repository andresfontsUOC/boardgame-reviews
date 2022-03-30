# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 12:51:45 2022

@author: ignac
"""


import requests
import re
from bs4 import BeautifulSoup
import os
from collections import defaultdict
# Url que voy a usar
link3 = "https://mishigeek.com/its-a-wonderful-kingdom-resena/"
link2 = "https://mishigeek.com/marco-polo-ii-resena/"
link="https://mishigeek.com/race-for-the-galaxy-resena-en-espanol/"
# Capturo la cabecera de la petición HTTP
headers = requests.utils.default_headers()

# Modifico el User Agent para evitar el bloqueo
headers.update(
    {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
     }
 )

# Me conecto a la url con .get()
sitemap_soup = requests.get(link, headers=headers)
sitemap_soup.close()

if (sitemap_soup.ok==True):
    
    soup = BeautifulSoup(sitemap_soup.text,features="html.parser")
    d= defaultdict(dict)
    key=[]   
    category=[]
    value=[]
    pattern = r'-resena.*$'
    
    nombre = re.sub(pattern,'',os.path.basename(link[:-1])).replace('-', ' ').title()
    key.append(nombre)
    category.append("Total") 
    for each_part in soup.select('div[class*="lets-review-block lets-review-block__final-score"]'):
            value.append(each_part.get_text())
    for each_part in soup.select('div[class*="lets-review-block__crit__title lr-font-h"]'):
            category.append(each_part.get_text())
    for each_part in soup.select('div[class*="lets-review-block__crit__score"]'):
            value.append(each_part.get_text())
    
    
    
    
    for k in key:
       for c,v in zip(category,value):
           d[k][c]=v
    
    print(d)

        
        

