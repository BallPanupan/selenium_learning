from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://127.0.0.1/)")

driver.implicitly_wait(5)
my_element = driver.find_element_by_id('downloadButtonx')
my_element.click()
 

