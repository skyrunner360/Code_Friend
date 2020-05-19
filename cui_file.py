#call created functions here
#It Works. So do not touch this file
#kind of a redundant file but still let's just keep it.
#TODO Maybe Obsolute file. Complete GUI TO Delete
import tools_func

class mainclass:
    def gui_g(self,se):
        ex=tools_func.non_gui()
        ex.search_google(se)
    def gui_yt(self,se):
        execute=tools_func.non_gui()
        execute.search_youtube(se)
    def gui_stack(self,se):
        execute=tools_func.non_gui()
        execute.search_stackoverflow(se)
    def gui_git(self,se):
        execute = tools_func.non_gui()
        execute.search_github(se)
