from selenium import webdriver


driver=webdriver.Firefox(firefox_profile="/home/destroyer/.mozilla/firefox/v8gm5evo.default",executable_path=r'//home//destroyer//Downloads//geckodriver')
driver.get("https://www.youtube.com/")
driver.find_element_by_xpath("//input[@id='search']").send_keys("No more sorrows") #Search for video
driver.find_element_by_xpath("//button[@id='search-icon-legacy']").click() #click the search button
driver.find_element_by_xpath('//a[@id="video-title"]').click()# click the link
driver.implicitly_wait(600)
driver.find_element_by_xpath('//*[@aria-label="Save"]').click()#add to playlist
driver.find_element_by_xpath("//*[@title='Songs']//parent::div[@id='checkbox-label']//parent::div[@id='checkbox-container']//parent::div[@id='checkboxLabel']//preceding-sibling::div[@id='checkboxContainer']").click()#adding to playlist
print(driver.current_url)
driver.find_element_by_xpath('//div[@id="columns"]').click()

#driver.find_element_by_class_name('style-scope yt-icon-button').click()

#used x path->>
#//*[@title="Songs"]//parent::div[@id='checkbox-label']//parent::div[@id='checkbox-container']//parent::div[@id='checkboxLabel']//preceding-sibling::div[@id='checkboxContainer']//div[@id='checkbox']
## put yor playlist name in place of Songs
