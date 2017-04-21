import ConfigStart
from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get(ConfigStart.STARTURL)
#data = driver.page_source
inputs = driver.find_element_by_css_selector("lallrace_nav")
print inputs
driver.quit()