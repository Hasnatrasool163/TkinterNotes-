from tkinter import *

root =Tk()
root.geometry("500x400")
root.title(" GUI IN TKINTER ")

# important things about label in tkinter
# text used to add any text in any label!
# fg stands for foreground
# bg stands for background
# padx stands for padding in x -axis
# pady stands for padding in y-axis
# font is used to select font and size of font with style
# 1. font=("TimesNewRoman",20,"bold") # with tuple     # name of style for font must be all in lowercases
# 2.font="TimesNewRoman 20 bold"      # without tuple  # name of style for font must be all in lowercases
# relief used for border styling ( SUNKEN ,RAISED,GROOVE,RIDGE,SOLID) # relief=SOLID

# PRACTISE FOR LABEL ATTRIBUTES

# bg="green",fg="white",padx="15",pady="20",font="TimesNewRoman 20 bold",borderwidth=3,relief=SOLID # example

# my_label =Label(text='''Hello i am using a computer language named python version 3.12.1 time 7.28 pm date 1/5/2024 
#                 i am using tkinter for gui ''') # using triple doubles as a string
# i have to pack this before then it will display on tkinter window

my_label =Label(text='''Hello i am using a computer language named python version 3.12.1 time 7.28 pm date 1/5/2024 
                i am using tkinter for gui ''',bg="green",fg="white",padx="15",pady="20",font="TimesNewRoman 20 bold",borderwidth=3,relief=SOLID) # now i have used 2 colors green for background of label
# and white for forground of label here i mean by the text written!
# the next things is padding means some space from x -axis and y -axis .

# important pack options 

# anchor =nw ( northwest,southwest,southeast etc)
# side ( top,left,right,bottom)
# fill used to fill space in x or y direction ( capital X Y is used)
# padx same
# pady same

my_label.pack(anchor="se",side=RIGHT,fill="y",padx="20",pady="20") # move label to north west side
# label will be exact at centre now both padding constant 




root.mainloop()