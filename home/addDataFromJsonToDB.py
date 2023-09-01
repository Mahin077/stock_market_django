import json
from home.models import StockMarket

with open('static/stock_market_data.json') as json_file:
    data = json.load(json_file)

objects_to_create = [
    StockMarket(date=item['date'], trade_code=item['trade_code'],high=float(item['high'].replace(',','')),low=float(item['low'].replace(',','')),open=float(item['open'].replace(',','')),close=float(item['close'].replace(',','')),volume=int(item['volume'].replace(',','')))  #using replace() to remove the commas
    for item in data
]

StockMarket.objects.bulk_create(objects_to_create)