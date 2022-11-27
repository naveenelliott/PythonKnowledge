# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 17:39:25 2022

@author: Naveen
"""

import requests 
from bs4 import BeautifulSoup

import pandas as pd
import matplotlib.pyplot as plt

headers = {'User-Agent':
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTMl, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
# MLS 21/22
page = "https://www.transfermarkt.us/major-league-soccer/transferstroeme/wettbewerb/MLS1/saison_id/2021/zuab/zu/wid//leihe/1/intern/1/s_w//plus/1"

pageTree = requests.get(page, headers=headers)
 
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')



Values = pageSoup.find_all("td", {"class": "rechts hauptlink"})

ValuesList = []
ValuesList2 = []

for i in range (0,25):
    ValuesList.append(Values[i].text)

df = pd.DataFrame({"Values": ValuesList})
df['Values'] = df['Values'].str.replace('$', '')
df['More Values'] = df['More Values'].str.replace('$', '')
df['Values'] = df['Values'].str.replace('m', '')
df['More Values'] = df['More Values'].str.replace('m', '')
df['More Values'] = df['More Values'].str.replace('1,000Th.', '1.0')
df['More Values'] = df['More Values'].str.replace('800Th.', '0.8')
df['More Values'] = df['More Values'].str.replace('550Th.', '0.55')
df['More Values'] = df['More Values'].str.replace('500Th.', '0.5')
df['More Values'] = df['More Values'].str.replace('400Th.', '0.4')
df['More Values'] = df['More Values'].str.replace('250Th.', '0.25')
df['More Values'] = df['More Values'].str.replace('175Th.', '0.175')
df['More Values'] = df['More Values'].str.replace('-', '0')
df = df.astype({'Values':'float'})
df = df.astype({'More Values':'float'})
df = df.drop_duplicates(subset=['Values'])
totalMLS = sum(df['Values'] + df['More Values'])

# Liga MX 21/22
page = "https://www.transfermarkt.us/liga-mx-apertura/transferstroeme/wettbewerb/MEXA"

pageTree = requests.get(page, headers=headers)
 
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')



Values = pageSoup.find_all("td", {"class": "rechts hauptlink"})

ValuesList = []

for i in range (0,25):
    ValuesList.append(Values[i].text)

ligaMX = pd.DataFrame({"Values": ValuesList})
ligaMX['Values'] = ligaMX['Values'].str.replace('$', '')
ligaMX['Values'] = ligaMX['Values'].str.replace('m', '')
ligaMX['Values'] = ligaMX['Values'].str.replace('990Th.', '.99')
ligaMX['Values'] = ligaMX['Values'].str.replace('935Th.', '.935')
ligaMX['Values'] = ligaMX['Values'].str.replace('880Th.', '.88')
ligaMX['Values'] = ligaMX['Values'].str.replace('715Th.', '.715')
ligaMX['Values'] = ligaMX['Values'].str.replace('660Th.', '.66')
ligaMX['Values'] = ligaMX['Values'].str.replace('-', '0')
ligaMX = ligaMX.astype({'Values':'float'})
ligaMX = ligaMX.drop_duplicates(subset=['Values'])
totalMX = sum(ligaMX['Values'])
