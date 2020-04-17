from django.shortcuts import render
from django.core.paginator import Paginator
import pandas as pd
import requests
from datetime import datetime
from bokeh.themes import built_in_themes
from math import pi
from bokeh.plotting import figure, show, output_notebook, output_file
from bokeh.io import curdoc
from bokeh.io import export_png
from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components
from django.http import JsonResponse, HttpResponse

def home(request):
    import requests
    import json

    # Grab Crypto Price Data
    # price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    # price = json.loads(price_request.content)

    # Grab Crypto News
    api_request = requests.get(
        "https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    price = api_periodic_refresh()
    return render(request, 'home.html', {'api': api, 'price': price})


def api_periodic_refresh(request=None):
    import json
    import requests

    # Grab Crypto Price Data
    price_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price = json.loads(price_request.content)

    if request is None:
        return json.loads(price_request.content)
    else:
        return HttpResponse(price_request.content, content_type='application/json')

# def home(request):
# 	import requests
# 	import json
	
# 	# Grab Crypto Price Data
# 	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
# 	price = json.loads(price_request.content)

# 	# Grab Crypto News
# 	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
# 	api = json.loads(api_request.content)
# 	return render(request, 'home.html', {'api': api, 'price': price})


def prices(request):
	if request.method == 'POST':
		import requests
		import json
		quote = request.POST['quote']
		quote = quote.upper()
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
		crypto = json.loads(crypto_request.content)
		return render(request, 'prices.html', {'quote':quote, 'crypto': crypto})
		
		
	else:
		notfound = "Enter a crypto currency symbol into the form above..."
		return render(request, 'prices.html', {'notfound': notfound})

def simple_chart(request):
    # plot = figure()
    # plot.circle([1,2], [3,4])
	import os
	mainfolder = os.path.join(os.path.dirname(__file__), '..')

	from_symbol = 'BTC'
	to_symbol = 'USD'
	exchange = 'Bitstamp'
	datetime_interval = 'day'
	current_datetime = datetime.now().date().isoformat()
	filename = get_filename(from_symbol, to_symbol, exchange, datetime_interval, current_datetime)
	filename=mainfolder+'/templates/'+filename
	df = read_dataset(filename)
	from stockstats import StockDataFrame
	df = StockDataFrame.retype(df)
	df['macd'] = df.get('macd') # calculate MACD
	df.head()
	output_notebook()
	datetime_from = '2016-01-01 00:00'
	datetime_to = current_datetime
	df_limit = df[datetime_from: datetime_to].copy()
	inc = df_limit.close > df_limit.open
	dec = df_limit.open > df_limit.close
	title = 'Bullish-Bearish Stratergies from %s to %s for %s and %s from %s with MACD strategy' % (
		datetime_from, datetime_to, from_symbol, to_symbol, exchange)
	p = figure(x_axis_type="datetime",  plot_width=1000, title=title)
	p.line(df_limit.index, df_limit.close, color='black')
	# plot macd strategy
	p.line(df_limit.index, 0, color='black')
	p.line(df_limit.index, df_limit.macd, color='blue')
	p.line(df_limit.index, df_limit.macds, color='orange')
	p.vbar(x=df_limit.index, bottom=[
		0 for _ in df_limit.index], top=df_limit.macdh, width=4, color="purple")
	# plot candlesticks
	candlestick_width = get_candlestick_width(datetime_interval)
	p.segment(df_limit.index, df_limit.high,
			df_limit.index, df_limit.low, color="black")
	p.vbar(df_limit.index[inc], candlestick_width, df_limit.open[inc],
		df_limit.close[inc], fill_color="#D5E1DD", line_color="black")
	p.vbar(df_limit.index[dec], candlestick_width, df_limit.open[dec],
		df_limit.close[dec], fill_color="#F2583E", line_color="black")
	# output_file("dark_minimal.html", title="visualizing trading strategy")
	# curdoc().theme = 'dark_minimal'
	# show(p)
	script, div = components(p, CDN)

	return render(request, "simple_chart.html", {"the_script": script, "the_div": div})

def get_filename(from_symbol, to_symbol, exchange, datetime_interval, download_date):
    return '%s_%s_%s_%s_%s.csv' % (from_symbol, to_symbol, exchange, datetime_interval, download_date)



def read_dataset(filename):
    print('Reading data from %s' % filename)
    df = pd.read_csv(filename)
    df.datetime = pd.to_datetime(df.datetime) # change type from object to datetime
    df = df.set_index('datetime') 
    df = df.sort_index() # sort by datetime
    print(df.shape)
    return df
def get_candlestick_width(datetime_interval):
    if datetime_interval == 'minute':
        return 30 * 60 * 1000  # half minute in ms
    elif datetime_interval == 'hour':
        return 0.5 * 60 * 60 * 1000  # half hour in ms
    elif datetime_interval == 'day':
        return 12 * 60 * 60 * 1000  # half day in ms