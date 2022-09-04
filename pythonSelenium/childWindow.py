from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

service_object = Service("C:\\msedgedriver.exe")
# service_object = Service("C:\\geckodriver.exe")
driver = webdriver.Edge(service=service_object)
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(windowsOpened[0])
parentWindowText = driver.find_element(By.TAG_NAME, "h3").text
print(parentWindowText)
assert "Opening a new window" == parentWindowText
