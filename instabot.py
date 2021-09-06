from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException,ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions

driver=webdriver.Chrome()
wait=WebDriverWait(driver, 60)

webpage='https://instagram.com'
driver.get(webpage)

user=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"loginForm\"]/div/div[1]/div/label/input")))
user.send_keys("zeus2.0._")
password=driver.find_element_by_xpath("//*[@id=\"loginForm\"]/div/div[2]/div/label/input")
password.send_keys("Pnah8726")
driver.find_element_by_xpath("//*[@id=\"loginForm\"]/div/div[3]/button").click()
otp=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"react-root\"]/section/main/div/div/div[1]/div/form/div[1]/div/label/input")))
s=input("Enter OTP")
otp.send_keys(s)
driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div/div[1]/div/form/div[2]/button").click()
dm=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a")))
dm.click()
user=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a")))
user.click()
time.sleep(2)
textb=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")))
for i in range(15):
    textb.send_keys("\"They say Baby Shark dodo\" but never \"Do the baby shark do? :(\"")
    time.sleep(1)
    send=driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
    send.click()




