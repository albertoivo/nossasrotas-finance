import pandas_datareader.data as web
import pandas as pd
import datetime

ds_yahoo = 'yahoo'

tickers = ['^GSPC', '^IXIC', '^GDAXI', '^DJI']

last_year = datetime.datetime.now().year - 1
start = datetime.datetime.now().replace(year=last_year)
end = datetime.datetime.now()

# ibov = web.DataReader('^BVSP', ds_yahoo, start, end)
# ibov.to_csv('csv/ibov.csv')

sp500 = web.DataReader('^GSPC', ds_yahoo, start, end)
sp500.to_csv('csv/sp500.csv')

nasdaq = web.DataReader('^IXIC', ds_yahoo, start, end)
nasdaq.to_csv('csv/nasdaq.csv')

dax = web.DataReader('^GDAXI', ds_yahoo, start, end)
dax.to_csv('csv/dax.csv')

# nasdaq_footsie = web.DataReader('^FTSE', ds_yahoo, start, end)
# nasdaq_footsie.to_csv('csv/nasdaq_footsie.csv')

dji = web.DataReader('^DJI', ds_yahoo, start, end)
dji.to_csv('csv/dji.csv')

# adj = 'Adj Close'
# all_adj_close = pd.concat([sp500[adj], nasdaq[adj], dax[adj], dji[adj], ibov[adj]], axis=1, sort=True)

def port_adj_close():
  data = pd.DataFrame()
  for t in tickers:
          data[t] = web.DataReader(t, ds_yahoo, start, end)['Adj Close']
  data.to_csv('csv/indices_ex_adj_close.csv')

port_adj_close()