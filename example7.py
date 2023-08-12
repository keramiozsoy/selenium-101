

from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
driver.get('https://www.python.org/')



# explicity wait kullanamak 
# about kısmının görülüp görülmediğini 10 saniye boyunca kontrol edicem
# 10 saniye içinde 1 saniyede gözükürse kod akışına devam eder. eğer 11. saniye olursa
# hemen hata fırlatılıp durulur.
# time.sleep(10) kullanmamak için bunu yaptık çünkü bu ne olurs olsun hep 10 sn bekler.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# element = WebDriverWait(driver,10).until(EC.presence_of_element_located(By.ID,"about")) # çalışmıyo düzelt :)
# element = WebDriverWait(driver,10).until(EC.presence_of_element_located(By.ID,"kek")) olmadığı için hata verecek
element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"about")))


# resim çekmek istediniz hemen çekelim.
driver.save_screenshot('screen_shot/ex1.png')

time.sleep(2)

driver.quit()
