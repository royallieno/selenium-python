from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_object = Service("C:\\chromedriver.exe")        # Invoke the service object
driver = webdriver.Chrome(service=service_object, options=chrome_options)       # Create driver object out of it

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
