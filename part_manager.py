from tkinter import *
from tkinter import messagebox
from db import  Database
import pylint

db = Database('store.db')

def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)

def add_item():
    if product_text.get() == '' or customer_text.get() == '' or part_text.get() == '' or price_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(product_text.get(), customer_text.get(), part_text.get(), price_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (product_text.get(), customer_text.get(), part_text.get(), price_text.get()))
    clear_text()
    populate_list()

def select_item(Event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)
        print(selected_item)

        product_entry.delete(0, END)
        product_entry.insert(END, selected_item[1])

        customer_entry.delete(0, END)
        customer_entry.insert(END, selected_item[2])

        part_entry.delete(0, END)
        part_entry.insert(END, selected_item[3])

        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass

def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def update_item():
    db.update(selected_item[0],product_text.get(), customer_text.get(), part_text.get(), price_text.get())
    populate_list()

def clear_text():
    product_entry.delete(0, END)
    customer_entry.delete(0, END)
    part_entry.delete(0, END)
    price_entry.delete(0, END)

# create window
app = Tk()

#product
product_text = StringVar()
product_label = Label(app, text = 'Product', font = ('bold', 10), pady = 20)
product_label.grid(row=0, column=0, sticky=W)
product_entry = Entry(app, textvariable=product_text)
product_entry.grid(row=0, column=1)

#customer
customer_text = StringVar()
customer_label = Label(app, text = 'customer Name', font = ('bold', 10), pady = 20)
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

#part
part_text = StringVar()
part_label = Label(app, text = 'Part Name', font = ('bold', 10), pady = 20)
part_label.grid(row=1, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=1, column=1)

#price
price_text = StringVar()
price_label = Label(app, text = 'Price', font = ('bold', 10), pady = 20)
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)

#Parts List
parts_list = Listbox(app, height=8, width=50, border=0)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

#Scrollbar
Scrollbar = Scrollbar(app)
Scrollbar.grid(row=3, column=3)

#set scrollbar
parts_list.configure(yscrollcommand=Scrollbar.set)
Scrollbar.config(command=parts_list.yview)

# Bind select
parts_list.bind('<<ListboxSelect>>', select_item)

#Buttons
add_btn = Button(app, text='Add Product', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove Product', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update Product', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)


app.title('Store Manager')
app.geometry('700x350')

#populate
populate_list()

#start:
app.mainloop()