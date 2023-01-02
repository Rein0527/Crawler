# 高鐵站名(中英文)
import requests, bs4

url = 'https://www.thsrc.com.tw/ArticleContent/a3b630bb-1066-4352-a1ef-58c7b4e8ef7c'
htmlfile = requests.get(url)
soup = bs4.BeautifulSoup(htmlfile.text, 'lxml')

temp = soup.find("select", id="select_location01")
stations = temp.find_all('option')

print("中文站名  英文站名")
for station in stations:
    if station['value']:
        print(station.text, "   :", station['value'])
