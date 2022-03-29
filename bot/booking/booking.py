import booking.constants as const
import os 
from selenium import webdriver
# from selenium.webdriver.common.by import By

# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(executable_path=r"C:/Users/AsusX/Desktop/my_learning/selenium_learning/chromedriver/chromedriver.exe")


class Booking(webdriver.Chrome):
    def __init__(self, driver_path = r"C:/Users/AsusX/Desktop/my_learning/selenium_learning/chromedriver/chromedriver.exe"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()

    def  land_first_page(self):
        self.get(const.BASE_URL)
    