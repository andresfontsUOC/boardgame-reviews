# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 21:57:56 2022

@author: fonts
"""

import random as rnd
import time
from collections import defaultdict
import csv

# Función ficticia get_info()
def get_info(url):
    print(url)
    time.sleep(0.02)
    
    category = ['Jugadores', 'Duración', 'Edad', 'Dureza', 'Precio', 'Género',
                'Editorial', 'Diseñador/a', 'Total', 'Aspecto / Componentes',
                'Interacción', 'Variabilidad', 'Originalidad', 'Mecánicas',
                'Conclusión']
    
    values = []
    for k in range(len(category)):
        values.append(rnd.randint(1,100))
    
    id_rnd = rnd.randint(1,10000)
    name = 'Juego_' + str(id_rnd)
    
    d = defaultdict(dict)
    for c,v in zip(category,values):
        d[name][c]=v
    
    return d

def info2list(dict_review, csv_header):
    
    list_review = [0] * len(csv_header)
    
    csv_map  = {'Jugadores':               'n_jug',    
                'Duración':                'duracion',
                'Dureza':                  'dureza',
                'Edad':                    'edad',   
                'Precio':                  'precio',
                 'Género':                 'genero',  
                'Editorial':               'editorial',
                 'Diseñador/a':            'diseño',
                'Total':                   'val_glob',
                'Aspecto / Componentes':   'val_asp',
                'Interacción':             'val_inter',
                'Variabilidad':            'val_var',
                'Originalidad':            'val_org', 
                'Mecánicas':               'val_mec', 
                'Conclusión':               'val_cual'}
     
    # Capturo el nombre del juego
    name = list(dict_review.keys())[0]    
    list_review[csv_header.index('nombre')] = name
    
    values = list(dict_review.values())[0]
    for key in values.keys():
        idx = csv_header.index(csv_map[key])
        list_review[idx] = values[key]
    
    return list_review

# Obtener la lista de enlaces a reseñas y guardar en list
filename = "mishigeek_reviews.csv"

f = open(filename)
url_list = f.readlines()[0].split(',')

f.close()

csv_header = ['nombre', 'n_jug', 'duracion', 'dureza', 'edad', 'precio',
              'genero', 'editorial', 'diseño', 'val_asp', 'val_inter',
              'val_var', 'val_org', 'val_mec', 'val_glob', 'val_cual']

# csv_map  = {'n_jug':'Jugadores',
#             'duracion':'Duración',
#             'dureza':'Dureza',
#             'edad':'Edad',
#             'precio':'Precio',
#             'genero': 'Género',
#             'editorial':'Editorial',
#             'diseño': 'Diseñador/a',
#             'val_glob':'Total',
#             'val_asp':'Aspecto / Componentes',
#             'val_inter':'Interacción',
#             'val_var':'Variabilidad',
#             'val_org':'Originalidad',
#             'val_mec':'Mecánicas',
#             'val_cual':'Conclusión'}

# Iterar sobre review_list
dataset = []

for url in url_list:    
    dataset.append(info2list(get_info(url), csv_header))

# Escribir el dataset a un archivo .csv
with open('boardgame_ranking.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(csv_header)
    
    for row in dataset:
        writer.writerow(row)




    






 
 
 
 
 
    
    




