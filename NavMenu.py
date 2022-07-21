from Driver import *


class NavMenu(Driver):
    
    navMenu_xpath = './/nav[@id="mainnav"]'

    def hover_category(self, text):
        driver = self._driver()
        category = driver.find_element_by_xpath(f'{NavMenu.navMenu_xpath}//li[@id="{text}"]')
        self._get_Action().move_to_element(category).perform()

        return category

    @staticmethod
    def search_subcategory(text, category_elem):
        subcategory = category_elem.find_element_by_xpath(f'.//a[text()="{text}"]')
        return subcategory
