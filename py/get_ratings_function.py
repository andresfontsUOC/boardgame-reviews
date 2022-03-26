# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 12:51:45 2022

@author: ignac
"""


import requests
from bs4 import BeautifulSoup

# Url que voy a usar
link = "https://mishigeek.com/its-a-wonderful-kingdom-resena/"

# Evitar bloqueo
# Capturo la cabezera de la petición HTTP
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

if (page.ok==True):
    print("OK")
    
    
    
else:
    print("Conexión sin éxito")
        
        

