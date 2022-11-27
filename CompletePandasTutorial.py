# -*- coding: utf-8 -*-
"""
Created on Sun May 22 09:11:34 2022

@author: Naveen
"""

import pandas as pd 

# Loading in data
df = pd.read_csv('pokemon_data.csv')

# print(df.head(3))
# print(df.tail(3))

# Read Headers
# print(df.columns)

# Read each column 
# print(df[['Name', 'Type 1', 'HP']])

# Read each Row 
# print(df.head(4))
# print(df.iloc[1:4])
# print(df.iloc[2,1])
# for index, row in df.iterrows():
  #  print(index, row['Name'])
# print(df.loc[df['Type 1'] == 'Fire'])
df.describe()

# Sorting data
df.sort_values(['Type 1', 'HP'], ascending = [1,0])

# Making changes to the data
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

df = df.drop(columns=['Total'])

cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

df.head(5)

# Converting data frame to csv and excel files
df.to_csv('modified.csv', index = False)

df.to_excel('modified.xlsx', index = False)

df.to_csv('modified.txt', index=False, sep='\t' )

# Filtering Data
new_df = df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison') & (df['HP'] > 70)]

# new_df.to_csv('filtered.csv')

new_df = new_df.reset_index(drop=True, inplace=True)

import re
df.loc[~df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]

# find a pokemon that starts with 'pi' and next can be a-z
df.loc[df['Name'].str.contains('pi[a-z]*', flags = re.I, regex = True)]

# Conditional Changes

df.loc[df['Type 1'] == 'Flamer', 'Legendary'] = True

df = pd.read_csv('modified.csv')

# df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = 'TEST VALUE'

df = pd.read_csv('modified.csv')

# Aggregate Statistics (Groupby)

df.groupby(['Type 1']).mean().sort_values('Defense', ascending = False)

df.groupby(['Type 1']).sum()

df['count'] = 1
df.groupby(['Type 1', 'Type 2']).count()['count']

# Working with large amounts of data 
# Five rows getting passed in at a time
new_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv('modified.csv', chunksize = 5):
    results = df.groupby(['Type 1'].count())
    new_df = pd.concat([new_df, results])
    print('Chunk DF')
    print(df)



