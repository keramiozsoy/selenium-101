# test case 

# 1 open browser
#  2 go to file

from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
html_file = os.getcwd() + "/htmlPages/25_radio_button.html"
driver.get('file:///' + html_file)


# 3  zoom yap
driver.execute_script("document.body.style.zoom = '1.5' ") 
time.sleep(2)

element = driver.find_element_by_css_selector("input[value='male']")
element.click()


buttons.driver.find_element_by_css_selector('input')
for b in buttons:
        print('button:{} \t checked:{}'.format(b.get_attribute('value'))])  # tüm alanların değerlerini aldı for ile ekrana  bastı. eksik yazdın tamamla

driver.quit()
