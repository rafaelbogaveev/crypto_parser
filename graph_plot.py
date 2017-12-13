from bokeh.plotting import *
from bokeh.models import ColumnDataSource
import datetime
import requests
import time
import pandas as pd


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

        if ('3DES (3DES)'==str(coin['FullName']) or 'Elite 888 (8S)'==str(coin['FullName'])
                or 'Advanced Browsing Token (ABT)'==str(coin['FullName']) or 'The Abyss (ABYSS)'==str(coin['FullName'])
                or 'TokenStars (ACE)' == str(coin['FullName']) or 'ACT (ACT)' == str(coin['FullName'])
                or 'Achain (ACT*)' == str(coin['FullName']) or 'Adbank (ADB)' == str(coin['FullName'])):
            continue

        print(str(coin['FullName']))

        r = requests.get(HISTO_DAY_URL.format(coin.Symbol, 'USD')).json()
        df = pd.DataFrame(r['Data'])

        df['time'] = df['time'].apply(datetime.datetime.utcfromtimestamp)

        df['coin'] = coin.Symbol
        df['coin_id'] = coin.Id

        # prepare some date
        x = df['time']
        y0 = df['high']
        y1 = df['low']
        y2 = df['open']
        y3 = df['close']

        # output to static HTML file
        output_file(str("charts\\"+coin['FullName']) + ".html")

        # NEW: create a column data source for the plots to share
        source = ColumnDataSource(data=dict(x=x, y0=y0, y1=y1, y2=y2, y3=y3))

        TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

        w = 12 * 60 * 60 * 1000  # half day in ms

        # create a new plot and add a renderer
        p = figure(tools=TOOLS, width=700, height=700, x_axis_type="datetime", title=None)

        p.line('x', 'y0', source=source, legend='high', color='blue')
        p.line('x', 'y1', source=source, legend='low', color='green')
        p.line('x', 'y2',  source=source, legend='open', color='black')
        p.line('x', 'y3', source=source, legend='close', color='black')

        #left.multi_line([df['time'], df['time'], df['time'], df['time']],
        #                [df['high'], df['low'], df['open'], df['close']],
        #                color=['red', 'green', 'blue', 'black'],
        #                legend=['high', 'low', 'open', 'close'])


        p = gridplot([[p]])
        save(p)

        time.sleep(1)

    except Exception as e:
        print(e)
