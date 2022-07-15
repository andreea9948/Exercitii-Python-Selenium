from Pages import *
import time


def open_close(func):
    def wrapper():
        page = HomePage()
        msg = func(page)
        print(msg)
        time.sleep(10)
        Driver.close_driver()
    return wrapper


@open_close
def run_ex1(page):
    #ex1
    submenu_downloads = page.navMenu.hover_category("downloads")
    all_rls = page.navMenu.search_subcategory("All releases", submenu_downloads)
    HomePage.click_element(all_rls)
    page = DownloadsPage()
    page.scroll_until_xpath('.//div[@class="row download-list-widget"]')
    latest_release = TableReleases.get_number(page.table_releases.get_elem_by_index(1))

    message = f'Cel mai nou release - {latest_release}'

    return message


@open_close
def run_ex2(page):
    #ex2
    page.searchBar.put_text('decorator')
    HomePage.click_element(HomePage.get_element_by_xpath(HomePage.searchButton_xpath))
    first_res = ResultsPage.get_result_by_index(1)
    ResultsPage.click_element(first_res)
    page = PepPage()
    examples = PepPage.find_in_contents('Examples')
    PepPage.click_element(examples)
    nr_examples = PepPage.count_bullets('.//section[@id="examples"]/ol/li')

    message = ''
    if nr_examples == 5:
        message = f'Corect - Sunt 5 exemple'
    else:
        message = f'Gresit! Numarul de exemple gasit este {nr_examples}'

    return message


@open_close
def run_ex3(page):
    #ex3
    message = ''
    submenu_downloads = page.navMenu.hover_category("downloads")
    all_rls = page.navMenu.search_subcategory("All releases", submenu_downloads)
    HomePage.click_element(all_rls)
    page.scroll_until_xpath('.//div[@class="row download-list-widget"]')
    page = DownloadsPage()
    version = TableVersions.get_version(page.table_versions.get_elem_by_index(1))

    count_rls = page.table_releases.get_releases_by_version(version)
    if count_rls is not None:
        message = f'Exista {len(count_rls)} release-uri pentru ultima versiune\n'
    else:
        message = 'Nu exista release pentru ultima versiune\n'

    latest_release = page.table_releases.get_elem_by_index(1)
    latest_release_date = TableReleases.get_date(latest_release)
    latest_release_number = TableReleases.get_number(latest_release)

    first_release = page.table_versions.get_version_by_release(latest_release_number)
    first_release_date = TableVersions.get_date(first_release)

    if first_release_date < latest_release_date:
        message += f'Gresit - data primului release este {first_release_date} si a ultimului {latest_release_date}'
    else:
        message += f'Corect - data primului release este {first_release_date} si a ultimului {latest_release_date}'

    return message


if __name__ == "__main__":
    run_ex1()
    #run_ex2()
    #run_ex3()