from selenium import webdriver


class Driver:
    page_link = "https://www.python.org"
    driver = webdriver.Chrome("./chromedriver_win32/chromedriver.exe")
    driver.get(page_link)

    @staticmethod
    def close_driver():
        Driver.driver.close()
