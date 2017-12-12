import json
import requests
import sqlalchemy as sa
import pandas as pd
import datetime
import time

ICO_LIST_URL = "https://www.cryptocompare.com/api/data/icolist/"

json_response = requests.get(ICO_LIST_URL).json()
ico_list= pd.DataFrame(json_response['Data']).T

ico_list.Id = pd.to_numeric(ico_list.Id)
ico_list = ico_list.set_index('Id', drop=False)

engine = sa.create_engine('mysql+pymysql://root:1234@127.0.0.1/crypto_coins?charset=utf8', encoding='utf8')

# Save parsed coins to MySQL database
ico_list.to_sql('ico_alternative', engine, if_exists='replace', index=False)