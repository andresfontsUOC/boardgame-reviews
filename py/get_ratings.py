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
import itertools


# Se crea una función para obtener en forma de diccionario todas las valoraciones y datos sobre el juego de mesa:
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

    # Si hay una conexión con el sitio web, se procede a la extracción de información.
    if (page.ok==True):
        
        # Se crea en formato de texto plano (sopa) la web introducida
        soup = BeautifulSoup(page.content.decode('utf-8'), features="html.parser")
        
        # Se crean variables para añadir los valores a filtrar.
        d = defaultdict(dict)
        category = []
        value = []
        otros = []
        pattern = r'-resena.*$'
        
        
        try:
            
            table = soup.find('figure', {'class':'wp-block-table'}).find('table')    
            
            for tr in table.select('tr'):
                otros.append(tr.get_text())
            # En la tabla, se obtienen los elementos.
            split_items = (i.split(':') for i in otros)
            category, value = zip(*split_items)
            category, value = map(list, (category, value))
            
            # Obtenemos el nombre del juego a partir del link
            nombre = re.sub(pattern, '', os.path.basename(link[:-1])).replace('-', ' ').title()
            #key.append(nombre) No necesitas esta línea
            category.append("Total")
            
            # Mediante los bucle for, se buscan todos los valores que coincida con el soup.select
            for each_part in soup.select('div[class*="lets-review-block lets-review-block__final-score"]'):
                    value.append(each_part.get_text())
                    
            for each_part in soup.select('div[class*="lets-review-block__crit__title lr-font-h"]'):
                    category.append(each_part.get_text())
                    
            for each_part in soup.select('div[class*="lets-review-block__crit__score"]'):
                    value.append(each_part.get_text())
            
            # Obtener la valoración cualitativa
            category.append("Conclusion")
            value.append(review[1])
       
            # Se crea el diccionario anidado a partir del nombre del juego, categoría y valor:
            for c,v in zip(category,value):
               d[nombre][c]=v
        
            
            # Las siguientes funciones tratan de splitear un valor dentro de otro.
            # Pasa de ser {'Nota de lectores10 Votos', "8.5"} a {'Nota de lectores': '8.5', 'N. Votes': '10 Votos'}
            
            def split_before_number(text):
                """Separará el texto en dos partes: antes del dígito y el resto."""
                def not_digit(c):
                    """Return True if character c is not a digit."""
                    return not c.isdigit()
                before = ''.join(itertools.takewhile(not_digit, text))
                after = ''.join(itertools.dropwhile(not_digit, text))
                return before, after
            
            def split_key_and_value(key, value):
                if not key.startswith("Nota"):
                    yield key, value
                    return
                key1, value2 = split_before_number(key)
                yield key1, value
                yield "N. Votes", value2
                
            def transform(dict_object):
                """Separará algunas claves y valores específicos y forma un nuevo dict."""
                new_dict_object = {}
                for original_key, original_value in dict_object.items():
                    for key, value in split_key_and_value(original_key, original_value):
                        new_dict_object[key] = value
                return new_dict_object
            
            # Se actualiza el diccionario
            d = {key: transform(value) for key, value in d.items()}
            
                
        # En caso de que no se haya podido conectar con la url, lanza el siguiente mensaje:
        except:
            print("Something when wrong with " + page.url)
        
        # Devuelve el diccionario creado por cada link
        return d            
