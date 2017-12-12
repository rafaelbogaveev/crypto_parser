
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
        # N = 300
        x = df['time']
        y = df['high']

        # output to static HTML file
        output_file(str("charts\\"+coin['FullName']) + ".html")

        # NEW: create a column data source for the plots to share
        source = ColumnDataSource(data=dict(x=x, y=y))

        TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select,lasso_select"

        # create a new plot and add a renderer
        left = figure(tools=TOOLS, width=700, height=700, x_axis_type="datetime", title=None)
        left.line('x', 'y', source=source)

        # put the subplots in a gridplot
        p = gridplot([[left]])
        save(p)

        time.sleep(1)

    except Exception as e:
        print(e)
