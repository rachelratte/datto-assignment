# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:55:16 2018

@author: Rachel Ratte

Usage: Reads a csv file named "quandl_full_data.csv" from the same directory as the executable.
        Exports data to "quandl_full_data.parquet" in the same directory as the executable.

Requires: Pandas and pyarrow (or fastparquet)
"""
import pandas as pd

#read the target collums from the csv in to a dataframe. Assumes csv is in the same directory as this *.py file. 
#To debug, use nrows=# where # is a manageable number that doesn't take too long to load
df = pd.read_csv('quandl_full_data.csv', usecols=['ticker', 'date', 'open', 'close'], nrows = 20)

#drop rows that presumably have incorrect data (stocks' open or close should never be 0 or negative)
df[(df[['open','close']] > 0).all(1)]

#adds a new collumn 'average' to the dataframe where each row average[n] is the mean of open[n] and close[n]
df['average'] = df[['open', 'close']].mean(axis=1)

#exports the dataframe to a parquet file in the same directory as this *.py file
df.to_parquet('quandl_full_data.parquet')

