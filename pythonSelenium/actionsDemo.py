from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

# Chrome -
# service_object = Service("C:\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_object)

# Microsoft Edge -
service_object = Service("C:\\msedgedriver.exe")
driver = webdriver.Edge(service=service_object)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "input[value='option1']").click()
action = ActionChains(driver)
# action.double_click(driver.find_element(By.))                                   #Double Click
# action.context_click(driver.find_element(By.))                                  #Right Click
# action.drag_and_drop(driver.find_element(By.))                                  #Drag and Drop
action.move_to_element(driver.find_element(By.CSS_SELECTOR, "#mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
action.context_click(driver.find_element(By.CSS_SELECTOR, "input[value='option1']")).perform()
