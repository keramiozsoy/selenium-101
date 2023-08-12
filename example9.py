# sayfadaki button ile açılan pop up taki butoan basmak

from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
html_file = os.getcwd() + "/htmlPages/33.html" # page.html diye bir sayfa yoktur
driver.get('file:///' + html_file)



driver.find_element_by_css_selector("button").click()
time.sleep(1)

driver.switch_to_alert().accept()
time.sleep(1)

driver.close()
time.sleep(1)

driver.close()