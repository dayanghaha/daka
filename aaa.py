from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

def daka():
    driver = webdriver.Chrome()
    driver.get('https://sso.wecash.net/login')
    driver.find_element_by_xpath('//*[@id="login-input"]').click()
    driver.find_element_by_xpath('//*[@id="login-input"]').send_keys('fengbo')
    driver.find_element_by_xpath('//*[@id="login-password"]').click()
    driver.find_element_by_xpath('//*[@id="login-password"]').send_keys('Liushanshan519!')
    driver.find_element_by_xpath('//*[@id="wrapper"]/div/form/button').click()
    driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[2]/div[1]/div[3]/div/div[1]/a/div[2]/span').click()
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[2]/div[4]/table/tbody/tr/td/h2/strong').click()
    time.sleep(6)
    texts=driver.switch_to_alert().text
    result="成功" in texts
    if result==True:
        driver.close()
    else:
        driver.close()
        daka()

daka()



