from selenium.webdriver import ActionChains
from Elements import *
from Tables import *


class Page:
    def __init__(self):
        self.a = ActionChains(Driver.driver)

    def scroll_until_xpath(self, xpath):
        scroll = Driver.driver.find_element_by_xpath(xpath)
        self.a.move_to_element(scroll).perform()

    @staticmethod
    def get_element_by_xpath(xpath):
        return Driver.driver.find_element_by_xpath(xpath)

    @staticmethod
    def click_element(elem):
        elem.click()


class HomePage(Page):
    navMenu_xpath = './/nav[@id="mainnav"]'
    searchBar_xpath = './/form[@class="search-the-site"]//input[@id="id-search-field"]'
    searchButton_xpath = './/button[@class="search-button"]'

    def __init__(self):
        super().__init__()
        self.navMenu = NavMenu(HomePage.navMenu_xpath, Driver.driver, self.a)
        self.searchBar = SearchBar(HomePage.searchBar_xpath, Driver.driver)


class DownloadsPage(HomePage):
    def __init__(self):
        super().__init__()
        self.table_releases = TableReleases()
        self.table_versions = TableVersions()


class ResultsPage(HomePage):
    res_section_xpath = './/ul[@class="list-recent-events menu"]'

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_result_by_index(index):
        return Driver.driver.find_element_by_xpath(f'{ResultsPage.res_section_xpath}/li[{index}]//a')


class PepPage(Page):
    contents_xpath = './/nav[./h2[text()="Contents"]]'

    def __init__(self):
        super().__init__()

    @staticmethod
    def find_in_contents(text):
        return Driver.driver.find_element_by_xpath(f'{PepPage.contents_xpath}/ul/li[./a[text()="{text}"]]/a')

    @staticmethod
    def count_bullets(xpath):
        bullets = Driver.driver.find_elements_by_xpath(xpath)
        return len(bullets)

    @staticmethod
    def check_nr_bullets(expected_nr, actual_nr):
        message = ''
        if expected_nr == actual_nr:
            message = f'Corect - Sunt {expected_nr} exemple'
        else:
            message = f'Gresit! Numarul de exemple gasit este {actual_nr}'

        print(message)
