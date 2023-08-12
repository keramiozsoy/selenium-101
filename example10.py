from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

class MyListener(AbstractEventListener):
    def before_navigate_to(self,url,driver):
        print("log : before navigate to {} ".format(url))
    def after_navigate_to(self,url,driver):
        print("log : after navigate to {} ".format(url))



driver = webdriver.Chrome()
ef_driver = EventFiringWebDriver(driver, MyListener())
ef_driver.get("http://python.org")
driver.close()


bernagokce92@gmail.com