
import ttkbootstrap


window = ttkbootstrap.Window(themename="cyborg")
window.geometry("500x500")
window.title('lefty')
window.resizable(True,True)
#icon = tk.PhotoImage(file="")
#window.iconphoto(False, icon)

#setting a global variable
value = 0
paused = True

#initializing the meter widget
meter= ttkbootstrap.Meter(window ,amounttotal=24 ,meterthickness=10 ,interactive=True,textfont=(None,120),
                               stripethickness=20 ,metertype="break",metersize=300,bootstyle="success",)
meter.place(relx=0.02 ,rely=0.01)





#Function and logic  to countdown meter
def meter_count():
    global value,paused

    meter['amountused'] = value # the widget argument
    if value > 0 and not paused:
        value -= 1
        window.update()
        window.after(700,meter_count)


def pause(): # pause function
    global paused
    paused = not paused # toggle pause state
    if paused:
        pause_button['text'] = "resume" # change button text
    else:
        pause_button['text'] = "pause"
        meter_count() # resume countdown


def add_seconds():
    global value
    meter['amountused'] = value
    value += 1
    #window.update()


meter1= ttkbootstrap.Button(window,text="meter",command=meter_count )
meter1.place(relx=0.5 ,rely=0.7,height=50,width=100)

meter2= ttkbootstrap.Button(window,text="+add", command=add_seconds )
meter2.place(relx=0.5 ,rely=0.85,height=50,width=100)

pause_button= ttkbootstrap.Button(window,text="start", command=pause )
pause_button.place(relx=0.7 ,rely=0.85,height=50,width=100)
window.mainloop()



