import pandas_datareader.data as web
import datetime

datasource = 'yahoo'

last_year = datetime.datetime.now().year - 1
start = datetime.datetime.now().replace(year=last_year)
end = datetime.datetime.now()

# Energia

engie = web.DataReader('EGIE3.SA', datasource, start, end)
edpbrasil = web.DataReader('ENBR3.SA', datasource, start, end)

# Máquinas e Equipamentos

weg = web.DataReader('WEGE3.SA', datasource, start, end)

# Financeiros

bancomercantil = web.DataReader('BMEB4.SA', datasource, start, end)
b3 = web.DataReader('B3SA3.SA', datasource, start, end)