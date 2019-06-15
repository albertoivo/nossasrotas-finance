import pandas_datareader.data as web
import datetime

ds_yahoo = 'yahoo'

last_year = datetime.datetime.now().year - 1
start = datetime.datetime.now().replace(year=last_year)
end = datetime.datetime.now()

itau = web.DataReader('ITUB4.SA', ds_yahoo, start, end)
ambev = web.DataReader('ABEV3.SA', ds_yahoo, start, end)
usiminas = web.DataReader('USIM5.SA', ds_yahoo, start, end)
paranapanema = web.DataReader('PMAM3.SA', ds_yahoo, start, end)
fleury = web.DataReader('FLRY3.SA', ds_yahoo, start, end)
