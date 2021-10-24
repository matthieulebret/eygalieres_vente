import streamlit as st
import altair as alt

from seleniumwire import webdriver

from bs4 import BeautifulSoup
import requests
import pandas as pd

import numpy as np
import pandas as pd
import datetime
import time
import calendar
from datetime import date, timedelta
import xlrd
import openpyxl


# from selenium import webdriver



st.set_page_config('Vente Eygalieres',layout='wide')

st.title('Visites Eygalieres')




@st.cache(suppress_st_warning=True,ttl=3600)
def getupdates():
    propurl = 'https://api.m-oi.fr/api/Properties/GetProperties'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.5",
            "Content-Type": "application/json-patch+json",
            "Access-Control-Allow-Origin": "*",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site"}
    params = {
        "credentials": "include",
        "referrer": "https://www.m-oi.fr/",
        "method": "POST",
        "mode": "cors"}
    body = "{\"agentsList\":[129],\"SearchLength\":100000,\"Visible\":true,\"StatutsAvancement\":[1,3,5],\"StartSearchIndex\":0}"
    r = requests.post(propurl,headers = headers,json=params,data=body)
    data = r.json()
    reflist = ['B482445-AAG','B482444-AAG','B482312-AAG']
    data = [data['Properties'][i] for i in [0,1,3]]
    return data


df = getupdates()

st.image('https://www.m-oi.fr/img/properties/100076/terrain-1-piece-a-eygalieres--13810-_2.jpg')

st.header('Terrain 1')
col1,col2 = st.columns(2)
with col1:
    st.metric('Surface m2','{:,.0f}'.format(df[0]['OutdoorSurface']))
with col2:
    st.metric('Prix de vente eur','{:,.0f}'.format(df[0]['NetVendeur']))
st.subheader('Visites')

if df[0]['Visits']:
    visitdf = pd.DataFrame(df[0]['Visits']).iloc[:,2:]
else:
    visitdf = 'N/A'
visitdf

st.image('https://www.m-oi.fr/img/properties/100075/terrain-1-piece-a-eygalieres--13810-_1.jpg')

st.header('Terrain 2')
col3,col4 = st.columns(2)
with col3:
    st.metric('Surface m2','{:,.0f}'.format(df[1]['OutdoorSurface']))
with col4:
    st.metric('Prix de vente eur','{:,.0f}'.format(df[1]['NetVendeur']))

st.subheader('Visites')
if df[1]['Visits']:
    visitdf = pd.DataFrame(df[1]['Visits']).iloc[:,2:]
else:
    visitdf = 'N/A'
visitdf

st.image('https://www.m-oi.fr/img/properties/99935/mazet-a-eygalieres_1.jpg')
st.header('Maison')
col5,col6 = st.columns(2)
with col5:
    st.metric('Surface m2','{:,.0f}'.format(df[2]['OutdoorSurface']))
with col6:
    st.metric('Prix de vente eur','{:,.0f}'.format(df[0]['NetVendeur']))
st.subheader('Visites')
if df[2]['Visits']:
    visitdf = pd.DataFrame(df[2]['Visits']).iloc[:,2:]
else:
    visitdf = 'N/A'
visitdf


with st.expander('Show data'):
    df
