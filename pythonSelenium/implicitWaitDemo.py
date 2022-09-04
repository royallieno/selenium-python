# Implicit wait
# Explicit wait
# pause the test for few seconds using Time class.

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome -
# service_object = Service("C:\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_object)

# Microsoft Edge -
service_object = Service("C:\\msedgedriver.exe")
driver = webdriver.Edge(service=service_object)
driver.implicitly_wait(5)
# Wait until 5 seconds if object is not displayed.
# Global wait.
# 1.5 second to reach next page - execution will resume in 1.5 seconds.
# If object do not show up at all, then max time your test waits for 5 seconds.

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys('ber')
time.sleep(5)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
print(count)
assert count > 0
# buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in results:
    button.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys('rahulshettyacademy')
# driver.find_element(By.CLASS_NAME, "promoCode").send_keys('hjdsfhujw')
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
