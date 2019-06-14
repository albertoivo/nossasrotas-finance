import os.path
import pandas as pd
import numpy as np
import helper
import matplotlib.pyplot as plt


def generate_json(nome, stock):
    filename = helper.format_filename(nome)
    if not os.path.exists(filename):
        stock.to_json('json/{}.json'.format(filename))


def medias(nome, stock, medias):
    generate_json(nome, stock)

    df = pd.read_json('json/{}.json'.format(nome))
    for m in medias:
        df['{} Mean'.format(m)] = df['Close'].rolling(window=m).mean()

    return df


def bollinger(nome, stock, media=20):
    generate_json(nome, stock)
    
    df = pd.read_json('json/{}.json'.format(nome))
    column_name = 'Close: {} Day Mean'.format(media)
    df[column_name] = df['Close'].rolling(window=media).mean()
    df['Upper'] = df[column_name] + 2*df['Close'].rolling(window=media).std()
    df['Lower'] = df[column_name] - 2*df['Close'].rolling(window=media).std()
    
    return df[['Close',column_name,'Upper','Lower']]


def retorno_diario(stock):
    adj_close = stock['Adj Close']
    log_returns = np.log(adj_close / adj_close.shift(1))
    log_returns.plot(figsize=(17,6))
    plt.ylabel('Retorno Diário %')
    plt.xlabel('DATA')

    return plt


def fibonacci(stock):
    price_min = stock['Close'].min()
    price_max = stock['Close'].max()

    diff = price_max - price_min
    level1 = price_max - 0.236 * diff
    level2 = price_max - 0.382 * diff
    level3 = price_max - 0.618 * diff

    fig, ax = plt.subplots()
    ax.plot(stock.Close, color='black')

    ax.axhspan(level1, price_min, alpha=0.4, color='lightsalmon')
    ax.axhspan(level2, level1, alpha=0.5, color='palegoldenrod')
    ax.axhspan(level3, level2, alpha=0.5, color='palegreen')
    ax.axhspan(price_max, level3, alpha=0.5, color='powderblue')

    plt.ylabel("Price")
    plt.xlabel("Date")

    return plt