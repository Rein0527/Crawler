
urlbase = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2021'  #網址前半共同的部分
urltail = '01&stockNo=2330'  #網址後半共同的部分

#網址加入月份
def add_month(n):    
    if n < 10:
        month="0"+str(n)
    else:
        month = str(n)

    return month
  

for i in range(1, 13):  #取1到12數字
    url_twse = urlbase + add_month(i) + urltail  #組合網址
    print(url_twse)

'''
response=json&date=20210101&stockNo=2330
response=json&date=20210201&stockNo=2330
         :
         :
response=json&date=20211101&stockNo=2330
response=json&date=20211201&stockNo=2330
'''