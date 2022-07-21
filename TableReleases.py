import datetime
from Table import *

class TableReleases(Table):
    xpath= './/div[@class="row download-list-widget"]'
    
    def table_release(self):
        return self._driver().find_element_by_xpath(TableReleases.xpath)

    @staticmethod
    def get_release_number(elem):
        return elem.find_element_by_xpath('./span[@class="release-number"]/a').text

    @staticmethod
    def get_release_date(elem):
        rls_date = elem.find_element_by_xpath('.//span[@class="release-date"]').text
        rls_date = datetime.datetime.strptime(rls_date, '%B %d, %Y')
        rls_date = rls_date.strftime('%Y-%m-%d')

        return rls_date

    def get_releases_by_version(self, version):
        try:
            releases = self.table_release().find_elements_by_xpath(
                f'.//span[@class="release-number"]/a[contains(text(),"{version}")]')
            return releases
        except():
            return None