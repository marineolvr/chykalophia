
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
behance_btn = driver.find_element_by_xpath('//div[2]//span[7]/a')
behance_btn.click()
#wd_wait = WebDriverWait(driver, 10)
#behance_btn = WebDriverWait.until(EC.visibility_of_element_located((By.XPATH, '//div[2]/ul[1]/li[1]/a/div')))


element = driver.find_element_by_xpath("//div[2]//span[7]/a")
if element.is_displayed():
    print("Passed")
else:
    print("Failed")

driver.quit()
