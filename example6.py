# test case assertion

# 1 open browser
#  2 go to file
# bir sayfanın açılıp açılabamayacağını assert ettiğimiz kod

from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
html_file = os.getcwd() + "/htmlPages/page.html" # page.html diye bir sayfa yoktur
driver.get('file:///' + html_file)


# 3  zoom yap
try:
        assert 'your file was not found' not in driver.page_source
except AssertionError:
        print('error page not found check url')

time.sleep(2)

driver.quit()
