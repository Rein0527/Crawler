#將 JSON 存成 CSV
import requests
import json
import csv
#import pandas as pd
import os

filename = 'stockmonth01.csv'
url_twse = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20210101&stockNo=2330'


if not os.path.isfile(filename):  #如果檔案不存在就建立檔案
    resp = requests.get(url_twse)
    jdata = json.loads(resp.text) #解析JSON
    
    
    outfile = open(filename,"w",encoding="utf-8")
    outwriter = csv.writer(outfile)
    
    outwriter.writerow(jdata["fields"])
    
    for line in jdata["data"]:
        outwriter.writerow(line)
        
    outfile.close()