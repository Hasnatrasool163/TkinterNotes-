from tkinter import *
from PIL import Image ,ImageTk
import os
# for jpg images we can use pip install pillow and then use jpg images in tkinter window
root=Tk()

root.geometry("550x700")
# to display picture in tkinter we need to use a label then pack that as same as we did for text
# we have to use pnj picture by saving it in same folder where our file is saved

photo3 = PhotoImage (file="image1.png") # name then method PhotoImage then use file and name of png files
h1_label=Label(image=photo3) # make label then image=name of ...
h1_label.pack() #pack the label used above to display on screen!
# for jpg images

# image=Image.open("OIP.jpg")
# photo=ImageTk.PhotoImage(image)
# hasnat_label=Label(image=photo)
# hasnat_label.pack()
# image=Image.open("image1.jpg")
# photo0=ImageTk.PhotoImage(image)
# hamza_label=Label(image=photo0)
# hamza_label.pack()
# image=Image.open("image2.jpeg")
# photo1=ImageTk.PhotoImage(image)
# haider_label=Label(image=photo1)
# haider_label.pack()


root.mainloop()