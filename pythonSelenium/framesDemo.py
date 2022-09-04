from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.service import Service

from selenium.webdriver.common.by import By

# Firefox -
service_object = Service("C:\\geckodriver.exe")
driver = webdriver.Firefox(service=service_object)
driver.implicitly_wait(2)

driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I'm able to automate frames")
driver.switch_to.default_content()
iframeHeading = driver.find_element(By.TAG_NAME, "h3").text
print(iframeHeading)