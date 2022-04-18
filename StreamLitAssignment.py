#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 20:49:42 2022

@author: nishanthkarthikviswanathan
"""
import pandas as pd
import requests
import streamlit as st

st.title("Bitcoin Prices")

radio_btn = st.radio('Currency',('cad','usd','inr'))
slider_bth = st.slider("No of Days",min_value=1,max_value=365)
Crpyto = st.radio("Choose Crypto", ('Bitcoin','Dogecoin'))
API_URL='https://api.coingecko.com/api/v3/coins/{}/market_chart?vs_currency={}&days={}&interval=daily'.format(Crpyto.lower(), radio_btn,slider_bth)


req = requests.get(API_URL)

if req.status_code == 200:
    data = req.json()
    
raw_data = data['prices']

#print(raw_data)


df = pd.DataFrame(data=raw_data, columns=['date',radio_btn])
df['date']= pd.to_datetime(df['date'],unit='ms')
df=df.set_index('date')


st.line_chart(df)
Average_price = df[radio_btn].mean()
st.write("Average Price during this time {} {}".format(Average_price,radio_btn))