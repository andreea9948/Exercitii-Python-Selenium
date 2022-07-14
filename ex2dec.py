from open_close import *

@open_close
def ex2(driver):
    #Find search bar and input text
    search_bar = driver.find_element_by_xpath('.//input[@id="id-search-field"]')
    search_bar.send_keys('decorator')
    subm_button = driver.find_element_by_xpath('.//button[@type="submit"]')
    subm_button.click()

    #Find first link
    first_res = driver.find_element_by_xpath('.//ul[@class="list-recent-events menu"]/li[1]//a')
    first_res.click()

    #Open examples  - Contents
    contents = driver.find_element_by_xpath('.//nav[./h2[text()="Contents"]]/ul/li[./a[text()="Examples"]]/a')
    contents.click()

    #Get number of examples
    examples = driver.find_elements_by_xpath('.//section[@id="examples"]/ol/li')

    message = ''
    if len(examples) == 5:
        message = 'Corect - Sunt 5 exemple'
    else:
        message = f'Gresit! Numarul de exemple gasit este {len(examples)}'

    return message
