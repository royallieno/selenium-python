from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

# Chrome -
# service_object = Service("C:\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_object)

# Microsoft Edge -
from selenium.webdriver.support.select import Select

service_object = Service("C:\\msedgedriver.exe")
driver = webdriver.Edge(service=service_object)

driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Demo@1234")
driver.find_element(By.ID, "confirmPassword").send_keys("Demo@1234")

# driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()