import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import customtkinter as ctk
import csv
import random

# C U S T O M T K I N T E R
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

app = ctk.CTk()
app.title('Test CTk')
app.geometry('1200x800')
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

# D E S I G N
bg_color = app._apply_appearance_mode(ctk.ThemeManager.theme["CTkFrame"]["fg_color"])
text_color = app._apply_appearance_mode(ctk.ThemeManager.theme["CTkLabel"]["text_color"])
selected_color = app._apply_appearance_mode(ctk.ThemeManager.theme["CTkButton"]["fg_color"])

treestyle = ttk.Style()
treestyle.theme_use('default')
treestyle.configure("Treeview",background='silver',foreground='black',fieldbackground='silver',borderwidth=0,
                    font=('Arial',20),rowheight=50)
treestyle.configure("Treeview.Heading",background='gray',font=('Arial',22))
treestyle.map('Treeview',background=[('selected', '#0E4D92')],foreground=[('selected', 'white')])
app.bind("<<TreeviewSelect>>", lambda event: app.focus_set())

# F R A M E S
titlebar = ctk.CTkFrame(master=app,width=10000,height=100,corner_radius=0,fg_color='#260000')
titlebar.grid(row=0,column=0,columnspan=2,sticky='n')

frame1 = ctk.CTkFrame(master=app,corner_radius=0,fg_color='grey')
frame1.grid(padx=20,pady=120,row=0,column=0,sticky='nsew')
frame1.grid_rowconfigure(0, weight=1)
frame1.grid_columnconfigure(0, weight=1)

frame2 = ctk.CTkFrame(master=app,width=300,corner_radius=10,fg_color='#444444')
frame2.grid(padx=20,pady=120,row=0,column=1,sticky='nsew')

entry_frame = ctk.CTkFrame(master=app,width=10000,height=100,corner_radius=0,fg_color='#7A2021')
entry_frame.grid(row=0,column=0,columnspan=2,sticky='s')

# L A B E L S
title = ctk.CTkLabel(master=titlebar,font=('Wide Latin', 60),text='O R D E R T A K E R').place(relx=0.5,rely=0.5,anchor=tk.CENTER)
ordertext = ctk.CTkLabel(master=frame2,font=('Arial', 22),text='O R D E R').place(relx=0.5,y=20,anchor=tk.CENTER)
totaltext = ctk.CTkLabel(master=frame2,font=('Arial', 18,'bold'),text='T O T A L  C O S T :').place(relx=0.5,rely=0.82,anchor=tk.CENTER)
costtext = ctk.CTkTextbox(master=frame2,font=('Arial', 22,'bold'),text_color='black',height=60,width=250,fg_color='silver')
costtext.place(relx=0.5,rely=0.92,anchor=tk.CENTER)
costtext.configure(state='disabled')

# T R E E V I E W S
table = ttk.Treeview(frame1)
table.grid(row=0, column=0, sticky='nsew')
scroll = ttk.Scrollbar(frame1, orient="vertical", command=table.yview)
scroll.grid(row=0, column=1, sticky="ns")
table.configure(yscrollcommand=scroll.set)

order = ttk.Treeview(frame2)
order.grid(padx=15, pady=70,sticky='nsew')
order.config()
scroll2 = ttk.Scrollbar(frame2, orient="vertical", command=order.yview)
scroll2.grid(pady=70,row=0, column=1,sticky="ns")

# C O L U M N S
col1='NAME'
col2='TYPE'
col3='PRICE'
col4='AVAILABILITY'
cols = (col1,col2,col3,col4)
table['columns'] = cols
table.column('#0',width=0,stretch=NO)
table.column(col1,anchor=CENTER,width=300)
table.column(col2,anchor=CENTER)
table.column(col3,anchor=CENTER,width=100)
table.column(col4,anchor=CENTER)
for col in cols:
    table.heading(col,text=col)

initial_menu = [
    ("Pizza", "Meal", 12.99, "AVAILABLE"),
    ("Burger", "Meal", 8.99, "AVAILABLE"),
    ("Fries", "Appetizer", 3.99, "AVAILABLE"),
    ("Coke", "Beverage", 1.99, "AVAILABLE"),
    ("Cake", "Dessert", 4.99, "NOT AVAILABLE"),
    ("Tea", "Beverage", 1.49, "AVAILABLE"),
    ("Pasta", "Meal", 10.99, "NOT AVAILABLE"),
    ("Salad", "Appetizer", 5.99, "AVAILABLE"),
    ("Orange Juice", "Beverage", 2.99, "AVAILABLE"),
    ("Ice Cream", "Dessert", 3.49, "AVAILABLE"),
    ("Garlic Bread", "Appetizer", 2.49, "AVAILABLE"),
    ("Steak", "Meal", 15.99, "NOT AVAILABLE"),
    ("Fish and Chips", "Meal", 13.99, "AVAILABLE"),
    ("Water", "Beverage", 0.99, "AVAILABLE"),
    ("Brownie", "Dessert", 2.99, "AVAILABLE"),
    ("Spring Rolls", "Appetizer", 4.49, "NOT AVAILABLE"),
    ("Sushi", "Meal", 16.99, "AVAILABLE"),
    ("Lemonade", "Beverage", 2.49, "AVAILABLE"),
    ("Nachos", "Appetizer", 5.49, "AVAILABLE"),
    ("Cheesecake", "Dessert", 5.99, "AVAILABLE"),
]
    
for i, (name, type, price, avail) in enumerate(initial_menu):
    table.insert("", "end", iid=i, values=(name, type, price, avail))

umn1 = '#'
umn2 = 'NAME'
umn3 = 'PRICE'
umns = (umn1,umn2,umn3)
order['columns'] = umns
order.column('#0',width=0,stretch=NO)
order.column(umn1,anchor=CENTER,width=70)
order.column(umn2,anchor=CENTER,width=220)
order.column(umn3,anchor=CENTER,width=180)
for umn in umns:
    order.heading(umn,text=umn)

# I N P U T S
## f r a m e 1
name_box = ctk.CTkEntry(master=entry_frame,width=200,height=30,border_width=2,border_color='black',text_color='black',corner_radius=10,
                            placeholder_text='NAME',placeholder_text_color='black',fg_color='lightgrey')
name_box.place(rely=0.3,x=120,anchor=tk.CENTER)
type_var = ctk.StringVar(value='')
type_box = ctk.CTkComboBox(master=entry_frame,width=200,height=30,border_width=2,border_color='black',text_color='black',corner_radius=10,
                            values=['Appetizer','Beverage','Meal','Dessert'],state='readonly',variable=type_var,fg_color='lightgrey')
type_box.place(rely=0.3,x=340,anchor=tk.CENTER)
type_box.set("TYPE OF FOOD")
type_box.bind("<FocusIn>", lambda event: type_box.set('') if type_box.get() == "TYPE OF FOOD" else None)
type_box.bind("<FocusOut>", lambda event: type_box.set("TYPE OF FOOD") if type_box.get() == "" else None)
price_box = ctk.CTkEntry(master=entry_frame,width=200,height=30,border_width=2,border_color='black',text_color='black',corner_radius=10,
                            placeholder_text='PRICE',placeholder_text_color='black',fg_color='lightgrey')
price_box.place(rely=0.3,x=560,anchor=tk.CENTER)
avail_var = ctk.StringVar(value='')
avail_box = ctk.CTkComboBox(master=entry_frame,width=200,height=30,border_width=2,border_color='black',text_color='black',corner_radius=10,
                                values=['AVAILABLE','NOT AVAILABLE'],state='readonly',variable=avail_var,fg_color='lightgrey')
avail_box.place(rely=0.3,x=780,anchor=tk.CENTER)
avail_box.set("AVAILABILITY")
avail_box.bind("<FocusIn>", lambda event: avail_box.set('') if avail_box.get() == "AVAILABILITY" else None)
avail_box.bind("<FocusOut>", lambda event: avail_box.set("AVAILABILITY") if avail_box.get() == "" else None)

quantity_box = ctk.CTkEntry(master=frame2,width=250,height=30,border_width=2,border_color='black',text_color='black',corner_radius=10,
                            placeholder_text='QUANTITY',placeholder_text_color='black',fg_color='lightgrey')
quantity_box.place(relx=0.5,rely=0.67,anchor=tk.CENTER)

ulam_box = ctk.CTkEntry(master=entry_frame,width=250,height=30,border_width=2,border_color='black',text_color='black',corner_radius=10,
                            placeholder_text='KAHIT NA ANO',placeholder_text_color='grey',fg_color='lightgrey')
ulam_box.place(rely=0.7,x=1050,anchor=tk.CENTER)
    
## f r a m e 2


# D A T A B A S E
class Item():
    def __init__(self,name,type,price,avail):
        self.name = name
        self.type = type
        self.price = price
        self.avail = avail

class Menu():
    def __init__(self,init=False):
        self.itemlist = []
    
    def check_dupes(self,name,selectedname=''):
        for item in self.itemlist:
            if name == item.name and name != selectedname: return True
        return False
    
    def invalidinputs(self,type,price,avail):
        invalid = []
        try: num = float(price)
        except ValueError: num = price
        if not type in ('Appetizer','Beverage','Meal','Dessert'):invalid.append('TYPE')
        if not isinstance(num,(float)):invalid.append('PRICE')
        if not avail in ('AVAILABLE','NOT AVAILABLE'):invalid.append('AVAILABILTY')
        if invalid: return invalid 
        else: return False

    def get_menu(self):
        tupleList = []
        for item in self.itemlist:
            temptuple = (item.name,item.type,item.price,item.avail)
            tupleList.append(temptuple)
        return tupleList
    
    def add_item(self,name,type,price,avail):
        newItem = Item(name=name,type=type,price=price,avail=avail)
        self.itemlist.append(newItem)

    def delete_item(self, index):
        print(f"Ind`ex: {index}")
        print(f"Item list: {self.get_menu()}")
        self.itemlist.pop(int(index))

    def update_item(self,name,type,price,avail,index):
        updated = Item(name=name,type=type,price=price,avail=avail)
        self.itemlist[int(index)] = updated

    def csv_exp(self):
        with open('menu.csv', 'w') as exporter:
            for item in self.get_menu():
                exporter.write(f"{item[0]},{item[1]},{item[2]},{item[3]}\n")

    def csv_imp_file(self,filename=''):
        if filename == '': messagebox.showerror("UPDATE ITEM", "Please enter file name")
        else:
            with open(f'{filename}', mode='r', newline='') as file:
                self.itemlist=[]
                reader = csv.reader(file)
                for row in reader:
                    self.add_item(row[0],row[1],row[2],row[3])

class Order():
    def __init__(self,init=False):
        self.orderlist = []
    
    def get_total(self):
        total = 0
        for item in self.orderlist:
            total += (float(item[0])*float(item[2]))
        return total

    def find_nameindex(self,name):
        for row, sublist in enumerate(self.orderlist):
            if name in sublist:
                return row + 1
        return False
    
    def orderadd(self,num,name,price):
        templist = [int(num),name,price]
        index = self.find_nameindex(name)
        if index:
            self.orderlist[index-1][0] += int(num)       
        else: self.orderlist.append(templist)

    def orderremove(self,index):
        self.orderlist.pop(int(index))

    def change_num(self,index,num):
        self.orderlist[int(index)][0] = int(num)


# F U N C T I O N S
menu = Menu()
taker = Order()
for num in table.get_children():
    menu.add_item(table.item(num)['values'][0],table.item(num)['values'][1],table.item(num)['values'][2],table.item(num)['values'][3])

def update_entry_boxes(event):
    select= table.selection()
    if select:
        values = table.item(select[0], "values")
        name_box.delete(0, tk.END)
        name_box.insert(0, values[0])
        type_box.set(values[1])
        price_box.delete(0, tk.END)
        price_box.insert(0, values[2])
        avail_box.set(values[3])
table.bind("<<TreeviewSelect>>", update_entry_boxes)

def clear_table():
    for item in table.get_children():
        table.delete(item)

def refresh_table():
    clear_table()
    items = menu.get_menu()
    count = 0
    for item in items:
        table.insert(parent='',index='end',iid=count,text='',
                     values=(item[0],item[1],item[2],item[3]))
        count += 1

def add_f():
    invalid = menu.invalidinputs(type_box.get(),price_box.get(),avail_box.get())
    missing_fields = [field for field, box in [("NAME", name_box), ("TYPE", type_box), ("PRICE", price_box), ("AVAILABILITY", avail_box)] if box.get() in ['','TYPE OF FOOD','AVAILABILITY']]
    if missing_fields: messagebox.showerror("ADD ITEM", "Please enter the following fields:\n" + "\n".join(missing_fields))    
    elif menu.check_dupes(name_box.get()): messagebox.showerror("ADD ITEM", "NAME already exists")
    elif invalid: messagebox.showerror("ADD ITEM", "Invalid inputs:\n"+"\n".join(invalid))
    else:
        menu.add_item(name_box.get(),type_box.get(),price_box.get(),avail_box.get())
        refresh_table()
        name_box.delete(0,END)
        type_box.set('TYPE OF FOOD')
        price_box.delete(0,END)
        avail_box.set('AVAILABILITY')
        messagebox.showinfo("ADD ITEM", "Added new item")

def remove_f():
    tceles = (int(index) for index in table.selection())
    select = sorted(tceles,reverse=True)
    if len(select)>0:
        print(select)
        for index in select:
            menu.delete_item(index)
            refresh_table()
        messagebox.showinfo("REMOVE ITEM",f"Removed {len(select)} item/s")
    else:
        messagebox.showerror('REMOVE ITEM','Please select an item to delete.')

def update_f():
    select= table.selection()
    invalid = menu.invalidinputs(type_box.get(),price_box.get(),avail_box.get())
    missing_fields = [field for field, box in [("NAME", name_box), ("TYPE", type_box), ("PRICE", price_box), ("AVAILABILITY", avail_box)] if box.get() in ['','TYPE OF FOOD','AVAILABILITY']]
    if missing_fields: messagebox.showerror("UPDATE ITEM", "Please enter the following fields:\n" + "\n".join(missing_fields))    
    elif menu.check_dupes(name_box.get(),table.item(select[0])['values'][0]): messagebox.showerror("UPDATE ITEM", "NAME already exists")
    elif invalid: messagebox.showerror("UPDATE ITEM", "Invalid inputs:\n"+"\n".join(invalid))
    elif select:
        menu.update_item(name_box.get(),type_box.get(),price_box.get(),avail_box.get(),select[0])
        refresh_table()
        name_box.delete(0,END)
        type_box.set('TYPE OF FOOD')
        price_box.delete(0,END)
        avail_box.set('AVAILABILITY')
        messagebox.showinfo("UPDATED ITEM", "Successfully updated the item")

def export_csv():
    menu.csv_exp()
    refresh_table()
    messagebox.showinfo("EXPORT TO CSV", "Successfully exported into a CSV file")
    refresh_table()

def import_csv():
    filename = ctk.CTkInputDialog(title='IMPORT FROM CSV',text='ENTER FILENAME:')
    if filename: menu.csv_imp_file(filename.get_input()), refresh_table()
    else: messagebox.showerror("IMPORT FROM CSV", 'Please enter a filename')
    refresh_table()

def clear_order():
    for item in order.get_children():
        order.delete(item)

def take_order():
    clear_order()
    count = 0
    for item in taker.orderlist:
        order.insert(parent='',index='end',iid=count,text='',
                     values=(item[0],item[1],item[2]))
        count += 1

def total_payment():
    total = taker.get_total()
    costtext.configure(state='normal')
    costtext.delete("1.0", 'end')
    costtext.insert("1.0", f"{total}")
    costtext.configure(state='disabled')

def addtoorder():
    select = table.selection()
    values = table.item(select[0], "values")
    try: num = int(quantity_box.get())
    except ValueError: num = quantity_box.get()
    if values[3]=='NOT AVAILABLE': messagebox.showerror("ADD TO ORDER", "Item not available")
    elif not isinstance(num,int) or num == 0:messagebox.showerror("ADD TO ORDER", "Invalid Quantity!")
    elif select:
        taker.orderadd(quantity_box.get(),values[0],values[2])
    take_order()
    total_payment()
    quantity_box.delete(0,END)

def removeorder():
    tceles = (int(index) for index in order.selection())
    select = sorted(tceles,reverse=True)
    if len(select)>0:
        for index in select:
            taker.orderremove(index)
        take_order()
        total_payment()
        messagebox.showinfo("REMOVE ORDER",f"Removed {len(select)} item/s")
    else:
        messagebox.showerror('REMOVE ORDER','Please select an item to delete.')


def edit_quantity():
    select = order.selection()
    try: num = int(quantity_box.get())
    except ValueError: num = quantity_box.get()
    if not isinstance(num,int) or num == 0:messagebox.showerror("EDIT QUANTITY", "Invalid Quantity!")
    elif select:
        taker.change_num(select[0],int(quantity_box.get()))
        take_order()
        total_payment()
        quantity_box.delete(0,END)

def meronbakayong():
    ulam = ulam_box.get()
    karinderya = menu.get_menu()
    lyrics = ('WAITEERRRRR!!!!','ORDEERRRRR!!!!')
    if ulam:
        for listahan in karinderya:
            pagkain = listahan[0]
            if pagkain.lower() == ulam.lower():
                messagebox.showinfo("uwu", "Meron po <3")
                return
        secondvoice = ('WALA PO!', 'UBOS NA PO!','WALA!!!!')
        messagebox.showerror(f"{lyrics[random.randint(0, 1)]}", f"{secondvoice[random.randint(0, 2)]}")
    else: messagebox.showerror(f"{lyrics[random.randint(0, 1)]}", "WALA KA NILAGAY")


# B U T T O N S
add_button = ctk.CTkButton(master=entry_frame,text='ADD ITEM',
                           command=add_f).place(rely=0.7,x=90,anchor=tk.CENTER)
remove_button = ctk.CTkButton(master=entry_frame,text='REMOVE ITEM',
                              command=remove_f).place(rely=0.7,x=270,anchor=tk.CENTER)
update_button = ctk.CTkButton(master=entry_frame,text='UPDATE ITEM',
                              command=update_f).place(rely=0.7,x=450,anchor=tk.CENTER)
exportcsv_button = ctk.CTkButton(master=entry_frame,text='EXPORT TO CSV',
                              command=export_csv).place(rely=0.7,x=630,anchor=tk.CENTER)
importcsv_button = ctk.CTkButton(master=entry_frame,text='IMPORT CSV FILE',
                              command=import_csv).place(rely=0.7,x=810,anchor=tk.CENTER)

order_add = ctk.CTkButton(master=frame2,text='ADD',width=120,
                          command=addtoorder).place(rely=0.75,relx=0.27,anchor=tk.CENTER)
order_remove = ctk.CTkButton(master=frame2,text='REMOVE',width=120,
                          command=removeorder).place(rely=0.75,relx=0.73,anchor=tk.CENTER)
edit_num = ctk.CTkButton(master=frame2,text='EDIT',width=100,
                          command=edit_quantity).place(rely=0.67,relx=0.76,anchor=tk.CENTER)
search = ctk.CTkButton(master=entry_frame,text='MERON BA KAYONG...',font=('Arial',20),width=250,height=30,
                          command=meronbakayong).place(rely=0.3,x=1050,anchor=tk.CENTER)

app.mainloop()