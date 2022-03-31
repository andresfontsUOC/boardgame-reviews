# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 18:51:55 2022

@author: fonts
"""

import requests
from bs4 import BeautifulSoup
import time
import csv


# Defino la url 
template_url = "https://mishigeek.com/category/resenas/<review_type>/page/<page_num>/"

review_type_list = [
    "juegaco",
    "buen-juego",
    "recomendado",
    "aprobado",
    "suspenso"]    

# Capturo la cabezera de la petición HTTP
headers = requests.utils.default_headers()

# Modifico el User Agent para evitar el bloqueo
headers.update(
    {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
     }
    )

# Guardaré la lista de enlaces en resena_list
resena_list = []

for review_type in review_type_list:    
    # Empiezo buscando en la page /1
    page_num = 1
    next_page = True
    
    while next_page:
        
        # Petición a la url usando requests
        url = template_url.replace("<review_type>", review_type).replace("<page_num>", str(page_num))
        print(url)
        
        page = requests.get(url, headers=headers)
        
        # Compruebo que la petición se ha resuelto OK
        if page.ok:
            print("URL " + page.url + " was reached succesfully!\n")
            soup = BeautifulSoup(page.content)        
            
            # Itero sobre los elementos 'article'
            for article in soup.find_all('article'):
                
                # Itero sobre todo hipervínculo dentro de 'article'
                for a in article.find_all('a', href=True):
                    href = a['href']
                    
                    # Filtro con aquellos que son reseñas
                    if (href.find('#') == -1) and (href.find("-resena") != -1):                
                        resena_list.append(href)
            
            # Cerrar la sesión
            page.close()        
            page_num = page_num + 1       

        # TODO hacer un ifelse para 404 not found            
        else:
            print("URL " + page.url + "was NOT reached.")
            next_page = False
        
# Imprimo el resultado
for k in set(resena_list):
    print(k)

# Guardo como string separado por comas
resena_csv = ','.join(set(resena_list))

# Guardo lista de links con reseña
with open('mishigeek_reviews.csv', 'w') as f:
    f.write(resena_csv)
            


        

        
    
    
    


    