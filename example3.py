# test case 

# 1 open browser
#  2 go to file

from selenium import webdriver
import os
import time
driver = webdriver.Chrome()
html_file = os.getcwd() + "/htmlPages/24_clickable_dropdown.html"
driver.get('file:///' + html_file)

# 3 click dropdown button

dropdown = driver.find_element_by_css_selector('body > div > button')
dropdown.click()
time.sleep(2)


# 4 click about button
element = driver.find_element_by_css_selector('#myDropdown > a:nth-child(2)')
element.click()
time.sleep(2)


driver.quit()


