from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.geometry('600x600')

j = 0
image1 = Image.open("button.png")
photo1 = ImageTk.PhotoImage(image1)
label1 = tk.Label(image=photo1)
label1.place(relx=j, rely=0.1, width=500, height=650)

image2 = Image.open("anotherlogo.png")
photo2 = ImageTk.PhotoImage(image2)
label2 = tk.Label(image=photo2)
label2.place(relx=j, rely=0.1, width=500, height=650)

image3 = Image.open("goldenbootrace_1.png")
photo3 = ImageTk.PhotoImage(image3)
label3 = tk.Label(image=photo3)
label3.place(relx=j, rely=0.1, width=500, height=650)

image4 = Image.open("country_1_edited.png")
photo4 = ImageTk.PhotoImage(image4)
label4 = tk.Label(image=photo4)
label4.place(relx=j, rely=0.1, width=500, height=650)

image5 = Image.open("country1_1_borrowed.png")
photo5 = ImageTk.PhotoImage(image5)
label5 = tk.Label(image=photo5)
label5.place(relx=j, rely=0.1, width=500, height=650)

def slide_images():
    global j
    global i
    i += 1
    j += 0.01
    if i == 1:
        label1.place(relx=j, rely=0.1, width=500, height=650)
    elif i == 2:
        label2.place(relx=0.5, rely=0.1, width=500, height=650)
    elif i == 3:
        label3.place(relx=0.5, rely=0.1, width=500, height=650)
    elif i == 4:
        label4.place(relx=0.5, rely=0.1, width=500, height=650)
    elif i == 5:
        label5.place(relx=0.5, rely=0.1, width=500, height=650)

    root.after(2000, slide_images)



i = 0
#root.after(2000, slide_images)
button = tk.Button(root, text="Slide Images", command=slide_images)
button.pack()

root.mainloop()
