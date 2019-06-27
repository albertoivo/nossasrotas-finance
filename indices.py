import pandas_datareader.data as web
import pandas as pd
import datetime

ds_yahoo = 'yahoo'

tickers = {'IBOV': '^BVSP', 'SP500': '^GSPC', 'Nasdaq': '^IXIC',
           'DAX': '^GDAXI', 'DowJones': '^DJI', 'Footsie': '^FTSE'}

last_year = datetime.datetime.now().year - 1
start = datetime.datetime.now().replace(year=last_year)
end = datetime.datetime.now()


def generate_index_csv():

    for k, v in tickers.items():
        df = web.DataReader(v, ds_yahoo, start, end)
        df.to_csv('csv/ibov.csv')


# adj = 'Adj Close'
# all_adj_close = pd.concat([sp500[adj], nasdaq[adj], dax[adj], dji[adj], ibov[adj]], axis=1, sort=True)


def port_adj_close():
    data = pd.DataFrame()
    for t in tickers:
        data[t] = web.DataReader(t, ds_yahoo, start, end)['Adj Close']
    data.to_csv('csv/indices_ex_adj_close.csv')


generate_index_csv()
