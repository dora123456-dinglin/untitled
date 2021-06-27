from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
driver=webdriver.Firefox()
driver.get("https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index")
time.sleep(4)
# a=driver.find_element_by_id("J_roomCountList")
# time.sleep(3)
# Select(a).select_by_value("3")
driver.execute_script("window.scrollTo(0,100000)")
text=driver.find_element_by_link_text("宾馆索引").text
print(text)
