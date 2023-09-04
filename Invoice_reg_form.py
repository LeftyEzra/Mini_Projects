import customtkinter
from tkinter import ttk
from docxtpl import DocxTemplate
#from docx.shared import Inches
import datetime
import time as t
from PIL import Image
#from random import randint, choice
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.title("Lefty Invoice Generator Form")
icon_photo = customtkinter.CTkImage(light_image=Image.open("basketcourt.png"))


def clear_item():
    combobox1.set('0')
    combobox2.set("0.0")
    description_entry.delete(0,len(description_entry.get()))
x = t.asctime()
def generate_invoice():
    document= DocxTemplate("Lefty_Ezra_template.docx")
    name = firstname_entry.get() + " " + lastname_entry.get()
    phone =phone_label_entry.get()
    subtotal = sum(item[3] for item in invoice_list)
    salestax = 0.1
    total = subtotal*(1-salestax)

    document.render({"Company":"Tinazze-foot","telephone":"0703########",
                     "address":"10/11,Old olowora road reality plaza, isheri magodo phase1, Lagos.",
                     "name":name,"phone":phone,"time":x,
                     "invoice_list":invoice_list,
                     "subtotal":subtotal,
                     "salestax":str(salestax*100)+"%",
                     "total":total,})
    document_name ="generated_invoice" + name + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")+".docx"
    document.save(document_name)


def new_invoice():
    firstname_entry.delete(0,len(firstname_entry.get()))
    lastname_entry.delete(0,len(lastname_entry.get()))
    phone_label_entry.delete(0,len(phone_label_entry.get()))
    clear_item()
    treeview.delete(*treeview.get_children())

    invoice_list.clear()

invoice_list =[]
def add_item():
    qty = int_entry1.get()
    desc = (descriptn_entry.get())
    price = price_entry.get()
    line_total = qty * price
    invoice_items = [qty,desc,price,line_total]
    treeview.insert('',0, values=invoice_items)
    clear_item()

    invoice_list.append(invoice_items)

photo1 =customtkinter.CTkImage(light_image=Image.open("basketcourt.png"),size=(1500,1000))
#create frame for widgets
frame = customtkinter.CTkFrame(window,width=1000,height=600,corner_radius=5,fg_color='#475f2f',)
frame.place(relx=0.5,rely=0.5,anchor='center')

#Creating entry labels
firstname_label = customtkinter.CTkLabel(frame, text="First Name", font=("Roboto",24),compound='top',text_color="#ff0")
firstname_label.place(x=90,y=40)

firstname_entry = customtkinter.CTkEntry(frame,width=180,height=28)
firstname_entry.place(x=90,y=70)

lastname_label = customtkinter.CTkLabel(frame, text="Last Name", font=("Roboto",24),compound='top',text_color="#ff0")
lastname_label.place(x=400,y=40)

lastname_entry = customtkinter.CTkEntry(frame,width=180,height=28)
lastname_entry.place(x=400,y=70)

phone_label = customtkinter.CTkLabel(frame, text="Phone", font=("Roboto",24),compound='top',text_color="#ff0")
phone_label.place(x=700,y=40)

phone_label_entry = customtkinter.CTkEntry(frame,width=180,height=28)
phone_label_entry.place(x=700,y=70)


#Creating entry labels
quantity_label = customtkinter.CTkLabel(frame, text="Quantity", font=("Ghothic",24),compound='top',text_color="#ff0")
quantity_label.place(x=400,y=120)

int_entry1 = customtkinter.IntVar()
combobox1 = customtkinter.CTkComboBox(frame,width=180,height=28,variable=int_entry1,
                                      dropdown_text_color="cyan",
                                      values=['0','1','2','3','4','5'],state='readonly')
combobox1.place(x=400,y=150)
combobox1.set('0')


description_label = customtkinter.CTkLabel(frame, text=" Description", font=("Roboto",24),compound='top',text_color="#ff0")
description_label.place(x=90,y=120)

descriptn_entry = customtkinter.StringVar()
description_entry = customtkinter.CTkEntry(frame,width=180,height=28,textvariable=descriptn_entry)
description_entry.place(x=90,y=150)

unitprice_label = customtkinter.CTkLabel(frame, text="Unit Price", font=("Roboto",24),compound='top',text_color="#ff0")
unitprice_label.place(x=700,y=120)

price_entry = customtkinter.DoubleVar()
combobox2 = customtkinter.CTkComboBox(frame,width=180,height=28,variable=price_entry,
                                      dropdown_text_color="cyan",
                                      values=['0.5','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0'],state='readonly')
combobox2.place(x=700,y=150)
combobox2.set('0')

add_button_item = customtkinter.CTkButton(frame,text="Add Item(s)",command=add_item).place(x=720,y=190)
columns= ("qty","desc","price","total")

#style = ttk.Style()
#style.configure("Treeview.Heading",font=(None,20))
style = ttk.Style(window)
style.theme_use("clam")
style.configure("Treeview.Heading",font=("Arial",20))
style.configure('Treeview',font=("Arial",24,),foreground="#fff",background="#0A0B0C",fieldbackground='#1B1B21')
style.map('Treeview',background=[('selected', '#AA04A7')])

treeview = ttk.Treeview(frame,columns=columns,show='headings')
treeview.column('desc',width=150)
treeview.heading('desc',text=('Description'),anchor='w',)
treeview.heading('qty',text='Quantity',anchor='w')
treeview.heading('price',text='Price',anchor='w')
treeview.heading('total',text='Total',anchor='w')

treeview.place(x=90,y=355,height=450,width=1300)

saveinvoice_button =  customtkinter.CTkButton(frame,text=("Generate  Invioce"),text_color="white",command=generate_invoice,
                                              fg_color="green",width=300,
                                              font=("roman",15,"bold"))
saveinvoice_button.place(x=90,y=550)

newinvoice_button =  customtkinter.CTkButton(frame,text=("New  Invioce"),text_color="white",command=new_invoice,
                                              fg_color="green",width=300,
                                              font=("roman",15,"bold"))
newinvoice_button.place(x=600,y=550)



window.mainloop()