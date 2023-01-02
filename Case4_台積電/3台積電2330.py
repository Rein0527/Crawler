# 台積電
# plt.rcParams["font.sans-serif"] = "mingliu"
import csv
import matplotlib.pyplot as plt

fn = 'FMNPTK_2330.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    listCsv = list(csvReader)                   # 轉成串列
    csvData = listCsv[2:-5]                     # 切片刪除非成交資訊
    years, highs, lows, prices = [], [], [], [] # 設定空串列
