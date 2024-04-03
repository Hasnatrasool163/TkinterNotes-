from tkinter import *
import tkinter.messagebox as tmsg


root =Tk()
root.title("Slider of performance")
root.geometry("333x333")
def Print():
    value =tmsg.askquestion("Surety Checker"," Are you sure about your selection")
    print(value)
    if value =="yes":
        msg="You must learn more langauges"
    else:
        msg="Be honest Next time i have noted you "
    tmsg.showinfo("Experience",msg)
def Statushow():
    status.set("Busy...")
    sbar.update()
    import time
    time.sleep(2)
    status.set("Ready")
    
Label(root,text="How many programming languages you know?",fg="red",font="helvetica 20 bold").pack(pady=20)

myslider1=Scale( length=220, from_=0 , to=10,orient=HORIZONTAL,tickinterval=1,relief=SUNKEN,fg="green",font="helvetica 15 bold",width=20,cursor="hand2" )
myslider1.set(1)
myslider1.pack(pady=10)

status =StringVar()
status.set("Ready")

Button(root,text="Submit",command=Print,font="helvetica 10 bold",borderwidth=5,border=6,cursor="circle").pack(pady=10)
Button(root,text="Status",command=Statushow,font="helvetica 10 bold",borderwidth=5,border=6,cursor="arrow").pack(pady=10)

sbar=Label(text="Ready",font="helvetica 12 bold",textvariable=status,relief=SUNKEN,anchor=W)
sbar.pack(side=BOTTOM,fill=BOTH)
root.mainloop()