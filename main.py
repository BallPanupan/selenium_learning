from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=r"C:/Users/AsusX/Desktop/my_learning/selenium_learning/chromedriver/chromedriver.exe")


driver.get('https://www.asxlistedcompanies.com/')
driver.implicitly_wait(3)

rows = driver.find_elements_by_xpath('//*[@id="table"]/tbody/tr')
print(len(rows))

print(rows[1])


# rows = driver.find_elements_by_xpath("//table/tbody/tr")
# print(len(rows))


# driver.quit()