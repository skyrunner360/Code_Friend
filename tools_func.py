# create functions here

from secrets import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from urllib.parse import quote


class Browser():
    """Operates selenium driver"""

    def __init__(self):
        self.driver = webdriver.Firefox()

    def open_page(self, url):
        """Opens a new page in browser"""
        # If no tabs are opened
        if self.driver.current_url == 'about:blank':
            self.driver.get(url)
        else:
            self.driver.execute_script("window.open('');")
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.get(url)

    def get_search_query(self, search):
        """Return search query which can be appended to URL"""
        """This can prevent us from searching manually"""
        return quote(search)

    def search_google(self, search):
        """Goes to Google results page"""
        url = GOOGLE_URL + self.get_search_query(search)
        self.open_page(url)
        # self.driver.get(url)

    def search_youtube(self, search):
        """Goes to YouTube results page"""
        url = YOUTUBE_URL + self.get_search_query(search)
        self.open_page(url)
        # self.driver.execute_script(f'window.open("{url}", "_blank")')

    def search_stackoverflow(self, search):
        """Goes to StackOverflow results page"""
        url = STACKOVERFLOW_URL + self.get_search_query(search)
        self.open_page(url)
        # self.driver.execute_script(f'window.open("{url}", "_blank")')

    def search_github(self, search):
        """Goes to GitHub results page"""
        url = GITHUB_URL + self.get_search_query(search)
        self.open_page(url)
        # self.driver.execute_script(f'window.open("{url}", "_blank")')
