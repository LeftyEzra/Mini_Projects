import customtkinter
from selenium import webdriver
from PIL import Image
import ttkbootstrap
import sqlite3
from tkinter import messagebox
import bcrypt
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

window = customtkinter.CTk()
window.geometry("500x500")
window.title('Lefty')
window.resizable(True,True)

photo1 =customtkinter.CTkImage(light_image=Image.open("Basketballcourt.png"),size=(1500,1000))
bg_pic= customtkinter.CTkLabel(window,image=photo1,)
bg_pic.pack()


#connection.execute(table_create_query)




def google():
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detatch', True)
    driver = webdriver.Chrome(options=option)
    driver.get("https://www.google.com/")

def facebook():
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detatch', True)
    driver = webdriver.Chrome(options=option)
    driver.get("https://www.facebook.com/")
conn = sqlite3.connect('Login.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS login_data
                                (username TEXT , password TEXT )
                       ''')
def signup():
    username = entry1.get()
    password = entry2.get()
    if username != "" and password != "":
        c.execute('SELECT username FROM login_data WHERE username=(?)',[username])
        if c.fetchone() is not None:
            messagebox.showerror('Error',"Username already exists")
        else:
            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password,bcrypt.gensalt())
            print(hashed_password)
            c.execute('INSERT INTO login_data VALUES(?, ?)',[username,hashed_password])
            messagebox.showinfo("Success!","Your account has been created ):")
    else: messagebox.showerror("Error", "Enter all data")

def login_account():
    username = login_username.get()
    password = login_password.get()
    if username != "" and password != "":
        c.execute('SELECT password FROM login_data WHERE username=(?)',[username])
        result = c.fetchone()
        if result:
            if bcrypt.checkpw(password.encode('utf-8'),result[0]):
                messagebox.showinfo('Success',"Welcome!")
            else: messagebox.showerror("Error"," Incorrect password ")
        else:
            messagebox.showerror("Error","Incorrect username :)")
    else: messagebox.showerror("Error", "Enter all data")
def login():
    frame1.destroy()
    login_frame = customtkinter.CTkFrame(window,width=400,height=400,corner_radius=5,fg_color='#010203')
    login_frame.place(relx=0.5,rely=0.55,anchor='center')

    label1 = customtkinter.CTkLabel(login_frame, text="          Login ",
                                    text_color="orange",font=("Roboto", 24), compound='top')
    label1.place(x=95, y=40)
    global login_username
    global login_password

    login_username = customtkinter.CTkEntry(login_frame, placeholder_text="Username", width=210)
    login_username.place(x=95, y=100)

    login_password = customtkinter.CTkEntry(login_frame, placeholder_text="Password", show="*", width=210,
                                    placeholder_text_color='green', )
    login_password.place(x=95, y=160)

    login_button = customtkinter.CTkButton(login_frame, text="Login", width=210,command=login_account )
    login_button.place(x=95, y=220)

frame1 = customtkinter.CTkFrame(window,width=400,height=400,corner_radius=5,fg_color='#010203')
frame1.place(relx=0.5,rely=0.55,anchor='center')

label = customtkinter.CTkLabel(frame1, text="Lefty Login System", font=("Roboto",24),compound='top')
label.place(x=95,y=40)

entry1 =customtkinter.CTkEntry(frame1, placeholder_text="Username",width=210)
entry1.place(x=95,y=100)

entry2 =customtkinter.CTkEntry(frame1, placeholder_text="Password",show="*",width=210,placeholder_text_color='green',)
entry2.place(x=95,y=160)

label =customtkinter.CTkLabel(frame1,text="forgot password?",bg_color='transparent')
label.place(relx=0.5,rely=0.47)
button =customtkinter.CTkButton(frame1, text="Login",width=210,command=login)
button.place(x=95,y=220)

checkbox =customtkinter.CTkCheckBox(frame1,text="Remember Me",)
checkbox.place(relx=0.25,rely=0.63)

photo2 =customtkinter.CTkImage(light_image=Image.open("GOOGLELOGO.PNG"),size=(20,20),)
photo3 =customtkinter.CTkImage(light_image=Image.open("FACEBOOK1.PNG"),size=(20,20))
button_gg =customtkinter.CTkButton(frame1,
                                   text='Google',image=photo2,
                                   compound='left',
                                   command=google,
                                   text_color="black",width=100,height=20,
                                   fg_color='white')
button_gg.place(relx=0.25,rely=0.75)
button_fb =customtkinter.CTkButton(frame1,
                                   text='Facebook',image=photo3,
                                   command=facebook,
                                   compound='left',
                                   text_color="black",width=90,
                                   fg_color="white")
button_fb.place(relx=0.51,rely=0.75)
signup_button =customtkinter.CTkButton(frame1,
                                   text='Sign-up',
                                   command=signup,
                                   text_color="white",width=200,
                                   fg_color="green")
signup_button.place(relx=0.25,rely=0.85)

window.mainloop()
"""import random
#import os

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

#window = customtkinter.CTk()
#window.geometry("600x600")
#window.title("Lefty Customstkinter projects")

GAME_WIDTH = 700
GAME_HEIGHT =700
SPEED = 300
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "red"

class Snake:
    def __init__(self):
        self.body_size  = BODY_PARTS
        self.coordinates = []
        self.squares    = []
        #self.running = True

        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tags="Snake")
            self.squares.append(square)
class Food:
    def __init__(self):
        x = random.randint(0,int(GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x,y]

        canvas.create_oval(x,y,x+ SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tags="food" )
def Next_turn(snake,food):
    global SPEED
    x,y =snake.coordinates[0]
    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE
    snake.coordinates.insert(0,(x,y))

    square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)
    snake.squares.insert(0,square)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.configure(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()
        if score == 3:
            SPEED = 250
        if score == 6:
            SPEED = 200
        if score == 9:
            SPEED =150
        if score == 9:
            SPEED = 100
        if score == 12:
            SPEED = 50
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED,Next_turn,snake,food)





def change_direction(new_direction):
    global direction
    global score
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):
    x,y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    if y < 0 or y >= GAME_HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():
    canvas.delete("all")
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,
                       font=("Gothic",70),text="GAME OVER!!!\nYour Scores:{}".format(score),fill='red',tags="'gameover")
    label.configure(text="Play Again?")


def play_again():

    if reset_button:
        canvas.configure(Next_turn(snake,food))
        return Next_turn(snake,food)







window = customtkinter.CTk()
window.title("Lefty Snake Game")
window.resizable(False,False)

score = 0
direction= "down"

label = customtkinter.CTkLabel(window,text=("Score:{}".format(score)),font=("Gothic",30))

label.pack()
canvas = customtkinter.CTkCanvas(window,width=GAME_WIDTH,height=GAME_HEIGHT,bg="black")
canvas.pack()

reset_button = customtkinter.CTkButton(window,text='restart',font=('Gothic',20),width=20,command=play_again
                                       )
reset_button.place(relx=0.85,rely=0.1 )
window.update()

window_width = window.winfo_width()
window_height = 550
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2)-(window_width/2))
y =  int((screen_height/2)-(window_height/2))

window.geometry(f'{window_width}x{window_height}+{x}+{y}')
window.bind('<Left>',lambda  event: change_direction('left'))
window.bind('<Right>',lambda  event: change_direction('right'))
window.bind('<Up>',lambda  event: change_direction('up'))
window.bind('<Down>',lambda  event: change_direction('down'))

snake = Snake()
food = Food()
Next_turn(snake,food)




window.mainloop()"""
"""
import random
import os

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

window = customtkinter.CTk()
window.geometry("600x550")
window.title("Lefty Customstkinter projects")

label= customtkinter.CTkLabel(window,fg_color="transparent",text="Puzzle game",text_color="orange",corner_radius=5,anchor="n",
                              font=("Gothic",40))
label.pack(side='top')
frame = customtkinter.CTkFrame(window,width=400,height=400,border_width=1)
frame.pack()
def move_button():
    global button_x
    button_x += 0.01
    if button_x < 0.9:
         window.after(50,move_button)

    colors= ['red','blue','green','white','orange','purple']
    color = random.choice(colors)




button1 = customtkinter.CTkButton(frame,text='A',width=100,height=100,fg_color='blue',corner_radius=0)
button2 = customtkinter.CTkButton(frame,text='B',width=100,height=100,fg_color='blue',corner_radius=0)
button3 = customtkinter.CTkButton(frame,text='C',width=100,height=100,fg_color='blue',corner_radius=0)

button4 = customtkinter.CTkButton(frame,text='D',width=100,height=100,fg_color='blue',corner_radius=0)
button5 = customtkinter.CTkButton(frame,text='E',width=100,height=100,fg_color='blue',corner_radius=0)
button6 = customtkinter.CTkButton(frame,text='F',width=100,height=100,fg_color='blue',corner_radius=0)

button7 = customtkinter.CTkButton(frame,text='G',width=100,height=100,fg_color='blue',corner_radius=0)
button8 = customtkinter.CTkButton(frame,text='H',width=100,height=100,fg_color='blue',corner_radius=0)
#button9 = customtkinter.CTkButton(frame,text='',width=100,height=100,fg_color='blue',corner_radius=0,command=lambda:b_clicked(button9))



frame.columnconfigure(0,weight=1,uniform='a')
frame.columnconfigure(1,weight=1,uniform='a')
frame.columnconfigure(2,weight=1,uniform='a')
frame.rowconfigure(0,weight=1,uniform='a')
frame.rowconfigure(1,weight=1,uniform='a')
frame.rowconfigure(2,weight=1,uniform='a')

button1.grid(row=0,column=0,padx=1,pady=1)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)
button4.grid(row=1,column=0)
button5.grid(row=1,column=1)
button6.grid(row=1,column=2)
button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
#button9.grid(row=2,column=2)
"""
"""from docxtpl import DocxTemplate
import customtkinter
#from random import randint, choice
from PIL import Image, ImageTk
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.geometry("500x350")
window.title("Lefty Invoice Generator Form")
#icon_photo = customtkinter.CTkImage(light_image=Image.open("IMG_1718.PNG"))
#window.iconbitmap(True,Image.open("IMG_1718.PNG"))


photo1 =customtkinter.CTkImage(light_image=Image.open("Basketballcourt.png"),size=(1500,1000))

#bg_pic= customtkinter.CTkLabel(window,image=photo1).pack()
frame1 = customtkinter.CTkFrame(window,width=1000,height=500,fg_color="orange").place(relx=0.1,rely=0.1)
first_name_label = customtkinter.CTkLabel(frame1,text="First Name").pack()






window.mainloop()"""