class NavMenu:
    def __init__(self, xpath, driver, a):
        self.xpath = xpath
        self.driver = driver
        self.a = a

    def hover_category(self, text):
        category = self.driver.find_element_by_xpath(f'{self.xpath}//li[@id="{text}"]')
        self.a.move_to_element(category).perform()

        return category

    def search_subcategory(self, text, category_elem):
        subcategory = category_elem.find_element_by_xpath(f'.//a[text()="{text}"]')
        return subcategory


class SearchBar:
    def __init__(self, xpath, driver):
        self.xpath = xpath
        self.driver = driver

    def put_text(self, text):
        search_bar = self.driver.find_element_by_xpath(self.xpath)
        search_bar.send_keys(text)
