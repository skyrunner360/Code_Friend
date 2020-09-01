"""This module contains Browser class"""

from secrets import GOOGLE_URL, YOUTUBE_URL, STACKOVERFLOW_URL, GITHUB_URL
from urllib.parse import quote
from selenium import webdriver


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

    def search_youtube(self, search):
        """Goes to YouTube results page"""
        url = YOUTUBE_URL + self.get_search_query(search)
        self.open_page(url)

    def search_stackoverflow(self, search):
        """Goes to StackOverflow results page"""
        url = STACKOVERFLOW_URL + self.get_search_query(search)
        self.open_page(url)

    def search_github(self, search):
        """Goes to GitHub results page"""
        url = GITHUB_URL + self.get_search_query(search)
        self.open_page(url)
