from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

productsList = []
locationsList = []
service_object = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
# Regular Expression -
# XPATH - //a[contains(@href, 'shop')] || CSS - a[href*='shop']
# driver.find_element(By.LINK_TEXT, "Shop").click()
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
print(len(products))

for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    # productsList.append(productName)
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()
# print(productsList)
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("in")

# ------------------------Scenario with Explicit wait and without for loop-------------------------------
explicitWait = WebDriverWait(driver, 10)
explicitWait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
successText = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success!" in successText
print(successText)
# -------------------------------------------------------------------------------------------------------

# --------------------Same scenario with for loop and without explicit wait------------------------------
# deliveryLocation = driver.find_elements(By.CSS_SELECTOR, "div[class='suggestions'] ul")
# print(len(deliveryLocation))
# for locations in deliveryLocation:
#     # locationsList.append(locations.text)
#     if locations.text == "India":
#         locations.click()
#         break
# # print(locationsList)
# driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
# driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
# successText = driver.find_element(By.CLASS_NAME, "alert-success").text
# assert "Success!" in successText
# ----------------------------------------------------------------------------------------------------
