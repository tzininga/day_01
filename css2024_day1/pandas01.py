#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:30:26 2024

@author: tzininga
"""

import pandas
file = pandas.read_csv("country_data.csv")
print(file)

print(file.info())
print(file.describe())

file = pandas.read_csv("diab_data.csv")
print(file) 
print(file.info())
print(file.describe())

file = pandas.read_csv("iris.csv")
print(file)
print(file.info())
print(file.describe())

file = pandas.read_csv("insurance_data.csv",skiprows=5)

file = pandas.read_csv("diab_data.csv")

file = pandas.read_csv("housing_data.csv")
print(file)

               


file = pandas.read_csv("movie_dataset.csv")
print(file)
print(file.info())
print(file.describe())
