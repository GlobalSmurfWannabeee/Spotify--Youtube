from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

songList=[]



def scroll_down():
    """A method for scrolling the page."""

    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:

        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:

            break

        last_height = new_height



def spotifyLogin():
	#driver.find_element_by_xpath('//button[contains(text(),"Log in")]').click()
	driver.find_element_by_name("username").send_keys("trialrun29")
	driver.find_element_by_name("password").send_keys("trial.run")
	driver.find_element_by_id("login-button").click()

def getTrackList(source):
	source=driver.current_url
	soup=BeautifulSoup(source,'html.parser')
	tracks=soup.findAll("div",{"class":"tracklist-name ellipsis-one-line"})
	print("using beutiful soup")
	print(tracks)


driver=webdriver.Firefox(firefox_profile="/home/udit/Desktop/PythonSc",executable_path=r'//home//udit//Downloads//geckodriver')
driver.get("https://open.spotify.com/browse/featured")
driver.implicitly_wait(3)
print(driver.current_url)

x=driver.find_elements_by_class_name("navbar-link__text")

for i in x:
	if i.text=='Your Library':
		i.click()
		break

driver.implicitly_wait(3)
print(driver.current_url)




y=driver.find_elements_by_class_name("EYVkZXmTImKH4iH48N7Uj")

for i in y:
	if i.text=="FAVORITE SONGS":
		i.click()
		break

driver.implicitly_wait(3)
print(driver.current_url)

c=0

scroll_down()

print("usinf selenium")
z=driver.find_elements_by_xpath("//div[@class='tracklist-name ellipsis-one-line']")
for i in z:
	ex=str(i.text)
	if '-' in ex:
		cc=ex.split('-')
		ex=cc[0]
	songList.append(ex)

print(songList)