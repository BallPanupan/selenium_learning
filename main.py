from selenium import webdriver

driver = webdriver.Chrome()

driver.get("file:///C:/Users/AsusX/Desktop/my_learning/selenium_learning/ex_web/index.html")

driver.implicitly_wait(5) #time.sleep(5)
my_element = driver.find_element_by_id('downloadButtonx')
my_element.click()
 

