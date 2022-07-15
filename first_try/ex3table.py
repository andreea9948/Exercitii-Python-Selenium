from selenium.webdriver import ActionChains
from open_close import *
import datetime

@open_close
def ex3(driver):
    a = ActionChains(driver)
    message = ''

    #Get menu and click on Downloads -> All releases
    menu = driver.find_element_by_xpath('.//nav[@id="mainnav"]//li[@id="downloads"]')
    a.move_to_element(menu).perform()
    rls = menu.find_element_by_xpath('.//a[contains(text(), "All releases")]')
    rls.click()

    #Scroll to table
    scroll = driver.find_element_by_xpath('.//div[@class="row download-list-widget"]')
    a.move_to_element(scroll).perform()

    #Get latest python version
    element_version = driver.find_element_by_xpath('.//div[@class="row active-release-list-widget"]/ol/li[1]/span')
    version = element_version.text

    #Get release versions
    try:
        nr_releases = driver.find_elements_by_xpath(f'.//div[@class="row download-list-widget"]/ol/li/span[@class="release-number"]/a[contains(text(),"{version}")]')
        message = f'Exista {len(nr_releases)} release-uri pentru ultima versiune'
    except():
        message = 'Nu exista release pentru ultima versiune'


    #Latest release
    latest_rls = driver.find_element_by_xpath('.//div[@class="row download-list-widget"]/ol/li[1]')
    latest_rls_date_elem = latest_rls.find_element_by_xpath('./span[@class="release-date"]')
    latest_rls_date = latest_rls_date_elem.text
    print(latest_rls_date)

    latest_rls_number_elem = latest_rls.find_element_by_xpath('./span[@class="release-number"]')
    latest_rls_number = latest_rls_number_elem.text
    latest_rls_number = ".".join(latest_rls_number.split(' ')[1].split('.')[0:2])
    print(latest_rls_number)

    #Get first released date
    first_rls_date_elem = driver.find_element_by_xpath('.//div[@class="row active-release-list-widget"]/ol/li[./span[@class="release-version" and text()="'+latest_rls_number+'"]]/span[@class="release-start"]')
    first_rls_date = first_rls_date_elem.text

    first_rls_date = datetime.datetime.strptime(first_rls_date, '%Y-%m-%d')
    first_rls_date = first_rls_date.strftime('%b %d,%Y')

    latest_rls_date = datetime.datetime.strptime(latest_rls_date, '%B %d, %Y')
    latest_rls_date = latest_rls_date.strftime('%b %d,%Y')
    if first_rls_date > latest_rls_date:
        message += "\nData primului release este inainte de data ultimului release"
    else:
        message += "\nData primului release este dupa data ultimului release"

    return message

