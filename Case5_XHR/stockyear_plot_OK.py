
import requests
import json
import csv
import pandas as pd
import os
import time
import matplotlib.pyplot as plt
from plotly.offline import plot
import plotly.graph_objs as go

#plt.rcParams["axes.unicode_minus"]=False
plt.rcParams["font.sans-serif"] = "mingliu"
urlbase = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2021'  #網址前半
urltail = '01&stockNo=2330'  #網址後半
filename = 'stockyear2021_2330.csv'


def add_month(n): 
    if(n < 10):
        month = '0' + str(n)
    else:
        month = str(n)
        
    return month


def convert_date(date):  #民國日期為西元
    str1 = str(date)
    yearstr = str1[:3]  #取出民國年
    realyear = str(int(yearstr) + 1911)  #轉為西元年
    realdate = realyear + str1[4:6] + str1[7:9]  #組合日期
    return realdate

'''
if not os.path.isfile(filename):
    for i in range(1,13):
        url_twse = urlbase + add_month(i) + urltail    
        resp = requests.get(url_twse)
        jdata = json.loads(resp.text)
        
        outputfile = open(filename, "a", newline="", encoding="utf-8")
        outputwriter = csv.writer(outputfile)
        
        if i==1:
            outputwriter.writerow(jdata["fields"])
            
        for dataline in (jdata["data"]): 
            outputwriter.writerow(dataline)
            
        time.sleep(0.5)
            
    outputfile.close()
'''

dfstock = pd.read_csv(filename, encoding="utf-8")
for i in range(len(dfstock['日期'])):
    dfstock['日期'][i] = convert_date(dfstock['日期'][i])
    
dfstock['日期'] = pd.to_datetime(dfstock['日期'])
# dfstock.plot(kind="line",figsize=(12,6), x="日期", y=["收盤價","最低價","最高價"])

data=[
      go.Scatter(x=dfstock['日期'],y=dfstock['收盤價'],name='收盤價'),
      go.Scatter(x=dfstock['日期'],y=dfstock['最低價'],name='最低價'),
      go.Scatter(x=dfstock['日期'],y=dfstock['最高價'],name='最高價')
      ]
layout = go.Layout(title="2021年 2330股價走勢")
figure = go.Figure(data, layout)
plot(figure,filename = '2021_2330.html',auto_open=True)

