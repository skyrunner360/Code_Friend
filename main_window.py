"""This module contains view and logic of main window"""


from tkinter import BooleanVar
from tkinter import Button
from tkinter import Checkbutton
from tkinter import Entry
from tkinter import Frame
from tkinter import Label
from tkinter import StringVar
from tkinter import Tk
import tkinter.messagebox as msg
from browser import Browser


class MainWindow():
    """Main GUI window class"""

    def __init__(self):
        root = Tk()
        root.geometry("800x150")
        root.title("Code Friend")

        self.search = StringVar()
        self.search.set("")

        frame = Frame(root, borderwidth=5)
        frame.grid(row=0, column=3)

        search_label = Label(frame, text="Enter What you want to search",
                             font="Helvetica 15 bold", fg="blue")
        search_label.grid(row=0, column=4)

        search_textbox = Entry(frame, textvar=self.search,
                               font="lucida 15 italic")
        search_textbox.grid(row=0, column=5)

        self.use_google = BooleanVar()
        google = Checkbutton(text="Google", variable=self.use_google)
        google.grid(row=1, column=3)

        self.use_youtube = BooleanVar()
        yt_checkbutton = Checkbutton(text="Youtube", variable=self.use_youtube)
        yt_checkbutton.grid(row=2, column=3)

        self.use_stackoverflow = BooleanVar()
        so_checkbutton = Checkbutton(text="Stack Overflow",
                                     variable=self.use_stackoverflow)
        so_checkbutton.grid(row=3, column=3)

        self.use_github = BooleanVar()
        gh_checkbutton = Checkbutton(text="Github", variable=self.use_github)
        gh_checkbutton.grid(row=4, column=3)

        search_button = Button(frame, text="Search", font="lucida 15 italic")
        search_button.bind("<Button-1>", self.search_button_clicked)
        search_button.grid(row=0, column=6)

        root.mainloop()

    def search_button_clicked(self, event):
        """Handler of Search Button"""
        google = self.use_google.get()
        youtube = self.use_youtube.get()
        stackoverflow = self.use_stackoverflow.get()
        github = self.use_github.get()

        if any([google, youtube, stackoverflow, github]):
            browser = Browser()
            request = self.search.get()

            if google:
                browser.search_google(request)
            if youtube:
                browser.search_youtube(request)
            if stackoverflow:
                browser.search_stackoverflow(request)
            if github:
                browser.search_github(request)
        else:
            msg.showerror("Error", "Please Select a option first!")
