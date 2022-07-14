from Pages import *


def run_ex1():
    #ex1
    page = HomePage()
    submenu_downloads = page.navMenu.hover_category("downloads")
    all_rls = page.navMenu.search_subcategory("All releases", submenu_downloads)
    HomePage.click_element(all_rls)
    page = DownloadsPage()
    page.scroll_until_xpath('.//div[@class="row download-list-widget"]')
    latest_release = TableReleases.get_number(page.table_releases.get_elem_by_index(1))

    print(f'Cel mai nou release - {latest_release}')


def run_ex2():
    #ex2
    page = HomePage()
    page.searchBar.put_text('decorator')
    HomePage.click_element(HomePage.get_element_by_xpath(HomePage.searchButton_xpath))
    first_res = ResultsPage.get_result_by_index(1)
    ResultsPage.click_element(first_res)
    page = PepPage()
    examples = PepPage.find_in_contents('Examples')
    PepPage.click_element(examples)
    nr_examples = PepPage.count_bullets('.//section[@id="examples"]/ol/li')
    PepPage.check_nr_bullets(5, nr_examples)


def run_ex3():
    #ex3
    page = HomePage()
    submenu_downloads = page.navMenu.hover_category("downloads")
    all_rls = page.navMenu.search_subcategory("All releases", submenu_downloads)
    HomePage.click_element(all_rls)
    page.scroll_until_xpath('.//div[@class="row download-list-widget"]')
    page = DownloadsPage()
    version = TableVersions.get_version(page.table_versions.get_elem_by_index(1))

    count_rls = page.table_releases.get_releases_by_version(version)
    if count_rls is not None:
        print(f'Exista {len(count_rls)} release-uri pentru ultima versiune')
    else:
        print('Nu exista release pentru ultima versiune')

    latest_release = page.table_releases.get_elem_by_index(1)
    latest_release_date = TableReleases.get_date(latest_release)
    latest_release_number = TableReleases.get_number(latest_release)

    first_release = page.table_versions.get_version_by_release(latest_release_number)
    first_release_date = TableVersions.get_date(first_release)

    if first_release_date < latest_release_date:
        print(f'Gresit - data primului release este {first_release_date} si a ultimului {latest_release_date}')
    else:
        print(f'Corect - data primului release este {first_release_date} si a ultimului {latest_release_date}')


if __name__ == "__main__":
    #First version
    #ex1()
    #ex2()
    #ex3()

    #Second version:
    run_ex1()
    #run_ex2()
    #run_ex3()