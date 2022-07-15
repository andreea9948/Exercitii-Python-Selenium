from selenium.webdriver.common.action_chains import ActionChains
from open_close import *

@open_close
def ex1(driver):
    a = ActionChains(driver)

    #Get menu and click on Downloads -> All releases
    menu = driver.find_element_by_xpath('.//nav[@id="mainnav"]//li[@id="downloads"]')
    a.move_to_element(menu).perform()
    rls = menu.find_element_by_xpath('.//a[contains(text(), "All releases")]')
    rls.click()


    #Scroll to table
    scroll = driver.find_element_by_xpath('.//div[@class="row download-list-widget"]')
    a.move_to_element(scroll).perform()


    #Get element from table
    latest_release = driver.find_element_by_xpath('.//ol[@class="list-row-container menu"]/li[1]/span[@class="release-number"]//a')
    return latest_release.text

