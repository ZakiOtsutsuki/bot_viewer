#Version 1.1
#need to add proxy

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
count = 0

def login(t):
    browser.get("https://stackoverflow.com/")
    time.sleep(t)
    login_button = browser.find_elements_by_xpath("/html/body/header/div/ol[2]/li[2]/a[1]")[0]
    login_button.click()
    time.sleep(t)
    google_button = browser.find_elements_by_xpath("/html/body/div[4]/div[2]/div/div[2]/button[1]")[0]
    google_button.click()
    time.sleep(t)
    acount_name = browser.find_elements_by_name("identifier")[0]
    acount_name.send_keys("naruto1745uzumaki")
    acount_name.send_keys(Keys.ENTER)
    time.sleep(t)
    password = browser.find_elements_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")[0]
    password.send_keys("arafi1745")
    password.send_keys(Keys.ENTER)
    time.sleep(15)

def video(link, t):
    browser.get(link)
    webdriver.ActionChains(browser).key_down(Keys.SPACE).perform()
    time.sleep(t)

login(5)

while count < 1:
    video("https://youtu.be/Z_G_BpPzGIE", 130)
    video("https://www.youtube.com/watch?v=VLpFgay9ZWY", 135)
    video("https://www.youtube.com/watch?v=UFwQZ7od4tY", 200)
    video("https://youtu.be/pE2j1W_QO0A", 860)
    count = count + 1

browser.close()