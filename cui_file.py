# call created functions here
# TODO Maybe Obsolute file. Complete GUI TO Delete
import tools_func


class MainClass:
    def gui_g(self, se):
        ex = tools_func.NonGui()
        ex.search_google(se)

    def gui_yt(self, se):
        execute = tools_func.NonGui()
        execute.search_youtube(se)

    def gui_stack(self, se):
        execute = tools_func.NonGui()
        execute.search_stackoverflow(se)

    def gui_git(self, se):
        execute = tools_func.NonGui()
        execute.search_github(se)
