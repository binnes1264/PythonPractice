#n01445323 - Bethany Innes

import pandas as pd
import numpy as np

df = pd.read_csv('items.csv')
#set to make sure all columns are displayed
pd.set_option('display.max_columns', None)

#printing the first 7 objects in the data
print('The first 8 items')
print(df.head(7), '\n')

#printing the last 7 objects in the data
print('The last 8 items')
print(df.tail(7), '\n')

#printing the information about the data
print('Information about Items DataFrame')
print(df.info(), '\n')

#printing the number of rows and columns
print('Items DataFrame has', len(df), 'rows and', len(df.columns), 'columns\n')

#printing Bottle_Cost descriptive statistics
print('Descriptive statistics for Bottle_Cost')
print(df['Bottle_Cost'].describe())

#adding new column to data and printing new table
df['bottle_profit_margin'] = (df['Bottle_Retail_Price'] - df['Bottle_Cost']) / df['Bottle_Retail_Price']
print('DataFrame after adding bottle_profit_margin column')
print(df.head(5), '\n')

#deleting rows 5 through 15 then printing new table
df.drop(df.index[5:15], inplace=True)
print('Rows 5 to 15 are deleted')
print(df.head(20), '\n')

#printing drinks with more than 750ml, more than 12 pack, profit more than 0.3
print('Items with more than 750ml, 12 packs, and bottle_profit_margin more than 0.3')
print(df[(df['Bottle_Volume_ml']> 750) & (df['Pack']> 12) & (df['bottle_profit_margin']> 0.3)], '\n')

#printing number of energy drinks
print('Number of Energy Drinks')
print(len(df[df.Category =='Energy Drink']), '\n')

#creating new DataFrame and printing
items2 =df[['Item_id', 'Item_Description' ,'Bottle_Retail_Price','bottle_profit_margin']].copy()
print('The new DataFrame')
print(items2.head(16), '\n')

#adding QTY column and printing
items2['QTY'] = np.random.randint(0, 1000, size = 4149)
print('QTY column added to DataFrame')
print(items2.head())