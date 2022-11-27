# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 23:44:33 2022

@author: Naveen
"""

import os
import pandas as pd 
import numpy as np 
import calendar 
import matplotlib.pyplot as plt 
import imageio 

winger = pd.read_csv("My Player Grades/Player Grades for Each Game - Wingers (6).csv")
st = pd.read_csv("My Player Grades/Player Grades for Each Game - CF's (6).csv")
st['Date'] = st['Date'].replace('/', '', regex=True)
winger['Date'] = winger['Date'].replace('/', '', regex=True)
tuiloma = st.loc[st['Match'] == 'Jaroslaw Niezgoda']
zuparic = winger.loc[winger['Match'] == 'Marvin Loria']
blanco = winger.loc[winger['Match'] == 'Santiago Moreno']
chara = winger.loc[winger['Match'] == 'Yimmi Chara']
asprilla = winger.loc[winger['Match'] == 'Dairon Asprilla']

# Getting the two games that we want
update_zuparic = zuparic.loc[zuparic['Date'] == ('6302022')]
update_zuparic = update_zuparic.append(zuparic.loc[zuparic['Date'] == ('742022')])
update_zuparic = update_zuparic.append(zuparic.loc[zuparic['Date'] == ('792022')])
update_zuparic = update_zuparic.append(zuparic.loc[zuparic['Date'] == ('7182022')])
update_zuparic = update_zuparic.append(zuparic.loc[zuparic['Date'] == ('7242022')])
update_tuiloma = tuiloma.loc[tuiloma['Date'] == ('6302022')]
update_tuiloma = update_tuiloma.append(tuiloma.loc[tuiloma['Date'] == ('742022')])
update_tuiloma = update_tuiloma.append(tuiloma.loc[tuiloma['Date'] == ('792022')])
update_tuiloma = update_tuiloma.append(tuiloma.loc[tuiloma['Date'] == ('7182022')])
update_tuiloma = update_tuiloma.append(tuiloma.loc[tuiloma['Date'] == ('7242022')])
update_blanco = blanco.loc[blanco['Date'] == ('6302022')]
update_blanco = update_blanco.append(blanco.loc[blanco['Date'] == ('742022')])
update_blanco = update_blanco.append(blanco.loc[blanco['Date'] == ('792022')])
update_blanco = update_blanco.append(blanco.loc[blanco['Date'] == ('7182022')])
update_blanco = update_blanco.append(blanco.loc[blanco['Date'] == ('7242022')])
update_chara = chara.loc[chara['Date'] == ('6302022')]
update_chara = update_chara.append(chara.loc[chara['Date'] == ('742022')])
update_chara = update_chara.append(chara.loc[chara['Date'] == ('792022')])
update_chara = update_chara.append(chara.loc[chara['Date'] == ('7182022')])
update_chara = update_chara.append(chara.loc[chara['Date'] == ('7242022')])
update_asprilla = asprilla.loc[asprilla['Date'] == ('6302022')]
update_asprilla = update_asprilla.append(asprilla.loc[asprilla['Date'] == ('742022')])
update_asprilla = update_asprilla.append(asprilla.loc[asprilla['Date'] == ('792022')])
update_asprilla = update_asprilla.append(asprilla.loc[asprilla['Date'] == ('7182022')])
update_asprilla = update_asprilla.append(asprilla.loc[asprilla['Date'] == ('7242022')])


adj_gradet = [float(x) for x in update_tuiloma['ADJUSTED GRADE']]
adj_gradez = [float(x) for x in update_zuparic['ADJ GRADE']]
adj_gradeb = [float(x) for x in update_blanco['ADJ GRADE']]
adj_gradec = [float(x) for x in update_chara['ADJ GRADE']]
adj_gradea = [float(x) for x in update_asprilla['ADJ GRADE']]


datet = [1, 2, 3, 4, 5]
datez = [4, 5]
dateb = [1, 2, 3, 4, 5]
datec = [1, 2, 3, 4, 5]
datea = [1, 2, 5]


# All Players but emphasis on Tuiloma
i = 0
plt.plot(datet, adj_gradet, color = '#D69A00', linewidth = 4, marker = '.', markeredgewidth = 6)
plt.plot(datez, adj_gradez, color = 'k')
plt.plot(dateb, adj_gradeb, color = 'k')
plt.plot(datec, adj_gradec, color = 'k')
plt.plot(datea, adj_gradea, color = 'k')
for x,y in zip(datet,adj_gradet):

    label = adj_gradet[i]

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center',
                 color = '#D69A00',
                 fontweight=500)
    i = i + 1
plt.title('Jaroslaw Niezgoda Last Five Games', color = "#D69A00", fontweight=600)
plt.xlabel('Date', fontweight=300, color = "#D69A00")
plt.ylabel('Adjustment Grade', fontweight=300, color = "#D69A00")
plt.xticks([1, 2, 3, 4, 5], ['6/29', '7/3', '7/9', '7/17', '7/23'])
plt.savefig('Tuiloma.png')
plt.show()

# All Players but emphasis on Zuparic
i = 0
plt.plot(datet, adj_gradet, color = 'k')
plt.plot(dateb, adj_gradeb, color = 'k')
plt.plot(datec, adj_gradec, color = 'k')
plt.plot(datez, adj_gradez, color = '#00482B', linewidth = 4, marker = '.', markeredgewidth = 6)
plt.plot(datea, adj_gradea, color = 'k')
for x,y in zip(datez,adj_gradez):

    label = adj_gradez[i]

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center',
                 color = '#00472B', 
                 fontweight=500)
    i = i + 1
plt.title('Marvin Loria Last Two Games', color = "#00482B", fontweight=600)
plt.xticks([1, 2, 3, 4, 5], ['6/29', '7/3', '7/9', '7/17', '7/23'])
plt.xlabel('Date', fontweight=300, color = "#00482B")
plt.ylabel('Adjustment Grade', fontweight=300, color = "#00482B")
plt.savefig('Zuparic.png')
plt.show()

# All Players but emphasis on Chara
i = 0
plt.plot(datet, adj_gradet, color = 'k')
plt.plot(dateb, adj_gradeb, color = 'k')
plt.plot(datec, adj_gradec, color = '#D69A00', linewidth = 4, marker = '.', markeredgewidth = 6)
plt.plot(datez, adj_gradez, color = 'k')
plt.plot(datea, adj_gradea, color = 'k')
for x,y in zip(datec,adj_gradec):

    label = adj_gradec[i]

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center',
                 color = '#D69A00', 
                 fontweight=500)
    i = i + 1
plt.title('Yimmi Chara Last Five Games', color = "#D69A00", fontweight=600)
plt.xticks([1, 2, 3, 4, 5], ['6/29', '7/3', '7/9', '7/17', '7/23'])
plt.xlabel('Date', fontweight=300, color = "#D69A00")
plt.ylabel('Adjustment Grade', fontweight=300, color = "#D69A00")
plt.savefig('Blanco.png')
plt.show()

# All Players but emphasis on Asprilla
i = 0
plt.plot(datet, adj_gradet, color = 'k')
plt.plot(dateb, adj_gradeb, color = 'k')
plt.plot(datec, adj_gradec, color = 'k')
plt.plot(datez, adj_gradez, color = 'k')
plt.plot(datea, adj_gradea, color = '#00482B', linewidth = 4, marker = '.', markeredgewidth = 6)
for x,y in zip(datea,adj_gradea):

    label = adj_gradea[i]

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center',
                 color = '#00482B', 
                 fontweight=500)
    i = i + 1
plt.title('Dairon Asprilla Last Three Games', color = "#00482B", fontweight=600)
plt.xticks([1, 2, 3, 4, 5], ['6/29', '7/3', '7/9', '7/17', '7/23'])
plt.xlabel('Date', fontweight=300, color = "#00482B")
plt.ylabel('Adjustment Grade', fontweight=300, color = "#00482B")
plt.savefig('Asprilla.png')
plt.show()

# All Players but emphasis on Moreno
i = 0
plt.plot(datet, adj_gradet, color = 'k')
plt.plot(dateb, adj_gradeb, color = '#D69A00', linewidth = 4, marker = '.', markeredgewidth = 6)
plt.plot(datec, adj_gradec, color = 'k')
plt.plot(datez, adj_gradez, color = 'k')
plt.plot(datea, adj_gradea, color = 'k')
for x,y in zip(dateb,adj_gradeb):

    label = adj_gradeb[i]

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center',
                 color = '#D69A00', 
                 fontweight=500)
    i = i + 1
plt.title('Santiago Moreno Last Five Games', color = "#D69A00", fontweight=600)
plt.xticks([1, 2, 3, 4, 5], ['6/29', '7/3', '7/9', '7/17', '7/23'])
plt.xlabel('Date', fontweight=300, color = "#D69A00")
plt.ylabel('Adjustment Grade', fontweight=300, color = "#D69A00")
plt.savefig('Chara.png')
plt.show()




with imageio.get_writer('timberattackersgif.gif', mode='I') as writer:
    for y in range (0, 30):
        image = imageio.imread('Tuiloma.png')
        writer.append_data(image)
        y = y + 1
    for x in range (0, 30):
        image = imageio.imread('Zuparic.png')
        writer.append_data(image)
        x = x + 1
    for z in range (0, 30):
        image = imageio.imread('Blanco.png')
        writer.append_data(image)
        z = z + 1
    for g in range (0, 30):
        image = imageio.imread('Asprilla.png')
        writer.append_data(image)
        g = g + 1
    for h in range (0, 30):
        image = imageio.imread('Chara.png')
        writer.append_data(image)
        h = h + 1

