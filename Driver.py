from selenium import webdriver
from robot.libraries.BuiltIn import BuiltIn
from SeleniumLibrary import SeleniumLibrary
import time
from selenium.webdriver import ActionChains

class Driver:
    page_link = "https://www.python.org"
    driver = None
    
    #driver = webdriver.Chrome("./chromedriver_win32/chromedriver.exe")
    
    # def get_driver(self):
    #     driver = webdriver.Chrome("C:/Users/AnCojocaru/Desktop/Exercitii/Python+Selenium/venv/Scripts/chromedriver.exe")
    #     driver.get(page_link)        
    
    def _driver(self):
        if Driver.driver is None:
            Driver.driver = webdriver.Chrome("C:/Users/AnCojocaru/Desktop/Exercitii/Python+Selenium/venv/Scripts/chromedriver.exe")
            Driver.driver.get(Driver.page_link)              
        return Driver.driver
    
    def start_driver(self):
        Driver.driver = self._driver()
        
    def _get_Action(self):
        a = ActionChains(self._driver())
        return a

    @staticmethod
    def close_driver():
        Driver.driver.close()
        Driver.driver = None
