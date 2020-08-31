# create functions here

from secrets import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class NonGui():
    def __init__(self):
        # Open Web Browser
        self.driver = webdriver.Firefox()

    def search_google(self, search):
        # Open Google and search for the search string
        self.driver.get(GOOGLE_URL)
        self.driver.find_element_by_xpath(
            '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(search, Keys.ENTER)
        sleep(2)

    def search_youtube(self, search):
        self.driver.execute_script(
            'window.open("'+YOUTUBE_URL+'", "new window")')
        sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        seaarching = self.driver.find_element_by_xpath(
            '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
        seaarching.click()
        seaarching.send_keys(search, Keys.ENTER)
        sleep(2)

    def search_stackoverflow(self, search):
        self.driver.execute_script(
            'window.open("'+STACKOVERFLOW_URL+'", "new window2")')
        sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        searching = self.driver.find_element_by_xpath(
            '/html/body/header/div/form/div/input')
        searching.click()
        searching.send_keys(search, Keys.ENTER)
        sleep(2)

    def search_github(self, search):
        self.driver.execute_script(
            'window.open("'+GITHUB_URL+'", "new window3")')
        sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        searching = self.driver.find_element_by_xpath(
            '/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label/input[1]')
        searching.click()
        searching.send_keys(search, Keys.ENTER)
        sleep(2)
