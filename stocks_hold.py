import pandas_datareader.data as web
import pandas as pd
import datetime
import helper

ds_yahoo = 'yahoo'

last_year = datetime.datetime.now().year - 1
start = datetime.datetime.now().replace(year=last_year)
end = datetime.datetime.now()

tickers = ['ITUB4.SA', 'ABEV3.SA', 'USIM5.SA', 'PMAM3.SA', 'FLRY3.SA', 'TIET11.SA']


def port_adj_close():
        data = pd.DataFrame()
        for t in tickers:
                data[t] = web.DataReader(t, ds_yahoo, start, end)['Adj Close']
        data.to_csv('csv/portfolio_adj_close.csv')


def read_stocks_and_generate_csv():
        itau = web.DataReader('ITUB4.SA', ds_yahoo, start, end)
        itau.to_csv('csv/itau.csv')

        ambev = web.DataReader('ABEV3.SA', ds_yahoo, start, end)
        ambev.to_csv('csv/ambev.csv')

        usim = web.DataReader('USIM5.SA', ds_yahoo, start, end)
        usim.to_csv('csv/usim.csv')

        pmam = web.DataReader('PMAM3.SA', ds_yahoo, start, end)
        pmam.to_csv('csv/pmam.csv')

        fleury = web.DataReader('FLRY3.SA', ds_yahoo, start, end)
        fleury.to_csv('csv/fleury.csv')

        tiete = web.DataReader('TIET11.SA', ds_yahoo, start, end)
        tiete.to_csv('csv/tiete.csv')


ibov_df = pd.read_csv('csv/ibov.csv', index_col=0)
itau_df = pd.read_csv('csv/itau.csv', index_col=0)
fleury_df = pd.read_csv('csv/fleury.csv', index_col=0)
tiete_df = pd.read_csv('csv/tiete.csv', index_col=0)
ambev_df = pd.read_csv('csv/ambev.csv', index_col=0)
pmam_df = pd.read_csv('csv/pmam.csv', index_col=0)
usim_df = pd.read_csv('csv/usim.csv', index_col=0)

adj = 'Adj Close'
all_adj_close = pd.concat([itau_df[adj], fleury_df[adj], tiete_df[adj], ambev_df[adj], pmam_df[adj], usim_df[adj]], axis=1, sort=True)

# all_adj_close.columns('Itau', 'Fleury', 'AES Tietê', 'AMBEV', 'Paranapanema', 'Usiminas')