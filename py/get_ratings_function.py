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

# Urls que voy a usar
link = "https://mishigeek.com/its-a-wonderful-kingdom-resena/"
link2 = "https://mishigeek.com/marco-polo-ii-resena/"
link3="https://mishigeek.com/race-for-the-galaxy-resena-en-espanol/"


# Capturo la cabecera de la petición HTTP
headers = requests.utils.default_headers()


links=[link, link2, link3]
# Modifico el User Agent para evitar el bloqueo
headers.update(
    {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
     }
 )

# Me conecto a la url con .get()
sitemap_soup = requests.get(link, headers=headers)
sitemap_soup.close()

# Se crea una función para obtener en forma de diccionario todas las valoraciones y datos sobre el juego de mesa:

def get_info(link):
    if (sitemap_soup.ok==True):
        
        soup = BeautifulSoup(sitemap_soup.text,features="html.parser")
        d= defaultdict(dict)
        key=[]   
        category=[]
        value=[]
        otros=[]
        pattern = r'-resena.*$'
        
        # Mediante los bucle for, se buscan todos los valores que coincida con el soup.select
        for each_part in soup.select('figure[class*="wp-block-table"]'):
            for each_part in soup.select('tr'):
                otros.append(each_part.get_text())
        split_items = (i.split(':') for i in otros[:8])
        category, value = zip(*split_items)
        category, value = map(list, (category, value))
        
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

        

