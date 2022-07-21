# Implicit wait
# Explicit wait
import time
from selenium import webdriver
# pause the test for few seconds using Time class.
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")


driver.find_element_by_css_selector("input.search-keyword").send_keys('ber')
time.sleep(5)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input.promoCode")))
driver.find_element_by_css_selector("input.promoCode").send_keys('rahulshettyacademy')
# driver.find_element_by_class_name("promoCode").send_keys('hjdsfhujw')
driver.find_element_by_css_selector("button.promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
print(driver.find_element_by_css_selector("span.promoInfo").text)
