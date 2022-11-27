# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 12:40:42 2022

@author: Naveen
"""

import requests 
from bs4 import BeautifulSoup

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

headers = {'User-Agent':
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTMl, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

# Liga MX 21/22
page = "https://www.transfermarkt.us/liga-mx-apertura/transferstroeme/wettbewerb/MEXA/plus/0/galerie/0?saison_id=2021&zuab=zu&wid=&s_w=&leihe=0&leihe=1&intern=0&intern=1"

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

# LigaMX 20/21
page = "https://www.transfermarkt.us/liga-mx-apertura/transferstroeme/wettbewerb/MEXA/plus/0/galerie/0?saison_id=2020&zuab=zu&wid=&s_w=&leihe=0&leihe=1&intern=0&intern=1"

pageTree = requests.get(page, headers=headers)
 
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')



Values = pageSoup.find_all("td", {"class": "rechts hauptlink"})

ValuesList = []

for i in range (0,25):
    ValuesList.append(Values[i].text)

ligaMX20 = pd.DataFrame({"Values": ValuesList})
ligaMX20['Values'] = ligaMX20['Values'].str.replace('$', '')
ligaMX20['Values'] = ligaMX20['Values'].str.replace('m', '')
ligaMX20['Values'] = ligaMX20['Values'].str.replace('935Th.', '.935')
ligaMX20['Values'] = ligaMX20['Values'].str.replace('770Th.', '.77')
ligaMX20['Values'] = ligaMX20['Values'].str.replace('550Th.', '.55')
ligaMX20['Values'] = ligaMX20['Values'].str.replace('-', '0')
ligaMX20 = ligaMX20.astype({'Values':'float'})
ligaMX20 = ligaMX20.drop_duplicates(subset=['Values'])
totalMX20 = sum(ligaMX20['Values'])


# LigaMX 19/20
page = "https://www.transfermarkt.us/liga-mx-apertura/transferstroeme/wettbewerb/MEXA/plus/0/galerie/0?saison_id=2019&zuab=zu&wid=&s_w=&leihe=0&leihe=1&intern=0&intern=1"

pageTree = requests.get(page, headers=headers)
 
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')


Values = pageSoup.find_all("td", {"class": "rechts hauptlink"})

ValuesList = []

for i in range (0,25):
    ValuesList.append(Values[i].text)

MX19 = pd.DataFrame({"Values": ValuesList})
MX19['Values'] = MX19['Values'].str.replace('$', '')
MX19['Values'] = MX19['Values'].str.replace('m', '')
MX19['Values'] = MX19['Values'].str.replace('-', '0')
MX19 = MX19.astype({'Values':'float'})
MX19 = MX19.drop_duplicates(subset=['Values'])
MX19 = MX19.drop([1])
totalMX19 = sum(MX19['Values'])

# LigaMX 18/19
page = "https://www.transfermarkt.us/liga-mx-apertura/transferstroeme/wettbewerb/MEXA/plus/0/galerie/0?saison_id=2019&zuab=zu&wid=&s_w=&leihe=0&leihe=1&intern=0&intern=1"

pageTree = requests.get(page, headers=headers)
 
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')


Values = pageSoup.find_all("td", {"class": "rechts hauptlink"})

ValuesList = []

for i in range (0,25):
    ValuesList.append(Values[i].text)

MX18 = pd.DataFrame({"Values": ValuesList})
MX18['Values'] = MX18['Values'].str.replace('$', '')
MX18['Values'] = MX18['Values'].str.replace('m', '')
MX18['Values'] = MX18['Values'].str.replace('220Th.', '.22')
MX18['Values'] = MX18['Values'].str.replace('-', '0')
MX18 = MX18.astype({'Values':'float'})
MX18 = MX18.drop_duplicates(subset=['Values'])
totalMX18 = sum(MX18['Values'])


# LigaMX 17/18
page = "https://www.transfermarkt.us/liga-mx-apertura/transferstroeme/wettbewerb/MEXA/plus/0/galerie/0?saison_id=2017&zuab=zu&wid=&s_w=&leihe=0&leihe=1&intern=0&intern=1"

pageTree = requests.get(page, headers=headers)
 
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')


Values = pageSoup.find_all("td", {"class": "rechts hauptlink"})

ValuesList = []

for i in range (0,25):
    ValuesList.append(Values[i].text)

MX17 = pd.DataFrame({"Values": ValuesList})
MX17['Values'] = MX17['Values'].str.replace('$', '')
MX17['Values'] = MX17['Values'].str.replace('m', '')
MX17['Values'] = MX17['Values'].str.replace('957Th.', '.957')
MX17['Values'] = MX17['Values'].str.replace('908Th.', '.908')
MX17['Values'] = MX17['Values'].str.replace('880Th.', '.880')
MX17['Values'] = MX17['Values'].str.replace('275Th.', '.275')
MX17['Values'] = MX17['Values'].str.replace('-', '0')
MX17 = MX17.astype({'Values':'float'})
MX17 = MX17.drop_duplicates(subset=['Values'])
totalMX17 = sum(MX17['Values'])

# MLS All Years
page = "https://www.transfermarkt.us/major-league-soccer/transferbilanz/wettbewerb/MLS1"

pageTree = requests.get(page, headers=headers)
 
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')


Values = pageSoup.find_all("td", {"class": "rechts hauptlink redtext"})

ValuesList = []

for i in range (0,10):
    ValuesList.append(Values[i].text)

mls = pd.DataFrame({"Values": ValuesList})
mls['Values'] = mls['Values'].str.replace('$', '')
mls['Values'] = mls['Values'].str.replace('m', '')
mls['Values'] = mls['Values'].str.replace('-', '0')
mls = mls.astype({'Values':'float'})

MLS = [mls['Values'][6], mls['Values'][5], mls['Values'][4], mls['Values'][3], mls['Values'][2]]


# Championship All Years
page = "https://www.transfermarkt.us/championship/transferbilanz/wettbewerb/GB2"

pageTree = requests.get(page, headers=headers)
 
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')


Values = pageSoup.find_all("td", {"class": "rechts hauptlink redtext"})

ValuesList = []

for i in range (0,25):
    ValuesList.append(Values[i].text)

champ = pd.DataFrame({"Values": ValuesList})
champ['Values'] = champ['Values'].str.replace('$', '')
champ['Values'] = champ['Values'].str.replace('m', '')
champ['Values'] = champ['Values'].str.replace('-', '0')
champ = champ.astype({'Values':'float'})

Championship = [champ['Values'][6], champ['Values'][5], champ['Values'][4], champ['Values'][3], champ['Values'][2]]
ligaMX = [totalMX17, totalMX18, totalMX19, totalMX20, totalMX]
date = [2017, 2018, 2019, 2020, 2021]
plt.plot(date, ligaMX, color = 'green', label = 'Liga MX', linewidth = 3)
plt.plot(date, MLS, color = 'blue', label = 'MLS', linewidth = 3)
plt.fill_between(date, ligaMX, MLS, color='black', alpha=0.4)
plt.plot(date, Championship, color = 'red', label = 'English Championship', linewidth = 3)
plt.fill_between(date, Championship, MLS, color='black', alpha=0.4)
plt.xticks([2017, 2018,2019,2020,2021], ['2017', '2018', '2019', '2020', '2021'])
plt.legend(loc = 'upper right')
plt.title('Liga MX vs MLS vs Championship Transfers (Last Five Years)')
plt.xlabel('Years')
plt.ylabel('Transfers Each Year (in Millions)')
ymax = max(Championship)
diff = np.arange(0,5)
# for i in range(4): 
  # diff[i] = MLS[i] - ligaMX[i]
   # plt.text(i, (abs(MLS[i] - ligaMX[i])/2), diff[i], color = 'white')
plt.show



