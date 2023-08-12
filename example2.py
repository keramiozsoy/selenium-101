# test case description:
# 1 open a browser
# 2 go to 23.htmlfile

from selenium import webdriver
import os
import time
driver = webdriver.Chrome()
html_file = os.getcwd() + "/htmlPages/23.html"
driver.get('file:///' + html_file)

# 3 check 'I have a blue'

element = driver.find_element_by_css_selector('body > form:nth-child(1) > input[type=checkbox]:nth-child(1)')
element.click()


element.get_attribute('checked') # seçili element gerçekten seçilmiş mi ?
time.sleep(2)


# 4 un checked 'I have a blue'
element.click()
element.get_attribute('checked') # seçili element gerçekten seçilmiş mi ?
time.sleep(2)

# 5 ichek button is enabled or not 
button = driver.find_element_by_css_selector('#disabled_button')
button.click()
button.is_enabled()
time.sleep(2)


# 6 click 'click me' button
button = driver.find_element_by_css_selector('body > button:nth-shild(4)')
button.is_enabled()
time.sleep(2)

# 7 send_keys
text_field = driver.find_element_by_css_selector('body > form:nth-child(11) > input[type=text]:nth-child(8)')
text_field.send_keys('kerami')
time.sleep(2)

# 8 clear text field 
text_field.clear()
time.sleep(2)

driver.quit()






