from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
driver.get('https://www.163.com/')
time.sleep(7)
aa=driver.find_element_by_link_text('登录')
ActionChains(driver).move_to_element(aa).perform()
time.sleep(3)
dd=driver.find_element_by_css_selector("div#js_N_login_wrap>iframe")
driver.switch_to.frame(dd)
driver.find_element_by_xpath("//div[@id='account-box']/div[2]/input").send_keys('123')
time.sleep(3)
# driver.get_screenshot_as_file(r'C:\Users\maydaydream18\Desktop\test01.png')


# driver.find_element_by_id('q').send_keys('nihao')
# time.sleep(3)
# driver.find_element_by_id('q').send_keys(Keys.BACK_SPACE)

# lel=driver.find_element_by_css_selector('.service-bd>li')
# ActionChains(driver).move_to_element(lel).perform()
# time.sleep(3)
# driver.find_element_by_link_text('女装').click()
# time.sleep(5)
# print(driver.window_handles)
# print(driver.current_window_handle)
# dd=driver.window_handles
# driver.switch_to.window(dd[1])
# time.sleep(7)
# print(driver.current_window_handle)
