from tkinter import *
import tkinter.messagebox as m

root=Tk()
root.title("Menu-in Tkinter")
root.geometry("500x400")

def func():
    print("hello")
# example of non drop down menu
# mainmenu=Menu(root)
# mainmenu.add_command(label="File",command=func)
# mainmenu.add_command(label="quit",command=quit)
# root.config(menu=mainmenu)
def help():
    m.askretrycancel("User experience prompt","Do you like this app ",)
    



# example of message box 



# drop down menu example 

mainmenu = Menu(root)
m1 = Menu(mainmenu,tearoff=0,fg="black")
m1.add_command(label="Newfile",command=help)
m1.add_command(label="NewWindow",command=func)
m1.add_command(label="NewTextFile",command=func)
m1.add_separator()
m1.add_command(label="Openfile",command=func)
m1.add_command(label="Openfolder",command=func)
m1.add_command(label="OpenRecent",command=func)
m1.add_separator()
m1.add_command(label="Save",command=func)
m1.add_command(label="SaveAs",command=func)
mainmenu.add_cascade(label="File",menu=m1)


m2 = Menu(mainmenu,tearoff=0)
m2.add_command(label="Undo Ctrl+Z",command=func,foreground="black")
m2.add_command(label="Redo Ctrl+Y",command=func)
m2.add_separator()
m2.add_command(label="Cut Ctrl+X",command=func)
m2.add_command(label="Copy Ctrl+C",command=func)
m2.add_command(label="Paste Ctrl+V",command=func)
m2.add_separator()
m2.add_command(label="Find Ctrl+F",command=func)
m2.add_command(label="Replace Ctrl+H",command=func)
m2.add_command(label="FindinFiles Ctrl+Shift+F",command=func)
mainmenu.add_cascade(label="Edit",menu=m2)

m3 = Menu(mainmenu,tearoff=0)
m3.add_command(label="Newfile",command=func)
m3.add_command(label="NewWindow",command=func)
m3.add_command(label="NewTextFile",command=func)
m3.add_separator()
m3.add_command(label="Openfile",command=func)
m3.add_command(label="Openfolder",command=func)
m3.add_command(label="OpenRecent",command=func)
m3.add_separator()
m3.add_command(label="Save",command=func)
m3.add_command(label="SaveAs",command=func)
mainmenu.add_cascade(label="Selection",menu=m3)

m4 = Menu(mainmenu,tearoff=0)
m4.add_command(label="Newfile",command=func)
m4.add_command(label="NewWindow",command=func)
m4.add_command(label="NewTextFile",command=func)
m4.add_separator()
m4.add_command(label="Openfile",command=func)
m4.add_command(label="Openfolder",command=func)
m4.add_command(label="OpenRecent",command=func)
m4.add_separator()
m4.add_command(label="Save",command=func)
m4.add_command(label="SaveAs",command=func)
mainmenu.add_cascade(label="View",menu=m4)

m5 = Menu(mainmenu,tearoff=0,fg="blue",relief=SOLID)
m5.add_command(label="Newfile",command=func)
m5.add_command(label="NewWindow",command=func)
m5.add_command(label="NewTextFile",command=func)
m5.add_separator()
m5.add_command(label="Openfile",command=func)
m5.add_command(label="Openfolder",command=func)
m5.add_command(label="OpenRecent",command=func)
m5.add_separator()
m5.add_command(label="Save",command=func)
m5.add_command(label="SaveAs",command=func)
mainmenu.add_cascade(label="Go",menu=m5)

m6 = Menu(mainmenu,tearoff=0,relief=RAISED,fg="green")
m6.add_command(label="Newfile",command=func)
m6.add_command(label="NewWindow",command=func)
m6.add_command(label="NewTextFile",command=func)
m6.add_separator()
m6.add_command(label="Openfile",command=func)
m6.add_command(label="Openfolder",command=func)
m6.add_command(label="OpenRecent",command=func)
m6.add_separator()
m6.add_command(label="Save",command=func)
m6.add_command(label="SaveAs",command=func)
mainmenu.add_cascade(label="Run",menu=m6)




root.config(menu=mainmenu)

root.mainloop()