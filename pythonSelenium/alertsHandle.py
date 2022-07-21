from selenium import webdriver

validateText = 'Gulnawaz Arshad'
validateTextOne = 'Aaira Arshad'

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys(validateText)
driver.find_element_by_id("alertbtn").click()
# driver.find_element_by_xpath("//input[@id='alertbtn']").click()
alert = driver.switch_to.alert
print(alert.text)
alertText = alert.text
assert validateText in alertText
alert.accept()


driver.find_element_by_css_selector("#name").send_keys(validateText)
driver.find_element_by_id("confirmbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alertText = alert.text
assert validateTextOne in alertText
alert.dismiss()