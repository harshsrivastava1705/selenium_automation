from selenium import webdriver
from time import sleep
import string
from threading import Thread
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def prog(q):
        driver=webdriver.Chrome()
        wait=WebDriverWait(driver,10)
        ####insert your link here###
        driver.get(q)
        ####insert your link here^###
        play=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="movie_player"]/div[5]/button')))
        sleep(2)
        play.click()
        sleep(35)
        driver.close()

def create(n):
    l=input("Enter link to the video: ")
    for i in range(n):
        t = Thread(target = prog,args=(l,))
        t.start()        
        
n=int(input("Enter number of views: " ))
create(n) 