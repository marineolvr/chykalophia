from selenium import webdriver

#imports for selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


#google chrome webdriver
driver = webdriver.Chrome()
driver.get("https://chykalophia.com/")

driver.maximize_window()


#Checking email field newsletter
email_input = driver.find_element_by_xpath('//*[@id="ff_3_email"]')
email_input.clear()
email_input.send_keys("marineolvera07@gmail.com")




#newsletter
email_btn = driver.find_element_by_xpath('//*[@id="ff_3_email"]')
email_btn.click()
#wd_wait = WebDriverWait(driver, 10)
#email_btn = wd_wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ff_3_email"]')))

element = driver.find_element_by_xpath('//*[@id="ff_3_email"]')
if element.is_displayed():
    print("Passed")
else:
    print("Failed")


driver.quit()
