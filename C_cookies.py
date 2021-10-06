from selenium import webdriver

#imports for selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#google chrome webdriver

driver = webdriver.Chrome()
driver.get("https://chykalophia.com/")

driver.maximize_window()

#clicking on the button to go to linkedin
cookies_btn = driver.find_element_by_xpath('//div[2]//p/a[2]')
cookies_btn.click()

element = driver.find_element_by_xpath('//div[2]//p/a[2]')
if element.is_displayed():
    print("Passed")
else:
    print("Failed")


driver.quit()
