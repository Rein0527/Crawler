from selenium import webdriver
from selenium.webdriver.common.by import By

# 高鐵時刻表查詢網站
#url = 'http://www.thsrc.com.tw/tw/TimeTable/SearchResult'
url = 'https://www.thsrc.com.tw/ArticleContent/a3b630bb-1066-4352-a1ef-58c7b4e8ef7c'

ss='台北站'      #出發站
es='台中站'      #到達站

# 建立瀏覽器物件開啟網站
driver_path = 'drivers/geckodriver'
driver = webdriver.Firefox(executable_path=driver_path)

driver.get(url)
#按我同意
driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
#輸入出發站
driver.find_element(By.ID,'select_location01').send_keys(ss) 
# #輸入到達站
driver.find_element(By.ID,'select_location02').send_keys(es)   
#輸入日期
driver.find_element(By.ID,"Departdate03").click()
driver.find_element(By.XPATH, "//div[@id='tot-1']/div/div/ul/li/div/div/table/tbody/tr[2]/td[1]").click()
# #輸入時間
driver.find_element(By.ID,"outWardTime").click()
driver.find_element(By.XPATH, "//div[@id='tot-1']/div[2]/div/ul/li[2]/div/div/table/tr[3]/td[3]/a/i").click()
driver.find_element(By.ID,'start-search').click() #按查詢鈕