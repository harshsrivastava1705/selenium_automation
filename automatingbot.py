from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
driver=webdriver.Chrome()
add='https://web.whatsapp.com/'
driver.get(add)
wait=WebDriverWait(driver, 60)
sleep(6)
user=wait.until(EC.presence_of_element_located((By.XPATH,"//span[@title='{}']".format("//enter contact name here"))))
user.click()


for i in range(0,6,1):
    text=wait.until(EC.presence_of_element_located((By.CLASS_NAME,'_2A8P4')))
    text.send_keys("HIIIIIIIIIIII " *(i+1))
    send=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#main > footer > div.vR1LG._3wXwX.copyable-area > div:nth-child(3) > button > span')))
    send.click()
    sleep(0.5)
