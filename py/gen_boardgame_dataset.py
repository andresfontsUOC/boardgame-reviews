# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 21:57:56 2022

@author: fonts
"""

import csv

# Obtener la lista de enlaces a reseñas y guardar en list
filename = "mishigeek_reviews.csv"

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
