from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
import time
# browser exposes an executable file
# Through selenium test we need to invoke the executable file which will then invoke actual browser
# s = Service("C:\\chromedriver.exe")
# driver = webdriver.Chrome(service=s)

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
# driver = webdriver.Edge(executable_path="C:\\msedgedriver.exe")
# driver = webdriver.Ie(executable_path="C:\\IEDriverServer")
driver.maximize_window()

driver.get("https://now.gg/")  # Get method to hit URL on browser

print(driver.title)
print(driver.current_url)
driver.get("https://now.gg/games.html/")
driver.minimize_window()
time.sleep(10)
driver.back()
driver.refresh()

time.sleep(5)
driver.close()