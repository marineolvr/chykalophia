from selenium import webdriver

#imports for selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#google chrome webdriver
driver = webdriver.Chrome()
driver.get("https://chykalophia.com/")

driver.maximize_window()

#clicking on the button to go to git
git_btn = driver.find_element_by_xpath('//section[2]//span[6]/a')
git_btn.click()

#wd_wait = WebDriverWait(driver, 10)
#git_btn = wd_wait.until(EC.visibility_of_element_located((By.XPATH, "//section[2]//span[6]/a")))

element = driver.find_element_by_xpath('//section[2]//span[6]/a')
if element.is_displayed():
    print("Passed")
else:
    print("Failed")

driver.quit()
