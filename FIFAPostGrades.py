# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 14:46:53 2022

@author: Naveen
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json
from mplsoccer import Pitch
from matplotlib.offsetbox import OffsetImage, AnnotationBbox



#Draw the pitch
pitch = Pitch(# axis=True, label=True, tick=True, 
              pitch_color='grass', line_color='white')
(fig,ax) = pitch.draw()

df = pd.DataFrame()
cam = pd.read_csv("My Player Grades/Player Grades for Each Game - CAM's (6).csv")
gk = pd.read_csv("My Player Grades/Player Grades for Each Game - GK's (7).csv")
winger = pd.read_csv("My Player Grades/Player Grades for Each Game - Wingers (8).csv")
st = pd.read_csv("My Player Grades/Player Grades for Each Game - CF's (8).csv")
cam['Date'] = cam['Date'].replace('-', '', regex=True)
st['Date'] = st['Date'].replace('/', '', regex=True)
winger['Date'] = winger['Date'].replace('/', '', regex=True)
tuiloma = st.loc[st['Match'] == 'Dairon Asprilla']
zuparic = cam.loc[cam['Match'] == 'Sebastian Blanco']
gk['Date'] = gk['Date'].replace('/', '', regex=True)
ivacic = gk.loc[gk['Match'] == 'Aljaz Ivacic']
blanco = winger.loc[winger['Match'] == 'Yimmi Chara']
chara = winger.loc[winger['Match'] == 'Santiago Moreno']
fb = pd.read_csv("My Player Grades/Player Grades for Each Game - LB_RB's (12).csv")
cb = pd.read_csv("My Player Grades/Player Grades for Each Game - CB's (9).csv")
fb.head()
cb.head() 
fb['Date'] = fb['Date'].replace('/', '', regex=True)
cb['Date'] = cb['Date'].replace('/', '', regex=True)
mabiala = cb.loc[cb['Unnamed: 0'] == 'Zac McGraw']
dario = cb.loc[cb['Unnamed: 0'] == 'Dario Zuparic']
van_rankin = fb.loc[fb['Match'] == 'Bill Tuiloma']
bravo = fb.loc[fb['Match'] == 'Claudio Bravo']
# cdm = pd.read_csv("My Player Grades/Player Grades for Each Game - CDM's (6).csv")
cm = pd.read_csv("My Player Grades/Player Grades for Each Game - CM's (10).csv")
cm['Date'] = cm['Date'].replace('/', '', regex=True)
williamson = cm.loc[cm['Match'] == 'Eryk Williamson']
dchara = cm.loc[cm['Match'] == 'Diego Chara']


# Getting the two games that we want
update_zuparic = zuparic.loc[zuparic['Date'] == ('20220827')]
update_tuiloma = tuiloma.loc[tuiloma['Date'] == ('8272022')]
update_blanco = blanco.loc[blanco['Date'] == ('8272022')]
update_chara = chara.loc[chara['Date'] == ('8272022')]
update_mabiala = mabiala.loc[mabiala['Date'] == ('8272022')]
update_dario = dario.loc[dario['Date'] == ('8272022')]
update_van_rankin = van_rankin.loc[van_rankin['Date'] == ('8272022')]
update_bravo = bravo.loc[bravo['Date'] == ('8272022')]
update_williamson = williamson.loc[williamson['Date'] == ('8272022')]
update_dchara = dchara.loc[dchara['Date'] == ('8272022')]
update_ivacic = ivacic.loc[ivacic['Date'] == ('8272022')]


# Getting the adjusted grades
tui_adj = [float(x) for x in update_tuiloma['ADJUSTED GRADE']]
zup_adj = [float(x) for x in update_zuparic['ADJ GRADE']]
mab_adj = [float(x) for x in update_mabiala['ADJ GRADE']]
dar_adj = [float(x) for x in update_dario['ADJ GRADE']]
bla_adj = [float(x) for x in update_blanco['ADJ GRADE']]
cha_adj = [float(x) for x in update_chara['ADJ GRADE']]
van_adj = [float(x) for x in update_van_rankin['ADJ GRADE']]
bra_adj = [float(x) for x in update_bravo['ADJ GRADE']]
wil_adj = [float(x) for x in update_williamson['ADJ GRADE']]
dch_adj = [float(x) for x in update_dchara['ADJ GRADE']]
iva_adj = [float(x) for x in update_ivacic['Adjustment Grade']]


df['Adjusted Grade'] = [tui_adj, zup_adj, bla_adj, cha_adj, mab_adj, dar_adj, 
                        van_adj, bra_adj, wil_adj, dch_adj, iva_adj]

df['Player Name'] = ['Asprilla', 'Blanco', 'Y. Chara', 'Moreno', 
                     'McGraw', 'Zuparic', 'Tuiloma', 'Bravo', 
                     'Williamson', 'D. Chara', 'Ivacic']


df['path'] = ['Asprilla.png', 'Blanco.png', 'yimmi.png', 'Santiago Moreno.png', 'mcGraw.png', 
              'dario zuparic.png', 'tuiloma.png', 'bravo.png', 'Williamson.png', 'diego.png', 'ivacic.png'
              ]
# Plot badges
def getImage(path):
    return OffsetImage(plt.imread(path), zoom=.05, alpha = 1)

ab = AnnotationBbox(getImage('Timbers Headshots/'+df['path'][0]), (105, 40), frameon=False)
ax.add_artist(ab)
plt.text(100, 47, df['Player Name'][0], color = '#d0e0da', size = 8)
plt.text(100, 51, df['Adjusted Grade'][0], color = '#0a3222', size = 9, fontweight = 'bold')


ab = AnnotationBbox(getImage('Timbers Headshots/'+df['path'][1]), (85, 40), frameon=False)
ax.add_artist(ab)
plt.text(80, 47, df['Player Name'][1], color = '#d0e0da', size = 8)
plt.text(80, 51, df['Adjusted Grade'][1], color = '#0a3222', size = 9, fontweight = 'bold')

ab = AnnotationBbox(getImage('Timbers Headshots/'+df['path'][2]), (85, 15), frameon=False)
ax.add_artist(ab)
plt.text(80, 22, df['Player Name'][2], color = '#d0e0da', size = 8)
plt.text(80, 26, df['Adjusted Grade'][2], color = '#0a3222', size = 9, fontweight = 'bold')

ab = AnnotationBbox(getImage('Timbers Headshots/'+df['path'][3]), (85, 65), frameon=False)
ax.add_artist(ab)
plt.text(80, 72, df['Player Name'][3], color = '#d0e0da', size = 8)
plt.text(80, 76, df['Adjusted Grade'][3], color = '#0a3222', size = 9, fontweight = 'bold')

ab = AnnotationBbox(getImage('Timbers Headshots/'+df['path'][8]), (45, 25), frameon=False)
ax.add_artist(ab)
plt.text(40, 32, df['Player Name'][8], color = '#d0e0da', size = 8)
plt.text(40, 36, df['Adjusted Grade'][8], color = '#0a3222', size = 9, fontweight = 'bold')


ab = AnnotationBbox(getImage('Timbers Headshots/'+df['path'][9]), (45, 55), frameon=False)
ax.add_artist(ab)
plt.text(40, 62, df['Player Name'][9], color = '#d0e0da', size = 8)
plt.text(40, 66, df['Adjusted Grade'][9], color = '#0a3222', size = 9, fontweight = 'bold')


ab = AnnotationBbox(getImage('Timbers Headshots/'+df['path'][4]), (20, 27), frameon=False)
ax.add_artist(ab)
plt.text(15, 34, df['Player Name'][4], color = '#d0e0da', size = 8)
plt.text(15, 38, df['Adjusted Grade'][4], color = '#0a3222', size = 9, fontweight = 'bold')


ab = AnnotationBbox(getImage('Timbers Headshots/'+df['path'][5]), (20, 53), frameon=False)
ax.add_artist(ab)
plt.text(15, 60, df['Player Name'][5], color = '#d0e0da', size = 8)
plt.text(15, 64, df['Adjusted Grade'][5], color = '#0a3222', size = 9, fontweight = 'bold')


ab = AnnotationBbox(getImage('Timbers Headshots/'+df['path'][7]), (20, 10), frameon=False)
ax.add_artist(ab)
plt.text(15, 17, df['Player Name'][7], color = '#d0e0da', size = 8)
plt.text(15, 20, df['Adjusted Grade'][7], color = '#0a3222', size = 9, fontweight = 'bold')


ab = AnnotationBbox(getImage('Timbers Headshots/'+df['path'][6]), (20, 70), frameon=False)
ax.add_artist(ab)
plt.text(15, 77, df['Player Name'][6], color = '#d0e0da', size = 8)
plt.text(15, 80, df['Adjusted Grade'][6], color = '#0a3222', size = 9, fontweight = 'bold')


ab = AnnotationBbox(getImage('Timbers Headshots/'+df['path'][10]), (5, 40), frameon=False)
ax.add_artist(ab)
plt.text(2, 47, df['Player Name'][10], color = '#d0e0da', size = 8)
plt.text(2, 51, df['Adjusted Grade'][10], color = '#0a3222', size = 9, fontweight = 'bold')

plt.title('Timbers vs Sounders Player Grades', color = '#0a3222', fontweight = 'bold')

# Save plot
plt.savefig('FIFAPostGrades.png', dpi=1200, bbox_inches = 'tight')
