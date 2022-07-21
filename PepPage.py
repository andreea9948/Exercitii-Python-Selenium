from Page import *
from robot.libraries.BuiltIn import BuiltIn

class PepPage(Page):
    contents_xpath = './/nav[./h2[text()="Contents"]]'

    def __init__(self):
        super().__init__()

    def find_in_contents(self, text):
        return self._driver().find_element_by_xpath(f'{PepPage.contents_xpath}/ul/li[./a[text()="{text}"]]/a')

    def count_bullets(self, xpath):
        bullets = self._driver().find_elements_by_xpath(xpath)
        return len(bullets)
    
    @staticmethod
    def check_nr_bullets(expected_nr, actual_nr):
        if int(expected_nr) == int(actual_nr):
            BuiltIn().pass_execution(f'Numarul de bullets este cel asteptat = {expected_nr}')
        else:
            BuiltIn().fail(f"Numarul de bullets este {actual_nr} si ar trebui sa fie {expected_nr}")
