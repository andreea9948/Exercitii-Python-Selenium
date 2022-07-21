from Page import *
from NavMenu import *
from SearchBar import *


class HomePage(Page, NavMenu, SearchBar):
    
    searchButton_xpath = './/button[@class="search-button"]'
    
    @staticmethod
    def get_searchButton_xpath():
        return HomePage.searchButton_xpath
    
    
