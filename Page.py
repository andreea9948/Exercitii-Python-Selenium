from Driver import Driver

class Page(Driver):

    def scroll_until_xpath(self, xpath):
        scroll = self._driver().find_element_by_xpath(xpath)
        self._get_Action().move_to_element(scroll).perform()
    
    def get_element_by_xpath(self, xpath):
        return self._driver().find_element_by_xpath(xpath)
    
    def get_elements_by_xpath(self, xpath):
        return self._driver().find_elements_by_xpath(xpath)
    
    @staticmethod
    def get_text_from_element(elem):
        return elem.text
    
    @staticmethod
    def click_element(elem):
        elem.click()
    
    @staticmethod
    def print_message(message):
        print(message)

