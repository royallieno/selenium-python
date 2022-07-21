from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute('value') == 'option2':
        checkbox.click()
        assert checkbox.is_selected()

radioButtons = driver.find_elements_by_class_name("radioButton")
radioButtons[0].click()
assert radioButtons[2].is_selected()
