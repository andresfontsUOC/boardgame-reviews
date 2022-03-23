# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 18:51:55 2022

@author: fonts
"""

import requests
from bs4 import BeautifulSoup
import time
import csv


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
    
    # Cerrar la sesión
    sitemap_page.close()    
    
    # Capturar todos los enlaces del sitemap
    sitemap_all_urls = []
    for link in sitemap_soup.find_all('loc'):        
        
        link_page = requests.get(link.text, headers=headers)
        time.sleep(0.125) # Delay de 125 ms entre peticiones
        
        if link_page.ok:
            print("URL " + link_page.url + " was reached succesfully!")
            
            link_soup = BeautifulSoup(link_page.content)
            sitemap_all_urls.extend(link_soup.find_all('loc'))        
            
            # Cerrar sesión
            link_page.close()
        
        else:
            print("URL " + link_page.url + " was NOT reached.")

    print(sitemap_all_urls)

    
else:
    print("URL " + sitemap_page.url + "was NOT reached.")
    
# Guardo lista de links con reseña
with open('sitemap_reviews.csv', 'w') as f:
    writer = csv.writer(f, delimiter=",")
    
    for link in sitemap_all_urls:        
        print(link.text)
        link = link.text
        
        if (link.find("resena") != -1) and (link.find("resenas") == -1):
            writer.writerow([link])


