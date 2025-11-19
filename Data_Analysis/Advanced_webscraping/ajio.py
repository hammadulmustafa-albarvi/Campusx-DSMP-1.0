# import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--force-device-scale-factor=0.9")
s = Service('D:/coding/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=s,options=options)

driver.get('https://www.ajio.com/men-fashion-bags/c/830201004')
time.sleep(25)
old_height = driver.execute_script('return document.body.scrollHeight')

counter = 1
while True:

    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(12)

    new_height = driver.execute_script('return document.body.scrollHeight')

    print(counter)
    counter += 1
    print(old_height)
    print(new_height)

    if new_height == old_height:
        break

    old_height = new_height


# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# # time.sleep(2)
# driver = uc.Chrome()  
# # time.sleep(2)
# # driver.get('http://google.com')

# # time.sleep(2)

# driver.get('https://www.ajio.com/men-fashion-bags/c/830201004')
# # time.sleep(2) 
# old_height = driver.execute_script('return document.body.scrollHeight')

# counter = 1
# while True:
#     driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#     time.sleep(2)

#     new_height = driver.execute_script('return document.body.scrollHeight')

#     print(counter)
#     counter += 1
#     print(old_height)
#     print(new_height)

#     if new_height == old_height:
#         break

#     old_height = new_height