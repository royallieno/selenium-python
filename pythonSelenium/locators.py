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

driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CSSSeleqtor, Classname, Name, LinkText
driver.find_element(By.NAME, "name").send_keys("Gulnawaz Arshad")                               #Name
driver.find_element(By.NAME, "email").send_keys("khanarshad@gmail.com")                         #Email
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")                         #Password
driver.find_element(By.ID, "exampleCheck1").click()                                             #Checkbox

# Static Dropdown - select class provide the methods to handle the option in dropdown.
genderDropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))                #Gender Dropdown
genderDropdown.select_by_visible_text("Female")
genderDropdown.select_by_index(0)
# genderDropdown.select_by_value("value_here")

driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

# Xpath - //tagname[@attribute='value'] -> //input[@class='btn btn-success']
# CSS - tagname[attribute='value'] -> input[class='btn btn-success'], #id, .className
driver.find_element(By.XPATH, "//input[@class='btn btn-success']").click()                      #Submit Button
successMessage = driver.find_element(By.CLASS_NAME, "alert-success").text
print(successMessage)
assert "Success!" in successMessage

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello Gulnawaz Arshad")  #Two-Way Data Binding text field
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

# //*[contains(@class,'alert-success')] - Xpath - RegularExpression
# [class*='alert-success'] - CSS - RegularExpression
