# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 21:57:56 2022

@author: fonts
"""

import random as rnd
import time
from collections import defaultdict
import csv
from get_ratings import get_ratings

# Función ficticia get_info()
# def get_info(url):
#     print(url)
#     time.sleep(0.02)
    
#     category = ['Jugadores', 'Duración', 'Edad', 'Dureza', 'Precio', 'Género',
#                 'Editorial', 'Diseñador/a', 'Total', 'Aspecto / Componentes',
#                 'Interacción', 'Variabilidad', 'Originalidad', 'Mecánicas',
#                 'Conclusión']
    
#     values = []
#     for k in range(len(category)):
#         values.append(rnd.randint(1,100))
    
#     id_rnd = rnd.randint(1,10000)
#     name = 'Juego_' + str(id_rnd)
    
#     d = defaultdict(dict)
#     for c,v in zip(category,values):
#         d[name][c]=v
    
#     return d

def info2list(dict_review, csv_header):
    '''
    

    Parameters
    ----------
    dict_review : TYPE
        DESCRIPTION.
    csv_header : TYPE
        DESCRIPTION.

    Returns
    -------
    list_review : TYPE
        DESCRIPTION.
    exception : TYPE
        DESCRIPTION.

    '''
    
    list_review = [0] * len(csv_header)
    
    csv_map  = {'Jugadores':               'n_jug',
                'Número de jugadores':     'n_jug',
                'Jugadores/as':            'n_jug',
                'Fecha':                   'fecha',
                'Duración':                'duracion',
                'Duración aproximada del juego':  'duracion',
                'Duración aproximada':     'duracion',
                'Dureza':                  'dureza',
                'Edad':                    'edad',
                'Edad mínima':             'edad',
                'Edad mínima recomendada': 'edad',
                'Precio':                  'precio',
                'PVP Recomendado':         'precio',
                'PVP aproximado':          'precio',
                'PVP':                     'precio',
                'Precio Recomendado':      'precio',
                'Género':                  'genero',
                'Genero/mecánicas':        'genero',
                'Genero / Mecánicas':      'genero',
                'Género / Mecánicas':      'genero',
                'Editorial':               'editorial',
                'Editorial/Distribuidora': 'editorial',
                'Diseñador/a':             'diseño',
                'Autor/a':                 'diseño',
                'Total':                   'val_glob',
                'Aspecto / Componentes':   'val_asp',
                'Interacción':             'val_inter',
                'Diversión':               'val_div',
                'Variabilidad':            'val_var',
                'Rejugabilidad':           'val_rej',
                'Originalidad':            'val_org', 
                'Mecánicas':               'val_mec',
                'Calidad de mecánicas':    'val_mec',
                'Calidad de Mecánicas':    'val_mec',
                'Calidad Mecánica':        'val_mec',
                'Conclusion':              'val_cual'}
     
    # Capturo el nombre del juego
    name = list(dict_review.keys())[0]    
    list_review[csv_header.index('nombre')] = name
    
    exception = []
    
    values = list(dict_review.values())[0]
    for key in values.keys():
        try:            
            idx = csv_header.index(csv_map[key])
            list_review[idx] = values[key]
        except:
            print(key, ':', values[key])       
            exception.append([key, values[key]])
    
    return list_review, exception

# Obtener la lista de enlaces a reseñas y guardar en list
filename = "mishigeek_reviews.csv"
#filename = "mishigeek_reviews_test.csv"

url_list = []

with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        url_list.append(row)

csv_header = ['nombre', 'n_jug', 'fecha', 'duracion', 'dureza', 'edad', 'precio',
              'genero', 'editorial', 'diseño', 'val_asp', 'val_inter', 'val_div',
              'val_var', 'val_rej', 'val_org', 'val_mec', 'val_glob', 'val_cual']

# Iterar sobre review_list
dataset = []
exceptions = []

for url in url_list:
    try:
        list_review, exception = info2list(get_ratings(url), csv_header)
        dataset.append(list_review)
        exceptions.append(exception)
    except:
        print('No se ha analizado: ', url[0])

# Escribir el dataset a un archivo .csv
with open('boardgame_ranking.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(csv_header)
    
    for row in dataset:
        writer.writerow(row)

print(dataset)
print(exceptions)




    






 
 
 
 
 
