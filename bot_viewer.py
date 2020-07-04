#Version 1.0
#need to add proxy

from selenium import webdriver
import time

browser = webdriver.Firefox()
count = 0

while count < 1:
    browser.get("https://youtu.be/Z_G_BpPzGIE")
    play_button = browser.find_elements_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[23]/div[2]/div[1]/button")[0]
    play_button.click()
    time.sleep(130)
    count = count + 1