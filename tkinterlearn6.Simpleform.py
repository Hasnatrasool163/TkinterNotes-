from tkinter import *

root =Tk()
root.title("My tkinter window")
root.geometry("500x500")

def getvalues():
    print(f"The value of username entered is {username.get()}")
    print(f"The value of password entered is {password.get()}")
    
user =Label(root,text="User Name").grid()
password =Label(root,text="Password").grid(row=1)

# variable classes used in tkinter are as follows
#   BooleanVar , IntVar , DoubleVar , StringVar

username = StringVar()
password = StringVar()

# we can use entry for getting data in tkinter gui 
# grid are likes cell is excel with rows and columns 
# we have to mention same variable named with defined data types without " "

userentry = Entry(root,textvariable=username).grid(row=0,column=1)
passentry = Entry(root,textvariable=password).grid(row=1,column=1)

Button(text="Submit",command=getvalues).grid()

root.mainloop()