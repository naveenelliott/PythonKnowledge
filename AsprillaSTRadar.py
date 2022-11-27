# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 14:03:15 2022

@author: Owner
"""

import os
import pandas as pd 
import numpy as np 
import calendar 
import matplotlib.pyplot as plt
from mplsoccer import Radar, FontManager 

fb = pd.read_csv("My Player Grades/Player Grades for Each Game - CF's (8).csv")
fb.head()

# van_rankin = fb.loc[fb['Match'] == 'Jose Van Rankin']
rasmussen = fb.loc[fb['Match'] == 'Dairon Asprilla']

update_rasmussen = rasmussen.loc[rasmussen['Date'] == ('9/18/2022')]


# add ranges to list of tuple pairs
# a_values = van_rankin[['Match','Total Actions ', 'Passing', 'Playmaking', 'Defensive', 'Dribbling', 'ADJ GRADE']]
b_values = update_rasmussen[['Total Actions ', 'Shooting', 'Passing', 'Dribbling/Skilling', 'Aerials', 'Pressing', 'ADJUSTED GRADE']]
total_actions = update_rasmussen['Total Actions '].values[0]
total_actions = float(total_actions)
passing = update_rasmussen['Shooting'].values[0]
passing = float(passing)
playmaking = update_rasmussen['Passing'].values[0]
playmaking = float(playmaking)
defensive = update_rasmussen['Dribbling/Skilling'].values[0]
defensive = float(defensive)
dribbling = update_rasmussen['Aerials'].values[0]
dribbling = float(dribbling)
pressing = update_rasmussen['Pressing'].values[0]
pressing = float(pressing)
adj_grade = update_rasmussen['ADJUSTED GRADE'].values[0]
adj_grade = float(adj_grade)

values = [total_actions, passing, playmaking, defensive, dribbling, pressing, adj_grade]

# get parameters
params = list(b_values.columns)
low = [0, 0, 0, 0, 0, 0, 0]
high = [10, 10, 10, 10, 10, 10, 10]


URL6 = 'https://github.com/googlefonts/roboto/blob/main/src/hinted/Roboto-Bold.ttf?raw=true'
robotto_bold = FontManager(URL6)

def radar_mosaic(radar_height=0.915, title_height=0.06, figheight=14):
    """ Create a Radar chart with a title and endnote axes.

    Parameters
    ----------
    radar_height: float, default 0.915
        The height of the radar axes in fractions of the figure height (default 91.5%).
    title_height: float, default 0.06
        The height of the title axes in fractions of the figure height (default 6%).
    figheight: float, default 14
        The figure height in inches.

    Returns
    -------
    fig : matplotlib.figure.Figure
    axs : dict[label, Axes]
    """
    if title_height + radar_height > 1:
        error_msg = 'Reduce one of the radar_height or title_height so the total is ≤ 1.'
        raise ValueError(error_msg)
    endnote_height = 1 - title_height - radar_height
    figwidth = figheight * radar_height
    figure, axes = plt.subplot_mosaic([['title'], ['radar'], ['endnote']],
                                      gridspec_kw={'height_ratios': [title_height, radar_height,
                                                                     endnote_height],
                                                   # the grid takes up the whole of the figure 0-1
                                                   'bottom': 0, 'left': 0, 'top': 1,
                                                   'right': 1, 'hspace': 0},
                                      figsize=(figwidth, figheight))
    axes['title'].axis('off')
    axes['endnote'].axis('off')
    return figure, axes

radar = Radar(params, low, high) 
fig, axs = radar_mosaic(radar_height=0.9, title_height=0.1, figheight=14)  # format axis as a radar
# plot the radar 
radar.setup_axis(ax=axs['radar'])
rings_inner = radar.draw_circles(ax=axs['radar'], facecolor='#D3D3D3', edgecolor='white')  # draw circles
radar_output = radar.draw_radar(values, ax=axs['radar'],
                                kwargs_radar={'facecolor': '#00482B'},
                                kwargs_rings={'facecolor': '#D69A00'})  # draw the radar
radar_poly, rings_outer, vertices = radar_output
range_labels = radar.draw_range_labels(ax=axs['radar'], fontsize=23, fontproperties=robotto_bold.prop)  # draw the range labels
param_labels = radar.draw_param_labels(ax=axs['radar'], fontsize=27, fontproperties=robotto_bold.prop)  # draw the param labels 

title1_text = axs['title'].text(0.03, .65, 'Dairon Asprilla', fontsize=35, fontproperties=robotto_bold.prop, ha='left', va='center', color='#00482B')
title2_text = axs['title'].text(0.03, .13, 'Portland Timbers', fontsize = 30, fontproperties=robotto_bold.prop, ha='left', va='center', color='#D69A00')
title3_text = axs['title'].text(0.97, 0.65, 'Radar Chart', fontsize = 35, fontproperties=robotto_bold.prop, ha='right', va='center', color='#00482B')
title4_text = axs['title'].text(0.97, 0.13, 'Center Forward', fontsize = 30, fontproperties=robotto_bold.prop, ha='right', va='center', color='#D69A00')    
plt.savefig('AsprillaRadarST.png')
    
    
    
    