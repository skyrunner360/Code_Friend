# create functions here

from secrets import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from urllib.parse import quote


class NonGui():
    def __init__(self):
        # Open Web Browser
        self.driver = webdriver.Firefox()

    def get_search_query(self, search):
        return quote(search)

    def search_google(self, search):
        # Open Google and search for the search string
        url = GOOGLE_URL + self.get_search_query(search)
        self.driver.get(url)

    def search_youtube(self, search):
        url = YOUTUBE_URL + self.get_search_query(search)
        self.driver.execute_script(f'window.open("{url}", "new_window")')

    def search_stackoverflow(self, search):
        url = STACKOVERFLOW_URL + self.get_search_query(search)
        self.driver.execute_script(f'window.open("{url}", "new_window")')

    def search_github(self, search):
        url = GITHUB_URL + self.get_search_query(search)
        self.driver.execute_script(f'window.open("{url}", "new_window")')
