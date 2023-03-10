# 台積電
import csv
import matplotlib.pyplot as plt


filename = 'FMNPTK_2330.csv'
with open(filename) as csvFile:
    csvReader = csv.reader(csvFile)
    listCsv = list(csvReader)                   # 轉成串列
    csvData = listCsv[2:-5] 
    print(csvData)                    # 切片刪除非成交資訊
    years, highs, lows, prices = [], [], [], [] # 設定空串列
    for row in csvData:
        try:
            year = int(row[0]) + 1911
            high = float(row[4])                # 設定最高價
            low = float(row[6])                 # 設定最低價
            price = float(row[8])               # 設定收盤平均價
        except Exception:
            print('有缺值')
        else:
            highs.append(high)                  # 儲存最高價
            lows.append(low)                    # 儲存最低價
            prices.append(price)                # 儲存收盤平均價
            years.append(year)                  # 儲存日期
       
fig = plt.figure(dpi=80, figsize=(12, 8))       # 設定繪圖區大小
plt.plot(years, highs, '-*', label='High')      # 繪製最高價
plt.plot(years, lows, '-o', label='Low')        # 繪製最低價
plt.plot(years, prices, '-^',   label='Price')  # 繪製收盤平均價
plt.legend(loc='best')
 # 日期旋轉
#fig.autofmt_xdate()                        
plt.rcParams["font.sans-serif"] = "mingliu"
plt.title("台積電近年股價走勢", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel("Price", fontsize=14)
plt.tick_params(axis='both', labelsize=12, color='red')
plt.show()
