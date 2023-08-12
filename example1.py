# Test case description:

# 1 : open browser
# 2 : go to python.org
# 3 : web page title containe ewords python

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.python.org/')
assert 'python' in driver.title.lower()
#assert 'kek' in driver.title.lower()
driver.execute_script("document.body.style.zoom='1.5'")
driver.quit()
