# simple buttons use in tkinter .
from tkinter import *

root =Tk()
root.geometry("500x500") # width x height 
root.title("Simple gui window")

def add():
    print("enter your name")
def add2():
    print("enter your age")
def add3():
    print("enter your marks")
def add4():
    print("enter your final grade")
    
# made 4 functions that are used in 4 buttons

f1=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN).pack(side=LEFT,anchor=NW)

# we can make functions and use name without " " in button using keyword command= 
 
b1=Button(f1,fg="red",text="name",command=add).pack(side=LEFT,padx=22,anchor=NW)
b1=Button(f1,fg="red",text="age",command=add2).pack(side=LEFT,padx=22,anchor=NW)
b1=Button(f1,fg="red",text="marks",command=add3).pack(side=LEFT,padx=22,anchor=NW)
b1=Button(f1,fg="red",text="final grade",command=add4).pack(side=LEFT,padx=22,anchor=NW)







root.mainloop()