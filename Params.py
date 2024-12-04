import requests as rq
import pandas as pd

stocks = pd.read_csv('currency.csv')
stock_dict = stocks.to_dict(orient='records')

crurl = 'https://api.coinbase.com/v2/exchange-rates'

crHeader = {
    'user agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}

for st in stock_dict:
    currency = st['Currency']
    currencyParam = {'currency': currency}
    crresp = rq.get(url = crurl,headers=crHeader,params=currencyParam)
    crData = crresp.json()
    inr_rate = crData['data']['rates']['INR']
    st['INR_Price'] = st['Price'] * float(inr_rate)
    
currency_df = pd.DataFrame(stock_dict)
currency_df.to_csv('INR.csv')