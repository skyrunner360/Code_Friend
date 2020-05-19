#create functions here
#importing things
from secrets import *
from selenium import webdriver #Before running project install seleniuum by running 'pip install selenium'
from selenium.webdriver.common.keys import Keys
from time import sleep

class non_gui():
    def __init__(self):
        #Open Web Browser
        self.driver = webdriver.Firefox() #Choose the browser to run on. I chose firefox here. For it to work you need to install geckodriver from the web and add it to your environment variables path Otherwis it gives an error.
    def search_google(self,search):
        #Open Google and search for the search string
        self.driver.get(google) #open the link of google
        self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(search,Keys.ENTER) #Locate the search bar, then send the search string and press enter
        sleep(2) #Make the program sleep to let the page load completely. increase this sleep time if due to slow internet you get error like element not found.
    def search_youtube(self,search):
        self.driver.execute_script('window.open("'+youtube+'", "new window")') #Execute javascript to open youtube in new tab.
        sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1]) #Switch to the new tab.
        seaarching = self.driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input') #Locate search bar
        seaarching.click()#Click on the search bar
        seaarching.send_keys(search,Keys.ENTER) #send search string and press enter.
        sleep(2)
    def search_stackoverflow(self,search):
        self.driver.execute_script('window.open("'+stackoverflow+'", "new window2")')
        sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        searching = self.driver.find_element_by_xpath('/html/body/header/div/form/div/input')
        searching.click()
        searching.send_keys(search,Keys.ENTER)
        sleep(2)
    def search_github(self,search):
        self.driver.execute_script('window.open("'+github+'", "new window3")')
        sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        searching = self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label/input[1]')
        searching.click()
        searching.send_keys(search,Keys.ENTER)
        sleep(2)