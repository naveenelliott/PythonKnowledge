# -*- coding: utf-8 -*-
"""
Created on Mon May 23 16:54:28 2022

@author: Naveen
"""

import pandas as pd 
import matplotlib.pyplot as plt 

# Our pie chart is going to display the share of Premier league wins, as shown in our data below: 
leagueWins = {'Team': ['Manchester United','Blackburn Rovers','Arsenal','Chelsea',
                       'Manchester City', 'Leicester City'], 'Championships': [13, 1, 3, 4, 2, 1]}
df = pd.DataFrame(leagueWins, columns=['Team', 'Championships'])

plt.pie(df['Championships'])

# This next line just makes the plot look a little clearn in this notebook
plt.tight_layout()

# Create a list of the colors used for the teams, in order. 
teamColours = ['#f40206', '#0560b5', '#ce0000', '#1125ff', '#28cdff', '#091ebc']

plt.pie(df['Championships'],
        # Data labels are the team names in the dataFrame
        labels = df['Team'],
        # Assign our colors list 
        colors = teamColours,
        # Give a tidier angle to your first data angle 
        startangle = 90)

# Add a title 
plt.title('Premier League Titles')
plt.tight_layout()