# Implicit wait
# Explicit wait
# pause the test for few seconds using Time class.
import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.implicitly_wait(5)
# Wait until 5 seconds if object is not displayed.
# Global wait.
# 1.5 second to reach next page - execution will resume in 1.5 seconds.
# If object do not show up at all, then max time your test waits for 5 seconds.

driver.find_element_by_css_selector("input.search-keyword").send_keys('ber')
time.sleep(5)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element_by_css_selector("input.promoCode").send_keys('rahulshettyacademy')
# driver.find_element_by_class_name("promoCode").send_keys('hjdsfhujw')
driver.find_element_by_css_selector("button.promoBtn").click()
print(driver.find_element_by_css_selector("span.promoInfo").text)
