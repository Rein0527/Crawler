import requests

#開放資料：'YouBike新北市公共自行車即時資訊'
url = "https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json"
html_content = requests.get(url)

json_data = html_content.json()   #將回傳內容轉換成json格式

'''
#資料欄位說明
sno：站點代號
sna：場站名稱(中文)
tot：場站總停車格
sbi：場站目前車輛數量
sarea：場站區域(中文)
mday：資料更新時間
lat：緯度
lng：經度
ar：地(中文)
sareaen：場站區域(英文)
snaen：場站名稱(英文)
aren：地址(英文)
bemp：空位數量
act：全站禁用狀態 
'''

for item_detail in json_data:
    print_info = "場站名稱:"+item_detail["sna"]+",空位數量:"+item_detail["bemp"]
    print_info += ",總停車格:"+item_detail["tot"]+",資料更新時間:"+item_detail["mday"] 
    print(print_info)