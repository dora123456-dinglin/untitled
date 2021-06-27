from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get('https://www.baidu.com')
time.sleep(5)
# driver.find_element_by_class_name('s_ipt').send_keys('nihao')
# time.sleep(6)
# driver.find_element_by_id('su').click()
# title=driver.title
# driver.refresh()
# driver.find_element_by_css_selector("input#kw").send_keys('nihao')
# driver.find_element_by_xpath("//input[@value='百度一下']").click()
# time.sleep(5)
# driver.find_element_by_css_selector("input#kw").clear()
# size=driver.find_element_by_css_selector("input#kw").size
# print(size)
text=driver.find_element_by_xpath("//input[@value='百度一下']").get_attribute('value')
print(text)
# driver.back()
# time.sleep(3)
# driver.forward()
# time.sleep(3)
# driver.set_window_size(600,300)
# time.sleep(3)
# driver.maximize_window()
# text=driver.find_element_by_link_text('新闻').text
# print(text)