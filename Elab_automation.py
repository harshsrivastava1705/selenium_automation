from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException,ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions

driver=webdriver.Chrome()


webpage='https://care.srmist.edu.in/srmktrada/student/questions'
driver.get(webpage)
username=driver.find_element_by_xpath('//*[@id="mat-input-0"]')
username.send_keys(input("Enter Registeration Number: "))
password=driver.find_element_by_xpath('//*[@id="mat-input-1"]')
password.send_keys(input("Enter password: "))
login=driver.find_element_by_xpath('/html/body/app-root/div/app-login/div/mat-card/div[2]/form/button')
login.click()
time.sleep(2)
questions=driver.find_element_by_xpath('/html/body/app-root/div/app-student-home/div/mat-card/div/div/app-student-home-card')
questions.click()
time.sleep(2)
main=driver.find_element_by_tag_name('g')
q=main.find_elements_by_tag_name('path')
i,f=0,-1
for i in range(100,1,-1):
    ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,ElementClickInterceptedException,)
    question = WebDriverWait(driver,3,ignored_exceptions=ignored_exceptions)\
                        .until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#svgChart > g > g:nth-child(4) > path:nth-child({q})".format(q=i))))
    
    question.click()
    time.sleep(0.4)
    a= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[1]/mat-form-field/div/div[1]/div')))
    a.click()
    time.sleep(0.4)    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/div[2]/div/div/mat-option[2]/span"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[2]/div[2]/mat-card/div[3]/button[2]"))).click()
    div=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[2]/div[2]/mat-card/div[4]/a[1]")))
    if(div.value_of_css_property('background-color')=="rgba(255, 0, 0, 1)") :
        driver.back()
        time.sleep(2)
        continue
    elif(div.value_of_css_property('background-color')=="rgba(0, 128, 0, 1)") :
        time.sleep(0.5)
        my_element_id = '/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[2]/div[2]/mat-card/div[4]/a[2]'
        ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
        download = WebDriverWait(driver,3,ignored_exceptions=ignored_exceptions)\
                        .until(expected_conditions.presence_of_element_located((By.XPATH, my_element_id)))
        download.click()
        time.sleep(2)
        driver.back()
    else:
        print (f"problem {i}")
        while(div.value_of_css_property('background-color')=="rgba(255, 179, 0, 1)"):
            driver.find_element_by_xpath('/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[2]/div[2]/mat-card/div[3]/button[2]').click()
            time.sleep(3)
            div=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[2]/div[2]/mat-card/div[4]/a[1]")))
        my_element_id = '/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[2]/div[2]/mat-card/div[4]/a[2]'
        ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,ElementClickInterceptedException,)
        download = WebDriverWait(driver,3,ignored_exceptions=ignored_exceptions)\
                        .until(expected_conditions.presence_of_element_located((By.XPATH, my_element_id)))
        download.click()
        time.sleep(2)
        driver.back()
        
    #while(driver.find_element_by_xpath('/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[2]/div[2]/mat-card/div[4]/a').value_of_css_property('background-color') == "rgb(255, 179, 0)"):
    #    driver.find_element_by_xpath('/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[2]/div[2]/mat-card/div[3]/button[2]').click()
    #driver.find_element_by_xpath('/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[2]/div[2]/mat-card/div[4]/a[2]').click()
    #time.sleep(1)
    #driver.back()
    #time.sleep(1.5) 
    
