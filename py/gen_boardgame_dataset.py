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

#############################
## DEFINICIÓN DE FUNCIONES ##
#############################

def info2list(dict_review, csv_header):    
    '''
    We use this function to translate data obtained from get_ratings to a list,
    assigning each category found to the proper field in the final dataset.
    

    Parameters
    ----------
    dict_review : defaultdict
        Dictionary that contains the name of the boardgame and the categories
        extracted from scrapping the review.
    csv_header : list
        List that contains the name of the dataset fields to be filled from data
        in dict_review

    Returns
    -------
    list_review : list
        Data scrapped with get_ratings to list format according to headers defined
        by csv_header input list.
    exception : list
        Description of category and value that caused excpetion when execturing
        the function.

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
                'PVP recomendado':         'precio',
                'PvP Recomendado':         'precio',
                'PVP aproximado':          'precio',
                'PvP Desde':               'precio',
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
                'Autor':                   'diseño',
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
                'Calidad de Mecanicas':    'val_mec',
                'Calidad Mecánica':        'val_mec',
                'Nota de lectores':        'val_lec',
                'N. Votes':                'n_votos',
                'Conclusion':              'val_cual'}
     
    # Capturo el nombre del juego
    name = list(dict_review.keys())[0]    
    list_review[csv_header.index('nombre')] = name
    
    exception = []
    
    # Itero sobre el diccionarios obtenido por get_ratings
    values = list(dict_review.values())[0]
    for key in values.keys():
        # Utilizo try except para prevenir excepciones en la ejecución
        try:            
            # Asigno las categorías obtenidas del scrapping a los campos
            # según el diccionario csv_map.
            idx = csv_header.index(csv_map[key])
            list_review[idx] = values[key]
        
        except:
            # En caso de excepción imprimio el valor y retorno la excepción
            print(key, ':', values[key])       
            exception.append([key, values[key]])
    
    return list_review, exception

############################
## GENERACIÓN DEL DATASET ##
############################

# Obtener la lista de enlaces a reseñas y guardar en list
filename = "mishigeek_reviews.csv"

url_list = []

# Abro la lista de urls con reseñas y guardo en una lista
with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        url_list.append(row)

# Defino la cabecera del dataset
csv_header = ['nombre', 'n_jug', 'fecha', 'duracion', 'dureza', 'edad', 'precio',
              'genero', 'editorial', 'diseño', 'val_asp', 'val_inter', 'val_div',
              'val_var', 'val_rej', 'val_org', 'val_mec', 'val_lec', 'n_votos',
              'val_glob', 'val_cual']

# Itero sobre el url de cada resela para obtener el dataset en forma de list
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






 
 
 
 
 
