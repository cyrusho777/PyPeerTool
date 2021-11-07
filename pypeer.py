import requests 
import pandas as pd
import json

api_key= 'ENTER-API-KEY-HERE'
tickers = []

def quote(ticker):
 # Company Quote Group of Items
    url = f"https://financialmodelingprep.com/api/v3/quote/{ticker}?apikey={api_key}"
    quote = requests.get(url)
    data = quote.text
    dataList = json.loads(data)
    market_cap = float("{0:.2f}".format((dataList[0]['marketCap']/10**9)))
    share_price = float("{0:.2f}".format(dataList[0]['price']))

    return(share_price,market_cap)

def analysis(ticker,tickers):
    data = map(quote, tickers)
    df = pd.DataFrame(data, columns=[f'Share Price of {ticker}s peers','Market Cap (Billions)'],index=tickers)
    print(df)

def peers(ticker):
    url = f"https://financialmodelingprep.com/api/v4/stock_peers?symbol={ticker}&apikey={api_key}"
    peers = requests.get(url)
    data = peers.text
    dataList = json.loads(data)
    tickers = dataList[0]['peersList']
    print(tickers)
    analysis(ticker,tickers)
    return(tickers)

def user_input():
    ticker = input('What is the Ticker?')
    peers(ticker)


user_input()

    




