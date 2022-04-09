# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 17:33:06 2022

@author: fonts
"""
import requests
import re
from bs4 import BeautifulSoup
import os
from collections import defaultdict

def get_ratings(review):   

    link = review[0]
    print('Procesando:', link)

    # Capturo la cabecera de la petición HTTP
    headers = requests.utils.default_headers()

    # Modifico el User Agent para evitar el bloqueo
    headers.update(
        {
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
         }
    )

    # Me conecto a la url con .get()
    page = requests.get(link, headers=headers)
    page.close()

    # Se crea una función para obtener en forma de diccionario todas las valoraciones y datos sobre el juego de mesa:
    if (page.ok==True):
        
        soup = BeautifulSoup(page.content.decode('utf-8'), features="html.parser")
     
        d = defaultdict(dict)
        category = []
        value = []
        otros = []
        pattern = r'-resena.*$'
        
        try:
            # Mediante los bucle for, se buscan todos los valores que coincida con el soup.select
            table = soup.find('figure', {'class':'wp-block-table'}).find('table')    
            
            for tr in table.select('tr'):
                otros.append(tr.get_text())
                        
            split_items = (i.split(':') for i in otros)
            category, value = zip(*split_items)
            category, value = map(list, (category, value))
            
            nombre = re.sub(pattern, '', os.path.basename(link[:-1])).replace('-', ' ').title()
            #key.append(nombre) No necesitas esta línea
            category.append("Total")
            
            for each_part in soup.select('div[class*="lets-review-block lets-review-block__final-score"]'):
                    value.append(each_part.get_text())
                    
            for each_part in soup.select('div[class*="lets-review-block__crit__title lr-font-h"]'):
                    category.append(each_part.get_text())
                    
            for each_part in soup.select('div[class*="lets-review-block__crit__score"]'):
                    value.append(each_part.get_text())
            
            # Obtener la valoración cualitativa
            category.append("Conclusion")
            value.append(review[1])
        
            for c,v in zip(category,value):
                d[nombre][c]=v
        
        except:
            print("Something when wrong with " + page.url)
                
        return d            