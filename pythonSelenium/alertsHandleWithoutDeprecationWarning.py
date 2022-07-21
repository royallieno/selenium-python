from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

validateText = 'Gulnawaz Arshad'
validateTextOne = 'Aaira Arshad'

# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver_service = Service(executable_path="C:\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# driver.find_element_by_css_selector("#name").send_keys(validateText)
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(validateText)

# driver.find_element_by_id("alertbtn").click()
driver.find_element(By.ID, "alertbtn").click()
# driver.find_element_by_xpath("//input[@id='alertbtn']").click()

alert = driver.switch_to.alert
print(alert.text)
alertText = alert.text
assert validateText in alertText
alert.accept()


# driver.find_element_by_css_selector("#name").send_keys(validateText)
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(validateText)
# driver.find_element_by_id("confirmbtn").click()
driver.find_element(By.ID, "confirmbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alertText = alert.text
assert validateTextOne in alertText
alert.dismiss()
