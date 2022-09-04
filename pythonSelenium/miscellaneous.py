from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_Options = webdriver.ChromeOptions()
chrome_Options.add_argument("headless")
chrome_Options.add_argument("--ignore-certificate-errors")

# Chrome -
service_object = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object, options=chrome_Options)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")
