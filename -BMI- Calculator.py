# This is full code of my -BMI- Calculator app .
# i have added some key bindings
# this code is written in python using tktinter and custom tkinter with pillow


###########################NECESSARY-IMPORTS################################################


from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import os, sys, time
from tkinter import messagebox as m

###########################NECESSARY-IMPORTS################################################


#####################################APPERANCE-MODE#################################
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
# customtkinter.set_default_color_theme("GreyGhost")
#####################################APPERANCE-MODE#################################

############################MAIN-WINDOW-#################################################
root = customtkinter.CTk()

######################################START######################################
root.title(" - BMI Calculator --")
# root.iconbitmap('myicon.ico')
root.geometry("500x670")
root.resizable(False, False)

# FUNCTION ADDED TO MAKE EXE FILE USING PYINSTALLER AND TO ADD IMAGES SAFELY
# root.wm_overrideredirect(True)
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # Running as a script, use the current working directory
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Define Our Image
meter = ImageTk.PhotoImage(Image.open(resource_path("meter2.png")))
meter_img = Label(root, image=meter, bd=0)
meter_img.pack(pady=10)

# CLEAR SCREEN FUNCTION!


def clear_screen(Event):
    h_entry.delete(0, END)
    w_entry.delete(0, END)
    results.configure(text="")

# MAIN FUNCTION TO CALCULATE BMI


def get_bmi(*args):
    # calculate BMI
    # (weight_pounds/height_inches^2) * 703

    our_height = float(h_entry.get())

    our_weight = float(w_entry.get())
    bmi = ((our_weight / 0.453592)) / ((our_height * 12) ** 2) * 703
    bmi_rounded = round(bmi, 2)

    results.configure(text=f"{str(bmi_rounded)}")

    # Logic
    if bmi_rounded < 18.5:
        results.configure(
            text=f"{str(bmi_rounded)}😗\nUnderweight\n🙄 ",text_color="#54b1e1"
        )
    elif bmi_rounded >= 18.5 and bmi_rounded <= 24.9:
        results.configure(text=f"{str(bmi_rounded)}\nNormal\n✌✌", text_color="#b3d686")

    elif bmi_rounded >= 25.0 and bmi_rounded <= 29.9:
        results.configure(
            text=f"{str(bmi_rounded)}\nOverweight\n😜", text_color="#fed429"
        )

    elif bmi_rounded >= 30.0 and bmi_rounded <= 34.9:
        results.configure(text=f"{str(bmi_rounded)}\nObese\n😊", text_color="#fbaf42")

    elif bmi_rounded >= 35:
        results.configure(
            text=f"{str(bmi_rounded)}\n😅\nExtreme Obese\n😂", text_color="#f2535"
        )
		

h1_label = customtkinter.CTkLabel(master=root, text="", font=("helvetica", 15, "bold"))
h1_label.pack(pady=0)

# Define Entry Boxes
h_entry = customtkinter.CTkEntry(
    master=root,
    placeholder_text="Height In Foot",
    width=200,
    height=30,
    border_width=1,
    corner_radius=10,
)
h_entry.pack(pady=20)
h_entry.bind(
    "<FocusIn>",
    lambda e: h1_label.configure(text="Height in feet😁" ,text_color="#8D6F3A",
))
h_entry.bind("<FocusOut>", lambda e: h1_label.configure(text=""))


h2_label = customtkinter.CTkLabel(master=root, text="", font=("helvetica", 15, "bold"))
h2_label.pack(pady=0)


w_entry = customtkinter.CTkEntry(
    master=root,
    placeholder_text="Weight in Kg",
    width=200,
    height=30,
    border_width=1,
    corner_radius=10,
)
w_entry.pack(pady=20)
w_entry.bind(
    "<FocusIn>",
    lambda e: h2_label.configure(text="Weight in kg😎" ,text_color="#98FB98",
))
w_entry.bind("<FocusOut>", lambda e: h2_label.configure(text=""))


# Buttons !
button_1 = customtkinter.CTkButton(
    master=root,
    text="Calculate BMI",
    width=190,
    height=40,
    compound="top",
    command=get_bmi,
)
button_1.pack(pady=20)


button_2 = customtkinter.CTkButton(
    master=root,
    text="Clear Screen",
    width=190,
    height=40,
    fg_color="#D35B58",
    hover_color="#C77C78",
    command=clear_screen,
)
button_2.pack(pady=20)
root.bind("<Control-Key-c>", clear_screen)
# result
results = customtkinter.CTkLabel(master=root, text="", font=("Helvetica", 28))
results.pack(pady=50)


# VALIDATION PURPOSE!

def checkempty():
    if h_entry.get() == "" or w_entry.get() == "":
        m.showerror("--BMI--Calculator", "Enter Values first to Calculate")
    else:
        pass


def on_enter(event):
    checkempty()
    get_bmi()


def move_up(event):
    h_entry.focus_set()


def move_down(event):
    w_entry.focus_set()


def end_it(*args):
    root.destroy()


# KEY BINDINGS!

root.bind("<Up>", move_up)
root.bind("<Down>", move_down)
root.bind("<Return>", on_enter)  # enter key
root.bind("<KeyPress-Escape>", end_it)


# TOP LVL WINDOW TO SHOW SHORTCUTS LIST!
def open_about_window(*args):
    about_window = customtkinter.CTkToplevel(root)
    about_window.title("Short-Cut-Keys")
    about_window.geometry("700x500")
    about_window.resizable(False, False)

    # Add a label with an icon
    bg_image = customtkinter.CTkImage(
        Image.open(resource_path("mhr.jpg")),
        size=(50, 50),
    )
    bg_image_label = customtkinter.CTkLabel(about_window, image=bg_image, text="")
    bg_image_label.pack()

    # Set the window to read-only mode
    my_text = customtkinter.CTkTextbox(
        about_window,
        width=600,
        height=300,
        corner_radius=1,
        border_width=10,
        border_color="#FFCC70",
        border_spacing=10,
        fg_color="silver",
        text_color="#8D6F3A",
        font=("Helvetica", 22),
        wrap="word",  # Char default, word, none
        activate_scrollbars=True,
        scrollbar_button_color="#FFCC70",
        scrollbar_button_hover_color="red",
    )
    my_text.pack(pady=20)

    my_text.insert(
        1.0,
        text="\t\t\"Short Cut Key\" 😁\n\n-->Ctrl+s \t\t For opening Shortcuts\n-->Ctrl+c \t\t For Clearing Values \n-->Ctrl+Esc \t\t For Exiting\n-->Up arrow \t\t For moving up\n-->Down-Arrow \t\t For Moving Down\n-->Enter-Key \t\t For Calculating BMI-index\n\n\t😍\t\t😍"
    )


short_b = customtkinter.CTkButton(root, text="shortcut-keys", command=open_about_window)
short_b.pack()
root.bind("<Control-KeyPress-s>", open_about_window)
# notify_user()
# root.after(10000,notify_user)

# main loop start !

root.mainloop()

#################################################-END-###########################################################
