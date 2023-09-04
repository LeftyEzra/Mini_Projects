"""import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
window = customtkinter.CTk()
window.geometry("400x400")
window.title('Stop Clock')
window.resizable(False, False)

colors = ["red", "blue", "white"]
percent1 = customtkinter.IntVar()

bar = customtkinter.CTkProgressBar(window,height=30,orientation="vertical",progress_color=colors[0],
                                           width=10,
                                           mode="determinate", variable=percent1)
bar.place(relx=0.5,rely=0.5)
percent1.set(0)
bar['variable'] = percent1

percent2 = customtkinter.IntVar()
bar2 = customtkinter.CTkProgressBar(window,height=30,orientation="vertical",progress_color=colors[1],determinate_speed=5,
                                           width=100,
                                           mode="determinate", variable=percent2)
bar2.place(relx=0.2,rely=0.6)
percent2.set(0)
bar2['variable'] = percent2

percent3 = customtkinter.IntVar()
bar3 = customtkinter.CTkProgressBar(window,height=30,orientation="vertical",progress_color=colors[2],determinate_speed=15,
                                           width=100,
                                           mode="determinate", variable=percent3)
bar3.place(relx=0.2,rely=0.7)
percent3.set(0)

current_bar = 0
def increase_bar():
    global current_bar
    current_bar +=1
    if current_bar == 1:
        #percent1.set(percent1.get()+20)
        bar.start()
        # check the value of the first progress bar every 10 milliseconds and stop it when it is full
        window.after(10, check_bar1)
    elif current_bar == 2:
        #percent2.set(percent1.get()+20)
        bar2.start()
        # check the value of the second progress bar every 10 milliseconds and stop it when it is full
        window.after(10, check_bar2)
    elif current_bar == 3:
        #percent3.set(percent3.get()+20)
        bar3.start()
        # check the value of the third progress bar every 10 milliseconds and stop it when it is full
        window.after(10, check_bar3)

# define a function to check the value of the first progress bar and stop it when it is full
def check_bar1():
    if percent1.get() >= 100:
        bar.stop()
    else:
        # repeat the check after 10 milliseconds
        window.after(10, check_bar1)

# define a function to check the value of the second progress bar and stop it when it is full
def check_bar2():
    if percent2.get() >= 100:
        bar2.stop()
    else:
        # repeat the check after 10 milliseconds
        window.after(10, check_bar2)

# define a function to check the value of the third progress bar and stop it when it is full
def check_bar3():
    if percent3.get() >= 100:
        bar3.stop()
    else:
        # repeat the check after 10 milliseconds
        window.after(10, check_bar3)


open_button = customtkinter.CTkButton(window, command=increase_bar)
open_button.pack()


window.mainloop()"""
from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
import openpyxl
from tkinter import messagebox

import customtkinter


#customtkinter.set_appearance_mode("dark")
#customtkinter.set_default_color_theme("#0A0B0C")


window = customtkinter.CTk()
window.geometry("1000x500")
window.title('Stop Clock')
window.config(bg="#0A0B0C")

font1 = ("Arial", 20,'bold')
font2 = ("Arial", 18,'bold')
font3 = ("Arial", 33,'bold')


#Creating a animated class frame to contain all the entry widgets
class SlidePanel(customtkinter.CTkFrame):
    def __init__ (self,parent,start_position,end_position,):
        super().__init__(master=parent,fg_color="#FB7C00",width=880,height=480)

        #general attributes
        self.start_position = start_position + 0.01
        self.end_position   = end_position   - 0.01
        #self.width          = abs(start_position - end_position)

        #animation logic
        self.pos = self.start_position
        self.in_start_position = True

        #layout
        self.place(relx=0.1,rely=self.start_position)


    def animate(self):
        if self.in_start_position:
            self.animate_upward()
        else:
            self.animate_downwards()
    def animate_upward(self):
        if self.pos > self.end_position:
            self.pos -= 0.008
            self.place(rely=self.pos, relx=0.1)
            self.after(0,self.animate_upward)
        else:
            self.in_start_position = False

    def animate_downwards(self):
        if self.pos < self.start_position:
            self.pos += 0.008
            self.place(rely=self.pos, relx=0.1)
            self.after(1,self.animate_downwards)
        else:
            self.in_start_position = True

#                                  1.0,0.6
animated_panel1 = SlidePanel(window,1.0,0.02)

#font1 = ("Arial", 30,'bold')
#button to call the treeview from its resting state
slide_frame = customtkinter.CTkButton(window,text="treeview",command=animated_panel1.animate)
slide_frame.place(relx=0.02,rely=0.85)


#Teams Entry and label widgets
team1_label_stat = customtkinter.CTkLabel(animated_panel1,height=30,
                                          text="                          Team 1 Stats",font=font1)
team1_label_stat.place(relx=0.01,rely=0.01)

team_name_label = customtkinter.CTkLabel(animated_panel1,text="Team name").place(relx=0.01,rely=0.07)

team_name_entry = customtkinter.CTkEntry(animated_panel1,width=140,height=30,corner_radius=5)
team_name_entry.delete(0, "end")
team_name_entry.insert(0, "Team name")

team_name_entry.bind("<FocusIn>", lambda d: team_name_entry.delete('0', "end"))
team_name_entry.place(relx=0.01,rely=0.12)


team_3ptAttempts_label = customtkinter.CTkLabel(animated_panel1,text="3points Attempts").place(relx=0.01,rely=0.2)

team_3ptsAttempts_entry = customtkinter.CTkEntry(animated_panel1,width=140,height=30,corner_radius=5)
team_3ptsAttempts_entry.delete(0, "end")
team_3ptsAttempts_entry.insert(0, "0")

team_3ptsAttempts_entry.bind("<FocusIn>", lambda e: team_3ptsAttempts_entry.delete('0', "end"))
team_3ptsAttempts_entry.place(relx=0.01,rely=0.25)

team_3ptMade_label = customtkinter.CTkLabel(animated_panel1,text="3points Made").place(relx=0.01,rely=0.33)

team_3ptsMade_entry = customtkinter.CTkEntry(animated_panel1,width=140,height=30,corner_radius=5)
team_3ptsMade_entry.delete(0, "end")
team_3ptsMade_entry.insert(0, "0")

team_3ptsMade_entry.bind("<FocusIn>", lambda f: team_3ptsAttempts_entry.delete('0', "end"))
team_3ptsMade_entry.place(relx=0.01,rely=0.38)

team_2ptsAttempts_label = customtkinter.CTkLabel(animated_panel1,text="2points Attempts").place(relx=0.2,rely=0.07)

team_2ptsAttempts_entry = customtkinter.CTkEntry(animated_panel1,width=140,height=30,corner_radius=5)

team_2ptsAttempts_entry.delete(0, "end")
team_2ptsAttempts_entry.insert(0, "0")

team_2ptsAttempts_entry.bind("<FocusIn>", lambda g: team_2ptsAttempts_entry.delete('0', "end"))
team_2ptsAttempts_entry.place(relx=0.2,rely=0.12)

team_2ptMade_label = customtkinter.CTkLabel(animated_panel1,text="2points Made").place(relx=0.2,rely=0.2)

team_2ptsMade_entry = customtkinter.CTkEntry(animated_panel1,width=140,height=30,corner_radius=5)
team_2ptsMade_entry.delete(0, "end")
team_2ptsMade_entry.insert(0, "0")

team_2ptsMade_entry.bind("<FocusIn>", lambda h: team_2ptsMade_entry.delete('0', "end"))
team_2ptsMade_entry.place(relx=0.2,rely=0.25)


team_ftAttempts_label = customtkinter.CTkLabel(animated_panel1,text="Freethrows Attempts").place(relx=0.51,rely=0.07)

team_ftAttempts_entry = customtkinter.CTkEntry(animated_panel1,width=140,height=30,corner_radius=5)
team_ftAttempts_entry.delete(0, "end")
team_ftAttempts_entry.insert(0, "0")

team_ftAttempts_entry.bind("<FocusIn>", lambda i: team_ftAttempts_entry.delete('0', "end"))
team_ftAttempts_entry.place(relx=0.51,rely=0.12)

team_ftMade_label = customtkinter.CTkLabel(animated_panel1,text="Freethrow Made").place(relx=0.51,rely=0.2)

team_ftMade_entry = customtkinter.CTkEntry(animated_panel1,width=140,height=30,corner_radius=5)

team_ftMade_entry.delete(0, "end")
team_ftMade_entry.insert(0, "0")

team_ftMade_entry.bind("<FocusIn>", lambda j: team_ftMade_entry.delete('0', "end"))
team_ftMade_entry.place(relx=0.51,rely=0.25)

team_offensive_rebound_label = customtkinter.CTkLabel(animated_panel1,text="Offensive Rebounds").place(relx=0.7,rely=0.07)

team_off_rebounds_entry = customtkinter.CTkEntry(animated_panel1,width=140,height=30,corner_radius=5)
team_off_rebounds_entry.delete(0, "end")
team_off_rebounds_entry.insert(0, "0")

team_off_rebounds_entry.bind("<FocusIn>", lambda k: team_off_rebounds_entry.delete('0', "end"))
team_off_rebounds_entry.place(relx=0.7,rely=0.12)

team_defensive_rebounds_label = customtkinter.CTkLabel(animated_panel1,text="Defensive Rebounds").place(relx=0.7,rely=0.2)

team_def_rebounds_entry = customtkinter.CTkEntry(animated_panel1,width=140,height=30,corner_radius=5)
team_def_rebounds_entry.delete(0, "end")
team_def_rebounds_entry.insert(0, "0")

team_def_rebounds_entry.bind("<FocusIn>", lambda l: team_def_rebounds_entry.delete('0', "end"))
team_def_rebounds_entry.place(relx=0.7,rely=0.25)

team_block_label = customtkinter.CTkLabel(animated_panel1,text="Blocks").place(relx=0.51,rely=0.33)

team_block_entry = customtkinter.CTkEntry(animated_panel1,width=140,height=30,corner_radius=5)
team_block_entry.delete(0, "end")
team_block_entry.insert(0, "0")

team_block_entry.bind("<FocusIn>", lambda f: team_block_entry.delete('0', "end"))
team_block_entry.place(relx=0.51,rely=0.38)



#Line to divide the animated panel into 2
baseline_div = customtkinter.CTkBaseClass(animated_panel1,height=300,bg_color="black",width=5)
baseline_div.place(relx=0.5)


######################################################################################################
### Team1 entry and lab
###Select items to update
def display_record():
    #Delete all the entry records
    team_name_entry.delete(0, "end")
    team_3ptsAttempts_entry.delete(0, "end")
    team_3ptsMade_entry.delete(0, "end")
    team_2ptsAttempts_entry.delete(0, "end")
    team_2ptsMade_entry.delete(0, "end")
    team_ftAttempts_entry.delete(0, "end")
    team_ftMade_entry.delete(0, "end")
    team_off_rebounds_entry.delete(0, "end")
    team_def_rebounds_entry.delete(0, "end")
    team_block_entry.delete(0, "end")



    #variable to select the row in the treeview
    selected_item = tree.focus()

    new_update = tree.item(selected_item,'values')
    team_name_entry.insert(0, new_update[0])
    team_3ptsAttempts_entry.insert(0, new_update[1])
    team_3ptsMade_entry.insert(0, new_update[2])
    team_2ptsAttempts_entry.insert(0, new_update[3])
    team_2ptsMade_entry.insert(0, new_update[4])
    team_ftAttempts_entry.insert(0, new_update[5])
    team_ftMade_entry.insert(0, new_update[6])
    team_off_rebounds_entry.insert(0, new_update[7])
    team_def_rebounds_entry.insert(0, new_update[8])
    team_block_entry.insert(0, new_update[9])
#
#Update the selected items in the treeview
def update_record():

    #The focus point
    selected_item = tree.focus()
    #row_index = int(tree.index(selected_item))
    tree.item(selected_item, text="",values=(team_name_entry.get(),team_3ptsAttempts_entry.get(),team_3ptsMade_entry.get(),
                                             team_2ptsAttempts_entry.get(),team_2ptsMade_entry.get(),team_ftAttempts_entry.get(),
                                             team_ftMade_entry.get(),team_off_rebounds_entry.get(),team_def_rebounds_entry.get(),
                                             team_block_entry.get()))

    #after updating clear the entry boxes
    team_name_entry.delete(0, "end")
    team_3ptsAttempts_entry.delete(0, "end")
    team_3ptsMade_entry.delete(0, "end")
    team_2ptsAttempts_entry.delete(0, "end")
    team_2ptsMade_entry.delete(0, "end")
    team_ftAttempts_entry.delete(0, "end")
    team_ftMade_entry.delete(0, "end")
    team_off_rebounds_entry.delete(0, "end")
    team_def_rebounds_entry.delete(0, "end")
    team_block_entry.delete(0, "end")

    messagebox.showinfo("Success", "Datas updated successfully.")


#Clear selected items from treeview
def clear():
    x = tree.selection()
    for record in x:
        tree.delete(record)



#Add items to treeview
def add_items():

    ###Variable to store the entry datas
    team_name = str(team_name_entry.get())
    pt3_attempts = int(team_3ptsAttempts_entry.get())
    pt3_made = int(team_3ptsMade_entry.get())
    pt2_attempts = int(team_2ptsAttempts_entry.get())
    pt2_made = int(team_2ptsMade_entry.get())
    ft_attempts = int(team_ftAttempts_entry.get())
    ft_made = int(team_ftMade_entry.get())
    off_rebound = int(team_off_rebounds_entry.get())
    def_rebound = int(team_def_rebounds_entry.get())
    blocks = int(team_block_entry.get())

    ### This is to insert all the input datas into the treview rows
    row_values = [team_name,pt3_attempts, pt3_made, pt2_attempts,pt2_made,ft_attempts,ft_made,off_rebound,def_rebound,blocks]
    tree.insert('', "end", values=row_values)

    #for loop function is to get all the widgets that are type entry and delete them
    for widget in animated_panel1.winfo_children():
        if isinstance(widget, customtkinter.CTkEntry):
            widget.delete(0,"end")

    ### Save data to Excel
    games_filepath = "team_datas.xlsx"
    if not os.path.exists(games_filepath):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        heading = ["Team names","3pts_Attempts", "3pts_Made", "2pts_Attempts","2pts_Made",
                    "FT_Attempts","FT_Made","Off_rebounds","Def_rebounds","Blocks","Team2",]

        sheet.append(heading)
        workbook.save(games_filepath)

    workbook = openpyxl.load_workbook(games_filepath)
    sheet = workbook.active
    sheet.append([team_name,pt3_attempts, pt3_made, pt2_attempts,pt2_made,ft_attempts,ft_made,off_rebound,def_rebound,blocks])
    workbook.save(games_filepath)
    messagebox.showinfo("Success","Datas saved successfully.")


###buton widgets to call the trreview created functions
add_button_item = customtkinter.CTkButton(window,text="Add Item(s)",command=add_items).place(relx=0.01,rely=0.3)
del_button = customtkinter.CTkButton(window,text="Clear",command=clear).place(relx=0.01,rely=0.45)
update_button = customtkinter.CTkButton(window,text="update",command=update_record).place(relx=0.01,rely=0.55)
select_button = customtkinter.CTkButton(window,text="select",command=display_record).place(relx=0.01,rely=0.65)


###styling the treeview
style = ttk.Style(window)
style.theme_use("clam")
style.configure("Treeview.Heading",font=("Arial",12,"bold"),foreground="blue",background="orange")
style.configure('Treeview',font=("Arial",15),foreground="#00FF2F",background="#000080",fieldbackground='#480062')
style.map('Treeview',background=[('selected', '#AA04A7')])


###Column title for the treeview
cols=("Team names","3pts Attempts", "3pts Made", "2pts Attempts","2pts Made","FT Attempts","FT Made","Off_rebounds","Def_rebounds","Blocks")

tree = ttk.Treeview(animated_panel1,height=15,columns=cols)
#tree["columns"] = ("3points Attempts","Made","Missed")

tree.column("#0",width=0,stretch=tk.NO)
tree.column("Team names",width=150,anchor=W,stretch=tk.YES,)
tree.column("3pts Attempts",width=120,anchor=W,stretch=True,)
tree.column("3pts Made",width=150,anchor=W,stretch=tk.YES,)
tree.column("2pts Attempts",width=130,anchor=W,stretch=True,)
tree.column("2pts Made",width=120,anchor=W,stretch=tk.YES,)
tree.column("FT Attempts",width=120,anchor=W,stretch=True,)
tree.column("FT Made",width=100,anchor=W,stretch=tk.YES,)
tree.column("Off_rebounds",width=150,anchor=W,stretch=True,)
tree.column("Def_rebounds",width=150,anchor=W,stretch=tk.YES,)
tree.column("Blocks",width=100,anchor=W,stretch=False,)


tree.heading("#0",text="")
tree.heading("Team names", text="Team names")
tree.heading("3pts Attempts", text="3pts Attempts",anchor=W)
tree.heading("3pts Made", text="3pts Made")
tree.heading("2pts Attempts", text="2pts Attempts")
tree.heading("2pts Made", text="2pts Made")
tree.heading("FT Attempts", text="FT Attempts",anchor=W)
tree.heading("FT Made", text="FT Made")
tree.heading("Off_rebounds", text="Off_rebounds")
tree.heading("Def_rebounds", text="Def_rebounds")
tree.heading("Blocks",text="Blocks")





tree.place(relx=0.001,rely=0.5)
#tree.bind('<ButtonRelease>', display_record)
tree_scrollbar = customtkinter.CTkScrollbar(animated_panel1,orientation="vertical",command=tree.yview,width=20,
                                            height=220,fg_color="transparent",bg_color="blue")
#tree.configure(xscrollcommand=treeview_scrollbar.set)
tree.configure(yscrollcommand=tree_scrollbar.set)
tree_scrollbar.place(relx=1,rely=0.5,anchor="ne")






window.mainloop()