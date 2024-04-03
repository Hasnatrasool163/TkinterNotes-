from tkinter import * # by using asterik(*)i have imported everything from tkinter 

# in tkinter we can use widgets 
# we can delcare all classes and buttons , labels , enteries start from took=Tk()end on root.mainloop()
root=Tk()
# 2 parameters width x size 
# defualt size in which tkinter window opens is set from root.geometry!
root.geometry("800x600")

# 2 functions exist to set min and max size of gui window 
root.minsize(222,333)
root.maxsize(999,888)
# 2 functions exist to set min and max size of gui window
 
# function to add any name on tkinter window 
root.title("mytkinterwindow")

# label code ( label cannot be used by user on screen!)
# nothings prints on gui so we have to pack it before to get displayed on screen!
hasnat=Label(text="This is a GUI label")
hasnat.pack()

root.mainloop()