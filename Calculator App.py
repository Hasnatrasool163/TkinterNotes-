from tkinter import *
import tkinter.messagebox as m
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
import os
import sys



def simulate_loading():
    loading_text_label.config()
    #loading_text_label1.config()
    #loading_text_label2.config()
    h1_label.config() 

    progress_bar.stop()
    progress_bar.destroy()

    # Remove loading screen components
    h1_label.pack_forget()
    loading_text_label.pack_forget()
    #loading_text_label1.pack_forget()
    #loading_text_label2.pack_forget()

    # Display the calculator interface
    f.pack()


def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get().replace("X","*").replace("^","**"))

            except Exception as e:
                print(e)
                value = "Error"
                m.showwarning("Syntax error", "Illegal operation!")

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
        
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # Running as a script, use the current working directory
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def showtime():
    current_time=datetime.now().strftime("%H:%M:%S")
    m.showinfo("Current Time",f"The Current time is : {current_time}")

def open_about_window():
    about_window = tk.Toplevel(root,cursor="hand2",bg="white",relief=SOLID)
    about_window.title("About")

    # Add a label with an icon
    icon = tk.PhotoImage(file=resource_path("image1.png")) # Replace with your icon file
    label = ttk.Label(about_window,text="This is a Simple Gui Calculator version1.0",image=icon, compound="left")
    label.photo = icon  # Keep a reference to avoid garbage collection
    label.pack(pady=5,padx=5)
    
    label1=ttk.LabeL()
    #label.pack()
    # Set the window to read-only mode
    text = tk.Text(about_window, state="disabled", wrap="word")
    text.insert("1.0", "This is a read-only window.")
    text.pack()

script_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
image_path = os.path.join(script_dir, 'image1.png')

root = tk.Tk()

root.geometry("580x685")
root.minsize(500, 650)
root.maxsize(580, 685)
root.title("My calculator in Tkinter")
root.wm_iconbitmap("icon1.ico")
root.wm_iconposition(50,10)



loading_label = tk.Label()

loading_text_label = tk.Label(
    root, text="Calculator App by Muhammad Hasnat Rasool",bg="#333333", fg="green", font="ar 26 bold",wraplength=250,
)
loading_text_label.pack(pady=20, side="top", padx=5)
# loading_text_label2 = tk.Label(
#     root, text=" Designed By ",bg="#333333", fg="green", font="ar 30 bold"
# )
# loading_text_label2.pack(pady=20, side="top", padx=5)
# loading_text_label1 = tk.Label(
#     root, text="Muhammad Hasnat Rasool",bg="#333333", fg="green", font="ar 30 bold"
# )
# loading_text_label1.pack(pady=60, side="top", padx=10)

photo3 = tk.PhotoImage(file=resource_path("image1.png"))

# name then method PhotoImage then use file and name of png files


#loaded_image = Image.open(resource_path("image1.png"))# Replace with the path to your loaded image
resized_image=photo3.subsample(2,2)
# loaded_image = ImageTk.PhotoImage(resized_image)
# Add a loading animation using ttk.Progressbar
h1_label = tk.Label(root, image=resized_image)  # make label then image=name of ...
h1_label.pack(padx=50, pady=25)  # pack the label used above to display on screen!

progress_bar = ttk.Progressbar(
    root, mode="determinate", cursor="hand2", orient="horizontal", length=230
)
progress_bar.pack(pady=63, side="bottom")
progress_bar.start()
progress_bar.step(10)

root.after(5000, simulate_loading)

scvalue = StringVar()
scvalue.set("")
screen = Entry(
    root,
    cursor="ibeam",
    font="helvetica 35 bold",
    textvariable=scvalue,
    bg="white",
    justify="right",
    relief="sunken",
    fg="black"
    
)
screen.pack(pady=10, padx=12, ipadx=8, ipady=8, fill=X)

    
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="More Features", menu=file_menu)
file_menu.add_command(label="See Time", command=showtime)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About Calculator",command=open_about_window)
help_menu.add_command(
    label="About",
    command=lambda: tk.messagebox.showinfo(
        "About",
        "Calculator App by Muhammad Hasnat Rasool For more info contact on hasnatrasool163@gmail.com",
    ),
)


f = Frame(root, bg="grey")  #FF5733
a = Button(
    f,
    font="ar 30 ",
    text="C",
    borderwidth=5,
    justify="center",
    relief=SOLID,
    width=4,
    cursor="hand2",
    fg="red"
)
a.pack(side=LEFT, padx=10, pady=5)
a.bind("<Button-1>", click)
a = Button(
    f,
    font="ar 30 ",
    text="00",
    borderwidth=5,
    justify="center",
    relief=SOLID,
    cursor="hand2",
    width=4,
)
a.pack(side=LEFT, padx=10, pady=5)
a.bind("<Button-1>", click)
a = Button(
    f,
    font="ar 30 ",
    text="^",
    borderwidth=5,
    justify="center",
    relief=SOLID,
    cursor="hand2",
    width=4,
    fg="#FF5733"
    
)
a.pack(side=LEFT, padx=10, pady=5)
a.bind("<Button-1>", click)
a = Button(
    f,
    font="ar 30 ",
    text="/",
    borderwidth=5,
    justify="center",
    relief=SOLID,
    cursor="hand2",
    width=4,
    fg="#FF5733"
)
a.pack(side=LEFT, padx=10, pady=5)
a.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="grey")
b = Button(
    f,
    font="ar 30 ",
    text="9",
    borderwidth=5,
    padx=8,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
    
)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)
b = Button(
    f,
    font="ar 30 ",
    text="8",
    borderwidth=5,
    padx=8,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
    
)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)
b = Button(
    f,
    font="ar 30 ",
    text="7",
    borderwidth=5,
    padx=8,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)
b = Button(
    f,
    font="ar 30 ",
    text="X",
    borderwidth=5,
    padx=8,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
    fg="#FF5733"
)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
c = Button(
    f,
    font="ar 30 ",
    text="4",
    borderwidth=5,
    padx=9,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
)
c.pack(side=LEFT, padx=10, pady=5)
c.bind("<Button-1>", click)
c = Button(
    f,
    font="ar 30 ",
    text="5",
    borderwidth=5,
    padx=9,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
)
c.pack(side=LEFT, padx=10, pady=5)
c.bind("<Button-1>", click)
c = Button(
    f,
    font="ar 30 ",
    text="6",
    borderwidth=5,
    padx=9,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
)
c.pack(side=LEFT, padx=10, pady=5)
c.bind("<Button-1>", click)
c = Button(
    f,
    font="ar 30 ",
    text="-",
    borderwidth=5,
    padx=9,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
    fg="#FF5733"
)
c.pack(side=LEFT, padx=10, pady=5)
c.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
d = Button(
    f,
    font="ar 30 ",
    text="1",
    borderwidth=5,
    padx=10,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
)
d.pack(side=LEFT, padx=10, pady=5)
d.bind("<Button-1>", click)
d = Button(
    f,
    font="ar 30 ",
    text="2",
    borderwidth=5,
    padx=10,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
)
d.pack(side=LEFT, padx=10, pady=5)
d.bind("<Button-1>", click)
d = Button(
    f,
    font="ar 30 ",
    text="3",
    borderwidth=5,
    padx=10,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
)
d.pack(side=LEFT, padx=10, pady=5)
d.bind("<Button-1>", click)
d = Button(
    f,
    font="ar 30 ",
    text="+",
    borderwidth=5,
    padx=10,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
    fg="#FF5733"
)
d.pack(side=LEFT, padx=10, pady=5)
d.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
e = Button(
    f,
    font="ar 30 ",
    text="%",
    borderwidth=5,
    padx=10,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
    fg="#FF5733"
)
e.pack(side=LEFT, padx=10, pady=5)
e.bind("<Button-1>", click)
e = Button(
    f,
    font="ar 30 ",
    text="0",
    borderwidth=5,
    padx=10,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
)
e.pack(side=LEFT, padx=10, pady=5)
e.bind("<Button-1>", click)
e = Button(
    f,
    font="ar 30 ",
    text=".",
    borderwidth=5,
    padx=10,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
    fg="blue",
   
)
e.pack(side=LEFT, padx=10, pady=5)
e.bind("<Button-1>", click)
e = Button(
    f,
    font="ar 30 ",
    text="=",
    borderwidth=5,
    padx=10,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
     fg="black",
    bg="#ADD8E6"
)
e.pack(side=LEFT, padx=10, pady=5)
e.bind("<Button-1>", click)
f.pack()
Label(text="Muhammad Hasnat Rasool", fg="green", font="ar 15 bold", pady=1).pack(side="bottom",
     anchor="s", fill=X, pady=1
)
root.config(bg="white")#333333
root.mainloop()
