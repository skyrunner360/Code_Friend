# make gui part here
import cui_file
from tkinter import *
import tkinter.messagebox as msg


# Protected variable search
def click(event):
    if use_google.get() == 1:
        obj = cui_file.MainClass()
        obj.gui_g(search.get())
    if use_youtube.get() == 1:
        obj = cui_file.MainClass()
        obj.gui_yt(search.get())
    if use_stackoverflow.get() == 1:
        obj = cui_file.MainClass()
        obj.gui_stack(search.get())
    if use_github.get() == 1:
        obj = cui_file.MainClass()
        obj.gui_git(search.get())
    else:
        msg.showerror("Error", "Please Select a option first!")


if __name__ == '__main__':
    root = Tk()
    root.geometry("800x150")
    root.title("Code Friend")

    search = StringVar()
    search.set("")

    frame = Frame(root, borderwidth=5)
    frame.grid(row=0, column=3)

    lb = Label(frame, text="Enter What you want to search",
               font="Helvetica 15 bold", fg="blue")
    lb.grid(row=0, column=4)

    tb = Entry(frame, textvar=search, font="lucida 15 italic")
    tb.grid(row=0, column=5)

    use_google = BooleanVar()
    google = Checkbutton(text="Google", variable=use_google)
    google.grid(row=1, column=3)

    use_youtube = BooleanVar()
    yt = Checkbutton(text="Youtube", variable=use_youtube)
    yt.grid(row=2, column=3)

    use_stackoverflow = BooleanVar()
    stack = Checkbutton(text="Stack Overflow", variable=use_stackoverflow)
    stack.grid(row=3, column=3)

    use_github = BooleanVar()
    git = Checkbutton(text="Github", variable=use_github)
    git.grid(row=4, column=3)

    bt = Button(frame, text="Search", font="lucida 15 italic")
    bt.bind("<Button-1>", click)
    bt.grid(row=0, column=6)

    root.mainloop()
