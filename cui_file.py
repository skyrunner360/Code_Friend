# call created functions here
# TODO Maybe Obsolute file. Complete GUI TO Delete
import tools_func


class MainClass:
    def __init__(self):
        self.browser = tools_func.Browser()

    def gui_g(self, se):
        self.browser.search_google(se)

    def gui_yt(self, se):
        self.browser.search_youtube(se)

    def gui_stack(self, se):
        self.browser.search_stackoverflow(se)

    def gui_git(self, se):
        self.browser.search_github(se)
