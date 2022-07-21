from Driver import Driver

class SearchBar(Driver):
    
    searchBar_xpath = './/form[@class="search-the-site"]//input[@id="id-search-field"]'

    def put_text(self, text):
        search_bar = self._driver().find_element_by_xpath(SearchBar.searchBar_xpath)
        search_bar.send_keys(text)
