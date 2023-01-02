# 繪製 [收盤價,最低價,最高價]統計圖表
# 日期使用西元年(110/01/01 -> 20210101)
import requests
import json
import csv
import pandas as pd
import os
import matplotlib.pyplot as plt

filename = 'stockmonth01.csv'
url_twse = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20210101&stockNo=2330'


# "110/01/01" -> 20210101
def convert_date(date):
    datestr = str(date)
    yearstr = datestr[:3] # 取出民國年
    realyear = str(int(yearstr)+1911)
    realdate = realyear + datestr[4:6] + datestr[7:9]
        
    return realdate    


if not os.path.isfile(filename):  # 如果檔案不存在就建立檔案
    resp = requests.get(url_twse)
    jdata = json.loads(resp.text) # 解析JSON
        
    
    outfile = open(filename,"w",encoding="utf-8")
    outwriter = csv.writer(outfile)
    
    outwriter.writerow(jdata["fields"])   
    for line in jdata["data"]:
        outwriter.writerow(line)
        
    outfile.close()
    
plt.rcParams["font.sans-serif"] = "mingliu"
pdstock = pd.read_csv(filename,encoding="utf-8")

for i in range(len(pdstock["日期"])):
    pdstock["日期"][i] = convert_date(pdstock["日期"][i])

pdstock["日期"] = pd.to_datetime(pdstock["日期"]) # 轉換成日期格式

pdstock.plot(kind="line", figsize=(12,6), x="日期", y=["收盤價","最低價","最高價"])



