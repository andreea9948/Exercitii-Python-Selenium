from selenium import webdriver
import time


def open_close(func):
    def wrapper():
        # Create driver and open python.org
        driver = webdriver.Chrome("../chromedriver_win32/chromedriver.exe")
        driver.get("https://www.python.org")
        message = func(driver)
        print(message)
        time.sleep(10)
        driver.close()

    return wrapper
