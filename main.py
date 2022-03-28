from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('file:///C:/Users/AsusX/Desktop/my_learning/selenium_learning/ex_web/form/index.html')
driver.implicitly_wait(3)

input_a = driver.find_element(By.ID, 'input-a')
input_b = driver.find_element(By.ID, 'input-b')
btn = driver.find_element(By.XPATH, '/html/body/div/form/div[1]/button')

# input_a = driver.find_element(By.ID, "input-a").get_attribute("value")
sleep(2)
input_a.clear()
input_a.send_keys(122)
sleep(2)
input_b.clear()
input_b.send_keys(32)
sleep(2)
btn.click()

sleep(2)
input_a.clear()
input_a.send_keys(10)
sleep(2)
input_b.clear()
input_b.send_keys(7)
sleep(2)
btn.click()



# driver.quit()