#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:42:32 2024

@author: tzininga
"""

"""
storing data in Python
1. Lists
2. Dictionaries
3. Data Frames - speific to pandas
"""

import pandas
file = pandas.read_csv("country_data.csv")
print(file)

age1 = 30
age2 = 25
age3 = 29


age  = [30,25,28,46,22]
print(age)
print(age[0])
"""
30
"""

print(age[1])

print(min(age))

print(max(age))
print(sum(age))
print(len(age))


"""
[30.25.29.46,22]
"""
avg=sum(age)/len(age)
print(avg)
g1 = "M"
g2 = "F"
g3 =  "M"

Gender = ["M", "F", "F"]

print(Gender)

age.append(100)

print(age)




"""
Dictionaries - key:value pairs

cat "a cute animal"

"""
mammals = {"cat":"a cute animal","lion":"king of the jungle","elephant":"a gigantic herbivore"}

print(mammals["cat"])



"""

Data frames

"""
fruits = ["apple", "banana", "orange", "grape", "kiwi"]
size_nm = [9.8,10.1, 13.2, 8.7, 20.5]
fruit_sizes = {'fruits': fruits, 'size':size_nm}

"""df =dataframe
"""

import pandas as pd
df = pd.DataFrame(fruit_sizes)
print(df)

print(df['fruits'])

print(df['size'].min())
print(df['size'].mean())
print(df[df["size"]>10])

prices = [10.00, 12.50, 16.00, 23.00, 7.00]

df['prices'] = prices
df.drop(columns=["size"], inplace=True)










