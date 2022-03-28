from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
# chrome_options.addArguments("--auto-open-devtools-for-tabs")


driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://www.asxlistedcompanies.com/")

driver.title

driver.implicitly_wait(0.5)

# elements = driver.find_element(By.CLASS_NAME, "tableizer-table sortable")
elements = driver.find_elements(By.CLASS_NAME, 'tableizer-table sortable')

for e in elements:
    print(e.text)

# driver.quit()