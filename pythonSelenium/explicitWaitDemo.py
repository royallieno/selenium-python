# Implicit wait and Explicit wait
# Pause the test for few seconds using Time class.

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
productsList = []

# Chrome -
# service_object = Service("C:\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_object)

# Microsoft Edge -
service_object = Service("C:\\msedgedriver.exe")
driver = webdriver.Edge(service=service_object)
driver.implicitly_wait(2)
# Global wait - Wait until 5 seconds if object is not displayed.
# 1.5 second to reach next page - execution will resume in 1.5 seconds.
# If object do not show up at all, then max time your test waits for 5 seconds.

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys('ber')
time.sleep(5)

# -----------------------Written same code in next for loop-----------------------------
# productsName = driver.find_elements(By.CSS_SELECTOR, "div[class='products'] div h4")
# for productsNameCount in productsName:
#     # print(productsNameCount.text)
#     productsList.append(productsNameCount.text)
# print(productsList)
# assert productsList == expectedList
# ---------------------------------------------------------------------------------------

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
print(count)
assert count > 0
# buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in results:
    productsList.append(button.find_element(By.XPATH, "h4").text)
    button.find_element(By.XPATH, "div/button").click()
assert productsList == expectedList

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Some Validation  - XPATH --> //tr/td[5]/p
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print(sum)
totalAmt = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == totalAmt

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys('rahulshettyacademy')
# driver.find_element(By.CLASS_NAME, "promoCode").send_keys('hjdsfhujw')
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

explicitWait = WebDriverWait(driver, 10)
explicitWait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

# Total Amount and Total After Discount comparing
discountAmt = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert sum and totalAmt > discountAmt
