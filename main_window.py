# make gui part here
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
    def __init__(self):
        root = Tk()
        root.geometry("800x150")
        root.title("Code Friend")

        self.search = StringVar()
        self.search.set("")

        frame = Frame(root, borderwidth=5)
        frame.grid(row=0, column=3)

        lb = Label(frame, text="Enter What you want to search",
                   font="Helvetica 15 bold", fg="blue")
        lb.grid(row=0, column=4)

        tb = Entry(frame, textvar=self.search, font="lucida 15 italic")
        tb.grid(row=0, column=5)

        self.use_google = BooleanVar()
        google = Checkbutton(text="Google", variable=self.use_google)
        google.grid(row=1, column=3)

        self.use_youtube = BooleanVar()
        yt = Checkbutton(text="Youtube", variable=self.use_youtube)
        yt.grid(row=2, column=3)

        self.use_stackoverflow = BooleanVar()
        stack = Checkbutton(text="Stack Overflow",
                            variable=self.use_stackoverflow)
        stack.grid(row=3, column=3)

        self.use_github = BooleanVar()
        git = Checkbutton(text="Github", variable=self.use_github)
        git.grid(row=4, column=3)

        bt = Button(frame, text="Search", font="lucida 15 italic")
        bt.bind("<Button-1>", self.search_button_clicked)
        bt.grid(row=0, column=6)

        root.mainloop()

    def search_button_clicked(self, event):
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
