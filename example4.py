# test case 

# 1 open browser
#  2 go to file

from selenium import webdriver
import os
import time

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
html_file = os.getcwd() + "/htmlPages/24_hoverable_dropdown.html"
driver.get('file:///' + html_file)


# 3 hover to 'mouse over me'
element = driver.find_element_by_css_selector('body > div > span')
ActionChains(driver).move_to_element(element).perform()

time.sleep(2)


# 4 clcik 'hello world'
element = driver.find_element_by_css_selector('body > div > div > div > p')
element.click()


driver.quit()