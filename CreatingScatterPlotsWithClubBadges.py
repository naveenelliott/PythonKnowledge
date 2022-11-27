# -*- coding: utf-8 -*-
"""
Created on Fri May 27 14:12:10 2022

@author: Naveen
"""

# In this tutorial, we're going to create a scatter plot of teams xG & xGA, but with club logos representing each one
# To do this, we're going to go through the following steps:
    # Prep our badge images
    # Import and check data 
    # Plot regular scatter chart 
    # Plot badges on top of the scatter points 
    # tidy and improve our chart 
import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
df = pd.read_csv('Scatter Plot Logos/xGTable.csv')
df.head()

df['path'] = df['Squad'] + '.png'
df.head()

# Before making our plot with badges, we need to create a regular scatter plot. 
# This gives us the correct dimensions of the plot, the axes and other benefits of working with matplotlib
fig, ax = plt.subplots(figsize=(6,4), dpi=120)
ax.scatter(df['xG'], df['xGA'])
# Our base figures provides the canvas for the club badges 
# The first tool we will use is 'OffsetImage', which creates a box with an image, allows us to edit the image and readies it to be added to our plot. 
def getImage(path):
    return OffsetImage(plt.imread(path), zoom=.05, alpha = 1)
# OffsetImage takes a few arguments. Let's look at them in order:
    # The image. We use the plt.imread function to read in an image from the location that we provide. In this case, it will look in the path that we created in the dataframe earlier
    # Zoom level. The images are too big by default. .05 reduces their size to 5% of the original 
    # Alpha level. Our bades are likely to overlap, in case you want to make them transparent, change this figure to any number between 0 and 1

# This function prepares the image, but we still need to plot them. Let's do this by creating a new plot, just as before, then iterating on our dataframe to plot each team crest 
fig, ax = plt.subplots(figsize=(6,4), dpi=120)
ax.scatter(df['xG'], df['xGA'], color='white')
# Creating scatterplot, but with white points to hide them against the background

# Iterating through dataframe with df.iterrows()
for index, row in df.iterrows():
    ab = AnnotationBbox(getImage('Scatter Plot Logos/images/'+row['path']), (row['xG'], row['xGA']), frameon=False)
    # For each row of our data we use AnnotationBbox from matplotlib to take the desired image and assign its x,y location
    ax.add_artist(ab)
    # Draws this on our plot 
    
# Final touches
# Set font and background color 
bgcol = '#fafafa'

# Create initial plot 
fig, ax = plt.subplots(figsize=(6,4), dpi=120)
fig.set_facecolor(bgcol)
ax.set_facecolor(bgcol)
ax.scatter(df['xG'], df['xGA'], c=bgcol)

# Change plot spines 
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_color('#ccc8c8')
ax.spines['bottom'].set_color('#ccc8c8')

# Change ticks 
plt.tick_params(axis='x', labelsize=12, color='#ccc8c8')
plt.tick_params(axis='y', labelsize=12, color='#ccc8c8')

# Plot badges
def getImage(path):
    return OffsetImage(plt.imread(path), zoom=.05, alpha = 1)

for index, row in df.iterrows():
    ab = AnnotationBbox(getImage('Scatter Plot Logos/images/'+row['path']), (row['xG'], row['xGA']), frameon=False)
    ax.add_artist(ab)

# Add average lines 
plt.hlines(df['xGA'].mean(), df['xG'].min(), df['xG'].max(), color='#c2c1c0')
plt.vlines(df['xG'].mean(), df['xGA'].min(), df['xGA'].max(), color='#c2c1c0')

# Text

# Title & Axis'
fig.text( 'xG Performance, Weeks 1-6', size=20)
plt.xlabel('xG For')
plt.ylabel('xG Against')

# Avg line explanation 
fig.text(.76, .535, 'Avg. xG Against', size=6, color='#c2c1c0')
fig.text(.325, .17, 'Avg. xG For', size=6, color='#c2c1c0', rotation=90)

# Save plot
plt.savefig('xGChart.png', dpi=1200, bbox_inches = 'tight')


