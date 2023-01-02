# 台積電簡史
import requests
import bs4

url_tsmc = 'https://zh.wikipedia.org/wiki/%E5%8F%B0%E7%81%A3%E7%A9%8D%E9%AB%94%E9%9B%BB%E8%B7%AF%E8%A3%BD%E9%80%A0'
tsmchtml = requests.get(url_tsmc)
soup = bs4.BeautifulSoup(tsmchtml.text, 'lxml')

tsmc = soup.find("table",class_="infobox vcard")

temp = tsmc.find_all("tr") 

for t in temp:   
    col=t.find("th", class_="fn org")
    if col != None:
        print(col.text)
    col=t.find("th", scope="row")
    if col !=None:
        print(col.text,": ",end="")
        
    col=t.find("td")
    if col !=None:
        print(col.text) 
        