from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browserSortedVeggies = []
service_object = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
# Click on the column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
# Collect all veggie names -> browserSortedVeggies (A, B, C)
veggieWebElements = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(1)")
for veggies in veggieWebElements:
    browserSortedVeggies.append(veggies.text)

sortedList = browserSortedVeggies.copy()
print(browserSortedVeggies)
print(sortedList)
# sort the browserSortedVeggies == newSortedList -> (A, B, C)
browserSortedVeggies.sort()
assert browserSortedVeggies == sortedList
