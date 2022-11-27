# -*- coding: utf-8 -*-
"""
Created on Fri May  6 14:56:34 2022

@author: Naveen
"""

#Make a shot map and a pass map using Statsbomb data
#Set match id in match_id_required.

#Function to draw the pitch
import matplotlib.pyplot as plt
import numpy as np

#Size of the pitch in yards (!!!)
pitchLengthX=120
pitchWidthY=80

#ID for England vs Sweden Womens World Cup
match_id_required = 8651
home_team_required = "Sweden"
away_team_required = "England"

# Load in the data
# I took this from https://znstrider.github.io/2018-11-11-Getting-Started-with-StatsBomb-Data/
file_name=str(match_id_required)+'.json'

#Load in all match events 
import json
with open('Statsbomb/data/events/'+file_name) as data_file:
    #print (mypath+'events/'+file)
    data = json.load(data_file)

#get the nested structure into a dataframe 
#store the dataframe in a dictionary with the match id as key (remove '.json' from string)
from pandas.io.json import json_normalize
df = json_normalize(data, sep = "_").assign(match_id = file_name[:-5])

#A dataframe of shots
passes = df.loc[df['type_name'] == 'Pass'].set_index('id')
    
#Draw the pitch
from FCPython import createPitch
(fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','gray')


#Plot the shots
for i,thepass in passes.iterrows():
    x=thepass['location'][0]
    y=thepass['location'][1]
    circleSize=2
    if thepass['player_name']=="Harry Kane":
        passCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="blue")     
        passCircle.set_alpha(.2)
        ax.add_patch(passCircle)
        dx=thepass['pass_end_location'] [0]-x
        dy=thepass['pass_end_location'][1]-y
        passArrow=plt.Arrow(x,pitchWidthY-y,dx,-dy,width=3,color="blue")
        ax.add_patch(passArrow)
        
#for i,shot in shots.iterrows():
 #   x=shot['location'][0]
  #  y=shot['location'][1]
   # circleSize=4
    #if shot['player_name']=="Harry Kane":
     #   shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="blue")
      #  shotCircle.set_alpha(.2)
     #   ax.add_patch(shotCircle)
     
fig.set_size_inches(10, 7)
fig.savefig('Output/HarryKane.pdf', dpi=100) 
plt.show()

#Exercise: 
#1, Create a dataframe of passes which contains all the passes in the match
#2, Plot the start point of every Sweden pass. Attacking left to right.
#3, Plot only passes made by Caroline Seger (she is Sara Caroline Seger in the database)
#4, Plot arrows to show where the passes went