#MAIN File
#make gui part here
#importing
import cui_file
from tkinter import * #import all from tkinter. tkinter is inbuilt python library. if it's not installed run 'pip install tkinter'
import tkinter.messagebox as msg

#A Function to be called when button is clicked
def click(event):
    if choice.get()==1:
        obj=cui_file.mainclass() #Create a object from cuifile of a mainclass
        #search.get()- .get funtion is used to get the data from a variable. in this case, get the data from search variable.
        obj.gui_g(search.get()) #send the data received in search variable to gui_g function in cui_file
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
if __name__ == '__main__': #The main program execution starts here.
#Frontend Developers Work Here..................
    root = Tk() #Initialize Tkinter as Root
    root.geometry("800x150") #Set Main Frame Size
    root.title("Code Friend") #Set it's title
    #Take a empty string variable to store search string
    search = StringVar()
    search.set("")
    #Define the main frame and it's properties.
    frame = Frame(root,borderwidth=5)
    frame.grid(row=0, column=3) #Grid function places the elements in a grid format.
    #Take a label as lb and define it's properties
    lb = Label(frame,text="Enter What you want to search",font="Helvetica 15 bold",fg="blue")
    lb.grid(row=0,column=4) #Place the label on the grid
    #Make a textbox and place it
    tb= Entry(frame,textvar=search,font ="lucida 15 italic")
    tb.grid(row=0,column=5)
    #make a Checkbox and place it
    choice = IntVar() #Choice can either be 1 for true and 0 for false, hence made the choice as an integer variable
    google = Checkbutton(text="Google", variable=choice)
    google.grid(row=1, column=3)
    #Same as above
    choice1 = IntVar()
    yt = Checkbutton(text="Youtube", variable=choice1)
    yt.grid(row=2, column=3)
    #same as above
    choice2 = IntVar()
    stack = Checkbutton(text="Stack Overflow", variable=choice2)
    stack.grid(row=3, column=3)

    choice3 = IntVar()
    git = Checkbutton(text="Github", variable=choice3)
    git.grid(row=4, column=3)
    #Make a button
    bt=Button(frame,text="Search",font="lucida 15 italic")
    bt.bind("<Button-1>", click) #bind the button to the click function
    bt.grid(row=0,column=6)
    #root.mainloop makes shure that the gui keeps running until pressed close
    root.mainloop()