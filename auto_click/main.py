from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=r"C:/Users/AsusX/Desktop/my_learning/selenium_learning/chromedriver/chromedriver.exe")


driver.get('file:///C:/Users/AsusX/Desktop/my_learning/selenium_learning/ex_web/form/index.html')
driver.implicitly_wait(3)

input_a = driver.find_element(By.ID, 'input-a')
input_b = driver.find_element(By.ID, 'input-b')
# btn = driver.find_element(By.XPATH, '/html/body/div/form/div[1]/button')
btn = driver.find_element_by_css_selector('button[onClick="main()"]')
# input_a = driver.find_element(By.ID, "input-a").get_attribute("value")
sleep(1)
input_a.clear()
input_a.send_keys(122)
input_b.clear()
input_b.send_keys(32)
sleep(1)
btn.click()

sleep(1)
input_a.clear()
input_a.send_keys(10)

input_b.clear()
input_b.send_keys(7)
sleep(1)
btn.click()

# driver.quit()