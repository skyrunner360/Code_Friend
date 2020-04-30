google='https://www.google.com/'
youtube='https://www.youtube.com/'
stackoverflow='https://stackoverflow.com/'
github='https://github.com/'

github_uid =''#Github User ID
github_pass = '' #Github Password

#Extra and unused code

#  def mainbot(self):
#         self.open_google()
#         self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(search,Keys.ENTER)
#         sleep(5)
#         self.driver.execute_script('window.open("'+stackoverflow+'", "new window")')
#         sleep(5)
#         # window = self.driver.window_handles[0]
#         # self.driver.switch_to.window(window[1])
#         self.driver.switch_to.frame(1)
#         searchstac = self.driver.find_element_by_tag_name('input').click()
#         searchstac.send_keys(search, Keys.ENTER)
# if __name__ == '__main__':
#     bot = non_gui()
#     bot.mainbot()