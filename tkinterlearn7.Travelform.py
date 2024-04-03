from tkinter import *

# made a from for simple travel agency that takes some inputs and data is saved in file 
# file is opened in apend mode
root= Tk()

root.geometry("444x333")
root.minsize(400,300)
root.maxsize(500,400)
root.title("Travel Agency Form")
# functions used
def getvalues():
    print("Processing your Application")
    print(f"{Name.get(),
    Phone.get(),
    Gender.get(),
    Emergency.get(),
    Payment.get(),
    Foodservice.get()}\n")
    message.config(text="Your application is Submitted",fg="green")
    with open("records.txt","a") as f:
        f.write(f"{Name.get(),Phone.get(),Gender.get(),Emergency.get(),Payment.get(),Foodservice.get()}\n")
   
# labels added in the form
Label(text="Travel Agency",fg="green",padx=15,font="TimesNewRoman 20 bold",pady=15,anchor=NE).grid(row=0,column=2)
message=Label(root,text="Info will Appear here",fg="black")
message.grid(row=1,column=2)

Name=Label(root,text="Name->",padx=5,fg="blue",width=18,font="ar 10 bold",relief=RAISED,underline=100).grid(row=2,column=1)
Phone=Label(root,text="Phone->",padx=5,fg="blue",width=18,font="ar 10 bold",relief=RAISED).grid(row=3,column=1)
Gender=Label(root,text="Gender->",padx=5,fg="blue",width=18,font="ar 10 bold",relief=RAISED).grid(row=4,column=1)
Emergency=Label(root,text="Emergency contact->",padx=5,fg="blue",width=18,font="ar 10 bold",relief=RAISED).grid(row=5,column=1)
Payment=Label(root,text="Paymentmode->",padx=5,fg="blue",width=18,font="ar 10 bold",relief=RAISED).grid(row=6,column=1)
Foodservice=Label(root,text="FoodService->",padx=5,fg="blue",width=18,font="ar 10 bold",relief=RAISED).grid(row=7,column=1)

# data types used
Name =StringVar()
Phone =StringVar()
Gender =StringVar()
Emergency =StringVar()
Payment =StringVar()
Foodservice =IntVar()


# enteries defined to get data from user 


Nameval=Entry(root,textvariable=Name).grid(row=2,column=2)
Phoneval=Entry(root,textvariable=Phone).grid(row=3,column=2)
Genderval=Entry(root,textvariable=Gender).grid(row=4,column=2)
Emergencyval=Entry(root,textvariable=Emergency).grid(row=5,column=2)
Paymentval=Entry(root,textvariable=Payment).grid(row=6,column=2)

#Serviceval=Entry(root,textvariable=Foodservice).grid(row=7,column=2)

# checkbox for food service
Food=Checkbutton(variable=Foodservice,text="Want Food service",font="ar 10 bold",borderwidth=4,relief=SUNKEN).grid(row=7,column=2)

# buttons used for form
Button(text="Submit",command=getvalues,font="ar 10 bold",borderwidth=5,pady=3).grid(row=8,column=2)
Button(text="Quit",command=quit,font="ar 10 bold",borderwidth=4,pady=3).grid(row=9,column=2)
root.mainloop()
