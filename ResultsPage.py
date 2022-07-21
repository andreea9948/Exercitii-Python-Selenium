from HomePage import *


class ResultsPage(HomePage):
    res_section_xpath = './/ul[@class="list-recent-events menu"]'

    def __init__(self):
        super().__init__()

    def get_result_by_index(self, index):
        return self._driver().find_element_by_xpath(f'{ResultsPage.res_section_xpath}/li[{index}]//a')