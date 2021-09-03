import pandas as pd
import numpy as np
from datetime import datetime

sp500 = pd.read_csv('sphist.csv')
sp500['Date'] = pd.to_datetime(sp500['Date'])
sp500 = sp500.sort_values(by='Date')
sp500 = sp500.reset_index(drop=True)
sp500['avg_past_5'] = 0
sp500['avg_past_365'] = 0
sp500['avg_ratio_5_365'] = 0

for row in sp500.iterrows():
    if row[1]['Date'] < datetime(year=1951, month=1, day=3):
        continue
    else:
        # Computing average from past 5 days
        past_5 = row[0] - 5
        avg_5 = sp500.loc[past_5:row[0], 'Close'].mean()
        sp500.loc[row[0], 'avg_past_5'] = avg_5
        
        # Computing average from past 365 days
        counter = 0
        avg_365 = sp500.loc[counter:row[0], 'Close'].mean()
        sp500.loc[row[0], 'avg_past_365'] = avg_365
        counter += 1
        
        # Computing ratio between both indicators above 
        if row[1]['avg_past_365'] == 0:
            continue
        else:
            sp500.loc[row[0], 'avg_ratio_5_365'] = row[1]['avg_past_5']/(row[1]['avg_past_365'])

print(sp500.tail())