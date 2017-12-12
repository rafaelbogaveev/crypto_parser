import requests
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from routines import *


ICO_LIST_URL = "https://www.cryptocompare.com/api/data/icolist/"

json_response = requests.get(ICO_LIST_URL).json()

ico_list = json_response['Data']

engine = sa.create_engine("mysql+pymysql://root:1234@127.0.0.1/crypto_coins?charset=utf8", encoding='utf8')
session = sessionmaker(bind=engine)()

for item in ico_list:
    ico = getIco(ico_list, item)

    ico = session.merge(ico)


session.commit()