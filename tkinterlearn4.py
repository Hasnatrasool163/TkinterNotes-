from tkinter import *

root =Tk()
root.title("mytkinter --window")
root.geometry("500x500")


#  creating frames in tkinters using simple attributes . 

f1=Frame(root,bg="grey",borderwidth=8,relief=SOLID).pack(side=LEFT,fill=Y)
f2=Frame(root,bg="green",borderwidth=6,relief=SUNKEN).pack(side=TOP,fill=X)

# we can pack everything in same lines also as done in line 10 and 11.

l1=Label(f1,fg="green",text="This is gui made in tkinter using vs code",font="TimesNewRoman 18 bold")
l1.pack(pady=22)

#  packing labels in  frames 


l1=Label(f2,fg="red",text="I am making frames in tkinter and packing in labels",font="TimesNewRoman 18 bold")
l1.pack(pady=22)

root.mainloop()