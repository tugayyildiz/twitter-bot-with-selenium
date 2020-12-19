from selenium import webdriver
import loginInfo #CREATE LOGININFO PYTHON FOLDER AND ENTER YOUR USERNAME AND PASSWORD
import time

browser = webdriver.Firefox()
browser.get("https://twitter.com/")
time.sleep(3)

#PLEASE PASTE YOUR BROWSER XPATH 
giris_yap = browser.find_element_by_xpath("//*[@id='doc']/div/div[1]/div[1]/div[2]/form/div[3]/div/p/a")
giris_yap.click()
time.sleep(5)

username = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")
password = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")
username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

time.sleep(3)

login = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button")
login.click()
