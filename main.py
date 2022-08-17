# Program made by MikeyDevCreate/Muv

# letting the user choose the background and foreground color
print("Hello! Welcome to Muv's Digital Clock!")
background = input("What color would you like the background? (type a color) : ")
foreground = input("And what color would you like the foreground? (type a color) : ")
font = input("Also! What size do you want the font to be? (type a number) : ")
print("Ok! Starting Program!")

# importing the whole tkinter module
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
# imports strftime from time to use to show us on the window
from time import strftime

# makes a window
window = Tk()
window.iconphoto(False, tk.PhotoImage(file='images/Clock.png'))
window.title("Muv's Digital Clock")

# the funtion that show the time on the screen
def show_time():
    string = strftime('%H:%M:%S %p')
    text_time.config(text = string)
    text_time.after(1000, show_time)

# the label of the time text on the screen
text_time = Label(window, font = ('calibri', font, 'bold'),background = background, foreground = foreground)

# show the label in the center of the screen
text_time.pack(anchor = 'center')
# run the show_time function
show_time()

# the main loop of the program
window.mainloop()
