from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s=Service('D:/coding/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://www.smartprix.com/mobiles')
time.sleep(2)
exclude_outof_stock = driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input')
exclude_outof_stock.click()
time.sleep(2)
exclude_outof_upcoming = driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input')
exclude_outof_upcoming.click()
time.sleep(2)

old_height = driver.execute_script('return document.body.scrollHeight')
 
while True:
    driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    print(old_height,new_height)
    if new_height==old_height:
        break
    old_height=new_height



html = driver.page_source
with open('smartprix.html','w',encoding='utf-8') as w:
    w.write(html)







