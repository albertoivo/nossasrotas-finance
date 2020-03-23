import seaborn as sns
import pandas as pd
import numpy as np
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime
import stocks

datasource = 'yahoo'

now = datetime.datetime.now()

def correlacao(stocks, start, end=now):
    prices = pd.DataFrame()

    for b in stocks:
        prices[b] = web.DataReader(b, datasource, start, end)['Adj Close']

    log_returns = np.log(prices / prices.shift(1))
    return log_returns.corr()


def heatmap(correlacao):
    sns.set()

    f, ax = plt.subplots(figsize=(34, 15))
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    mask = np.zeros_like(correlacao, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    sns.heatmap(correlacao, mask=mask, cmap=cmap, vmax=1, center=0.5,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
