from math import pi
import pandas as pd
import requests
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.stocks import MSFT


COIN_LIST_URL = 'https://min-api.cryptocompare.com/data/all/coinlist'
HISTO_DAY_URL = 'https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym={}&allData=True'

coins_json_response = requests.get(COIN_LIST_URL).json()
coins = pd.DataFrame(coins_json_response['Data']).T
coins = coins.infer_objects()
coins.Id = pd.to_numeric(coins.Id)
coins = coins.set_index('Id', drop=False)


for index, coin in coins.iterrows():
    # Get coin quotes in USD
    try:
        if ('Litecoin (LTC)' != str(coin['FullName'])):
            continue;

        df1 = pd.DataFrame(MSFT)[:50]
        r = requests.get(HISTO_DAY_URL.format(coin.Symbol, 'USD')).json()
        df = pd.DataFrame(r['Data'])

        df['time'] = df['time'].apply(datetime.datetime.utcfromtimestamp).dt.date
        #df['just_date'] = df['time'].dt.date

        mids = (df.open + df.close) / 2
        spans = abs(df.close - df.open)

        inc = df.close > df.open
        dec = df.open > df.close
        w = 12 * 60 * 60 * 1000  # half day in ms

        output_file(str("charts\\" + coin['FullName']) + ".html")

        TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

        p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, toolbar_location="left")

        p.segment(df.time, df.high, df.time, df.low, color="black")
        p.rect(df.time[inc], mids[inc], w, spans[inc], fill_color="#D5E1DD", line_color="red")
        p.rect(df.time[dec], mids[dec], w, spans[dec], fill_color="#F2583E", line_color="blue")

        # p.title = "MSFT Candlestick"
        p.xaxis.major_label_orientation = pi / 4
        p.grid.grid_line_alpha = 0.3

        show(p)  # open a browser

    except Exception as e:
        print(e)

