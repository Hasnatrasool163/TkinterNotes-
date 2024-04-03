from tkinter import *

root=Tk()
Canvas_Width=800
Canvas_Height=600
root.geometry(f"{Canvas_Width}x{Canvas_Height}")
can_widget=Canvas(root,width=Canvas_Width,height=Canvas_Height)
can_widget.pack()
# we can create line by providing coordinates x1y1 to x2,y2
# can_widget.create_line(0,0,800,600,fill="red")
# can_widget.create_line(0,600,800,0,fill="red")

# we can draw rectangle by giving coordinates of top left and right bottom
can_widget.create_rectangle(3,5,700,500,fill="blue")

# we can draw oval same like using coordinates of rectangle 
can_widget.create_oval(3,5,700,500,fill="red")

# we can draw text by providing coordinates of x and y
# can_widget.create_text(300,300,text="Python with Tkinter")

root.mainloop()