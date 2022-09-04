import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

validateText = 'Gulnawaz Arshad'
validateTextOne = 'Aaira Arshad'

# Chrome -
# service_object = Service("C:\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_object)

# Microsoft Edge -
service_object = Service("C:\\msedgedriver.exe")
driver = webdriver.Edge(service=service_object)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(validateText)
driver.find_element(By.ID, "alertbtn").click()
# driver.find_element_by_xpath("//input[@id='alertbtn']").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert validateText in alertText
alert.accept()


driver.find_element(By.CSS_SELECTOR, "#name").send_keys(validateText)
driver.find_element(By.ID, "confirmbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert validateTextOne in alertText
alert.dismiss()
