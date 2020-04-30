#make gui part here
import cui_file
from tkinter import *
import tkinter.messagebox as msg


#Protected variable search
def click(event):
    # obj=cui_file.mainclass()
    # obj.gui_g(search.get())
    if choice.get()==1:
        obj=cui_file.mainclass()
        obj.gui_g(search.get())
    if choice1.get()==1:
        obj = cui_file.mainclass()
        obj.gui_yt(search.get())
    if choice2.get()==1:
        obj=cui_file.mainclass()
        obj.gui_stack(search.get())
    if choice3.get()==1:
        obj=cui_file.mainclass()
        obj.gui_git(search.get())
    else:
        msg.showerror("Error","Please Select a option first!")
if __name__ == '__main__':
    root = Tk()
    root.geometry("800x150")
    root.title("Code Friend")

    search = StringVar()
    search.set("")

    frame = Frame(root,borderwidth=5)
    frame.grid(row=0, column=3)

    lb = Label(frame,text="Enter What you want to search",font="Helvetica 15 bold",fg="blue")
    lb.grid(row=0,column=4)

    tb= Entry(frame,textvar=search,font ="lucida 15 italic")
    tb.grid(row=0,column=5)

    choice = IntVar()
    google = Checkbutton(text="Google", variable=choice)
    google.grid(row=1, column=3)

    choice1 = IntVar()
    yt = Checkbutton(text="Youtube", variable=choice1)
    yt.grid(row=2, column=3)

    choice2 = IntVar()
    stack = Checkbutton(text="Stack Overflow", variable=choice2)
    stack.grid(row=3, column=3)

    choice3 = IntVar()
    git = Checkbutton(text="Github", variable=choice3)
    git.grid(row=4, column=3)

    bt=Button(frame,text="Search",font="lucida 15 italic")
    bt.bind("<Button-1>", click)
    bt.grid(row=0,column=6)


    root.mainloop()