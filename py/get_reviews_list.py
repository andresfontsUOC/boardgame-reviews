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

# Guardaré la lista de enlaces en resena_list, así como el tipo de reseña
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
            main_soup = soup.find('div', {'id':'main'})
            for article in main_soup.find_all('article'):
                
                # Itero sobre todo hipervínculo dentro de 'article'
                for a in article.find_all('a', href=True):
                    href = a['href']
                    
                    # Filtro con aquellos que son reseñas
                    if (href.find('#') == -1) and (href.find("resena") != -1) and (href.find("resenas") == -1):
                        # Guardo tanto el url como el tipo de reseña
                        resena_list.append([href, review_type])
            
            # Cerrar la sesión
            page.close()        
            page_num = page_num + 1       

        # Si la página no existe pasar a siguiente reivew_type
        elif page.status_code == 404:
            print("Error 404. Page Not Found. URL " + page.url + "was NOT reached.")
            next_page = False
        
        else:
            print("URL " + page.url + "was NOT reached.")
            next_page = False        
    
# El resultado es una lista donde cada elemento consta de la url de la reseña
# así como el tipo de reseña (o conclusión cualitativa). Los tipos de reseña son
# 'juegaco', 'recomendad', etc, definidos en la lista review_type_list
resena_list = list(set(tuple(l) for l in resena_list))

# Imprimo el resultado
for k in set(resena_list):
    print(k)

# Guardo lista de links con reseña
with open('mishigeek_reviews.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    for link in resena_list:
        writer.writerow(link)
            


        

        
    
    
    


    