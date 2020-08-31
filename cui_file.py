# call created functions here
# TODO Maybe Obsolute file. Complete GUI TO Delete
# import tkinter as tk
import tools_func


class mainclass:
    def gui_g(self, se):
        ex = tools_func.non_gui()
        ex.search_google(se)

    def gui_yt(self, se):
        execute = tools_func.non_gui()
        execute.search_youtube(se)

    def gui_stack(self, se):
        execute = tools_func.non_gui()
        execute.search_stackoverflow(se)

    def gui_git(self, se):
        execute = tools_func.non_gui()
        execute.search_github(se)
