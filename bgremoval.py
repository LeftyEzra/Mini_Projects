"""from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
from rembg import remove

window = Tk()
window.configure(bg="black")
window.geometry("800x600")
window.title('image background removal')
window.resizable(False,False)

def  open_file():
    x = filedialog.askopenfilename(title="Select Image file path to open:")
    image = Image.open(x)
    global image_Nobg
    image_Nobg = remove(image)

    image.thumbnail(size=(500,500))
    render = ImageTk.PhotoImage(image)
    label.configure(image=render)
    label.image=render

def save_file():
    y = filedialog.asksaveasfilename(title='Save Image to: ')
    image_Nobg.save(y)
    image = Image.open(y)
    image.thumbnail(size=(500,500))
    render = ImageTk.PhotoImage(image)
    label.configure(image= render)
    label.image = render



frame = tk.Frame(window,width=500,height=500,background="grey")
frame.pack(padx=10,pady=10)
label = tk.Label(frame,)
label.place(x=5,y=5)

button1 = tk.Button(window,text="Open file",width=15,
                              command=open_file)
button1.place(x= 130, y=530)

button2 = tk.Button(window,text="Save file",command=save_file,width=15)
button2.place(x= 250, y=530)

window.mainloop()"""
import time

import time

def decrement_time(self):
    global minutes, seconds, seconds_24, running, milli_seconds
    if seconds > 0 and not running:
        seconds -= 1
    elif minutes > 0 and not running:
        minutes -= 1
        seconds = 59

    if seconds_24 > 0 and not running:
        milli_seconds -= 1000
        seconds_24 -= 1

        self.update_shot_clock()
        self.window.after(1, self.decrement_time)

"""import PIL.Image

ASCII_CHARS = ["B","S","#","&","#","$","%","*","!",":","."]
#Resize image to a new width
def resize_image(image, new_width= 100):
    width,height  = image.size
    image_ratio   = height / width
    new_height    = int(new_width * image_ratio)
    resized_image = image.resize(new_width,new_height)
    return(resized_image)

#Convert the image pixel to a gray scale
def grayish_color(image):
    gray_image = image.convert("L")
    return(gray_image)

#Convert pixels to ascii
def pixels_to_ascii(image):
    pixels     = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)


#defining a main function that will print the convert

def main():
    image_path = input("Enter a valid image path to convert:\n")
    try:
        image = PIL.Image.open(image_path)

with open("image_2_ascii_chars.txt",'w') as f:
    f.write(image_2_ascii_chars)"""

