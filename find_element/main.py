from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("file:///C:/Users/AsusX/Desktop/my_learning/selenium_learning/ex_web/index.html")

driver.implicitly_wait(3) #time.sleep(5)
my_element = driver.find_element(By.ID, "downloadButtonx")
my_element.click()

# progress_element = driver.find_element(By.CLASS_NAME, "completeds-label")
# print(f"{progress_element.text == 'Completed!'}")

WebDriverWait(driver, 3).until(
    EC.element_to_be_selected(
        (By.CLASS_NAME, 'completeds-label'), 'Completed!'
    )
)


driver.quit()


