import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = uc.Chrome()  
driver.get('http://google.com')

time.sleep(2)
user_input = driver.find_element(By.NAME, "q")
user_input.send_keys('CampusX')
time.sleep(2)
user_input.send_keys(Keys.ENTER)
time.sleep(2)
link = driver.find_element(by=By.XPATH,value='/html/body/div[3]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a')
link.click()
time.sleep(2)
link2 = driver.find_element(by=By.XPATH,value='/html/body/div[6]/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[2]/a[2]')
link2.click()