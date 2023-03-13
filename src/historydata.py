import pandas as pd
import yfinance as yf
import numpy as np 

df = pd.read_csv('/Users/gary/Documents/Python/data/growin/row_data.csv')
df = df.ticker.unique()
tick_list = list(df)

for ticker in tick_list:

    a = yf.download(str(ticker),start='2020-01-01',end='2023-01-01') 
    a.to_csv('/Users/gary/Documents/Python/NCKU-DAC-x-Growin/src/data/%s.csv'%(ticker))
    print(ticker)
