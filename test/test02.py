from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("file:///E:\\")
time.sleep(7)
driver.switch_to.alert.dismiss()