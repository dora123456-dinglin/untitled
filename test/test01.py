from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('123')
driver.find_element_by_id('su').click()
driver.maximize_window()
print(driver.window_handles)
time.sleep(4)
driver.find_element_by_partial_link_text('123网址').click()
time.sleep(4)
dd=driver.window_handles
print(dd)
print(driver.current_window_handle)
winhands = driver.window_handles
driver.switch_to.window(winhands[-1])
time.sleep(3)
driver.close()
time.sleep(3)