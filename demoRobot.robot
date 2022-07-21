*** Settings ***
Library    SeleniumLibrary
Library    HomePage
Library    Driver
Library    DownloadsPage
Library    PepPage
Library    ResultsPage
Library    DateTime

Test Setup    Driver.Start Driver
Test TearDown    Driver.Close Driver

*** Variables ***
&{args_5}    text=decorator    res_index=1    categ=Examples    count_xpath=.//section[@id="examples"]/ol/li    nr_bullets=4

*** Keywords ***
Click Downloads AllRls
    ${category}=    HomePage.Hover Category    downloads
    ${subcategory}=    HomePage.Search Subcategory    All releases    ${category}
    HomePage.Click Element    ${subcategory}
    DownloadsPage.Scroll Until Xpath    .//div[@class="row download-list-widget"]

Click Search Button   
    ${search_button_xpath}=    HomePage.Get SearchButton Xpath
    ${search_button}=    HomePage.Get Element By Xpath    ${search_button_xpath}
    HomePage.Click Element    ${search_button}
    
*** Test Cases ***
Ex1
    Click Downloads AllRls
    ${release_table}=    DownloadsPage.Table Release
    ${first_entry}=    DownloadsPage.Get Elem By Index    1    ${release_table}
    ${first_release_nr}=    DownloadsPage.Get Release Number    ${first_entry}
    Log    ${first_release_nr}
    [Documentation]    Go to Downloads->All Releases and get the latest release
    
Ex2
    HomePage.Put Text    decorator
    Click Search Button 
    ${first_result}=    ResultsPage.Get Result By Index    1
    ResultsPage.Click Element    ${first_result}
    ${examples}=    PepPage.Find In Contents    Examples
    PepPage.Click Element    ${examples}
    ${nr_examples}=    PepPage.Count Bullets    .//section[@id="examples"]/ol/li
    PepPage.Check Nr Bullets    5    ${nr_examples}
    [Documentation]    Search decorator and open the first link. Go to examples and make sure there are 5 bullets.
    
Ex3
    Click Downloads AllRls
    ${table_version}=    DownloadsPage.Table Version
    ${latest_version_elem}=    DownloadsPage.Get Elem By Index    1    ${table_version}
    ${latest_version_nr}=    DownloadsPage.Get Version Number    ${latest_version_elem}
    ${nr_releases}=    DownloadsPage.Get Releases By Version    ${latest_version_nr}
    DownloadsPage.Check Existing Releases    ${nr_releases}
    
    
    ${release_table}=    DownloadsPage.Table Release
    ${latest_rls}=    DownloadsPage.Get Elem By Index    1    ${release_table}
    ${latest_rls_nr}=    DownloadsPage.Get Release Number    ${latest_rls}
    ${latest_rls_date}=    DownloadsPage.Get Release Date    ${latest_rls}   
    
    ${first_release}=    DownloadsPage.Get Version By Release    ${latest_rls_nr}
    ${first_release_date}=    DownloadsPage.Get Version Date    ${first_release}
    DownloadsPage.Compare Dates    ${first_release_date}    ${latest_rls_date}    
    [Documentation]    Go to Downloads->Allreleases. Check if there is any release for the latest version. Check if the latest release was published before it's version.
    

Ex4
    HomePage.Put Text    decorator
    Click Search Button 
    ${first_result}=    ResultsPage.Get Result By Index    1
    ResultsPage.Click Element    ${first_result}
    ${examples}=    PepPage.Find In Contents    Examples
    PepPage.Click Element    ${examples}
    @{bullets}=    PepPage.Get Elements By Xpath    .//section[@id="examples"]/ol/li
    
    FOR    ${bullet}    IN    @{bullets}
    \    ${text_elem}=    PepPage.Get Text From Element    ${bullet}
    \    Log    ${text_elem}
    
    [Documentation]    Search decorator and open the first link. Go to examples and make sure there are 5 bullets. With list and FOR
    
    
Ex5    
    HomePage.Put Text   ${args_5.text}
    Click Search Button
    Set Log Level    DEBUG
    Log    Log de debug    level=DEBUG
    Log    Log de info    level=INFO
    ${first_result}=    ResultsPage.Get Result By Index    ${args_5.res_index}
    ResultsPage.Click Element    ${first_result}
    ${examples}=    PepPage.Find In Contents    ${args_5.categ}
    PepPage.Click Element    ${examples}
    ${nr_examples}=    PepPage.Count Bullets    ${args_5.count_xpath}
    PepPage.Check Nr Bullets    ${args_5.nr_bullets}    ${nr_examples}
    
    [Documentation]    Search decorator and open the first link. Go to examples and make sure there are 4 bullets - Using dictionary
    
    
    