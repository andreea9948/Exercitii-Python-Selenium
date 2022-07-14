from Driver import Driver
import datetime


class Table:
    def __init__(self, xpath):
        self.xpath = xpath
        self.table = Driver.driver.find_element_by_xpath(self.xpath)

    def get_elem_by_index(self, index):
        return self.table.find_element_by_xpath(f'.//li[{index}]')


class TableReleases(Table):
    def __init__(self):
        super().__init__(xpath='.//div[@class="row download-list-widget"]')

    @staticmethod
    def get_number(elem):
        return elem.find_element_by_xpath('./span[@class="release-number"]/a').text

    @staticmethod
    def get_date(elem):
        rls_date = elem.find_element_by_xpath('.//span[@class="release-date"]').text
        rls_date = datetime.datetime.strptime(rls_date, '%B %d, %Y')
        rls_date = rls_date.strftime('%b %d,%Y')

        return rls_date

    def get_releases_by_version(self, version):
        try:
            releases = self.table.find_elements_by_xpath(
                f'.//span[@class="release-number"]/a[contains(text(),"{version}")]')
            return releases
        except():
            return None


class TableVersions(Table):
    def __init__(self):
        super().__init__(xpath='.//div[@class="row active-release-list-widget"]')

    @staticmethod
    def get_version(elem):
        return elem.find_element_by_xpath('.//span[@class="release-version"]').text

    @staticmethod
    def get_date(elem):
        vers_date = elem.find_element_by_xpath('./span[@class="release-start"]').text
        vers_date = datetime.datetime.strptime(vers_date, '%Y-%m-%d')
        vers_date = vers_date.strftime('%b %d,%Y')
        return vers_date

    def get_version_by_release(self, release):
        release = ".".join(release.split(' ')[1].split('.')[0:2])
        print(release)

        first_rls_date_elem = self.table.find_element_by_xpath(
            f'.//li[./span[@class="release-version" and text()="{release}"]]')
        return first_rls_date_elem
