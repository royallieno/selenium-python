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

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# Checkbox handled as per the dynamic logic
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute('value') == 'option1':
        checkbox.click()
        assert checkbox.is_selected()
        break
time.sleep(3)

# Checkbox handled as per the static logic
staticCheckboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
staticCheckboxes[2].click()
assert staticCheckboxes[2].is_selected()

# Radio button handled as per the dynamic logic
dynamicradioButtons = driver.find_elements(By.CLASS_NAME, "radioButton")
print(len(dynamicradioButtons))
for dynamicradioButton in dynamicradioButtons:
    if dynamicradioButton.get_attribute('value') == 'radio3':
        dynamicradioButton.click()
        assert dynamicradioButton.is_selected()
        break
time.sleep(3)

# Radio button handled as per the static logic
radioButtons = driver.find_elements(By.CLASS_NAME, "radioButton")
radioButtons[0].click()
assert radioButtons[0].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
