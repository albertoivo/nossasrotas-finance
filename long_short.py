import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime

datasource = 'yahoo'

last_year = datetime.datetime.now().year - 1
start = datetime.datetime.now().replace(year=last_year)
end = datetime.datetime.now()

bancos = ['BBDC4.SA', 'BBDC3.SA', 'ITUB4.SA', 'ITUB3.SA', 'BBAS3.SA', 'SANB3.SA', 'SANB11.SA', 'SANB4.SA', 'ITSA3.SA', 'ITSA4.SA']

prices = pd.DataFrame()
for b in bancos:
    prices[b] = web.DataReader(b, datasource, start, end)['Adj Close']

log_returns = np.log(prices/prices.shift(1))