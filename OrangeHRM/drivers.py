import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:/Users/Admin/Desktop/Drivers/chromedriver/chromedriver.exe")

driver.implicitly_wait(6)

driver.get("https://www.facebook.com/login/")

forgot_link = driver.find_element(By.XPATH, "//a[contains(text(),'Forgotten account?')]")

ele = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(forgot_link))

ele.click()

print(driver.title)





