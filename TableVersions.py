from Table import *
import datetime

class TableVersions(Table):
      
    xpath= './/div[@class="row active-release-list-widget"]'
    
    def table_version(self):
        return self._driver().find_element_by_xpath(TableVersions.xpath)

    @staticmethod
    def get_version_number(elem):
        return elem.find_element_by_xpath('.//span[@class="release-version"]').text

    @staticmethod
    def get_version_date(elem):
        vers_date = elem.find_element_by_xpath('./span[@class="release-start"]').text
        #vers_date = datetime.datetime.strptime(vers_date, '%Y-%m-%d')
        #vers_date = vers_date.strftime('%Y-%m-%d')
        return vers_date

    def get_version_by_release(self, release):
        release = ".".join(release.split(' ')[1].split('.')[0:2])

        first_rls_date_elem = self.table_version().find_element_by_xpath(
            f'.//li[./span[@class="release-version" and text()="{release}"]]')
        return first_rls_date_elem