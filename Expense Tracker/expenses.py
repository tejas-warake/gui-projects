from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkcalendar import DateEntry
from tkinter.ttk import Notebook
from tkinter import messagebox
# import sqlite3 as db ----->to be used later
import os

def recent_entries():
    d = date_entry.get()
    n = name_entry.get()
    t = title_entry.get()
    a = amount_entry.get()
    data = [d, n, t, a]
    data_view.insert('', 'end', values=data)

def clear_recents():
    data_view.delete(*data_view.get_children())

App = Tk()
App.title('Expense Tracker')
App.geometry('800x600')

#sections created
Section = Notebook(App)
S1 = Frame(App, width=500, height=500)
S2 = Frame(App, width=500, height=500)

Section.add(S1, text='Your Expenses')
Section.add(S2, text='Report')

Section.pack(fill=BOTH, expand=1)


# Completing the section one
# Dates label and entries
date_label = ttk.Label(S1, text='Date:', font=('Arial', 15))
date_label.grid(row=0, column=0, padx=6, pady=6, sticky='w')
date_entry = DateEntry(S1, width=25, background='grey', foreground='white', font=(None, 11))
date_entry.grid(row=0, column=1, padx=6, pady=6, sticky='w')

# Names label and entries
name_label = ttk.Label(S1, text='Name:', font=('Arial', 15))
name_label.grid(row=1, column=0, padx=6, pady=6, sticky='w')
name_entry = ttk.Entry(S1, textvariable=StringVar(), font=('calibri', 15))
name_entry.grid(row=1, column=1, padx=6, pady=6, sticky='w')

# Title label and entries
title_label = ttk.Label(S1, text='Title:', font=('Arial', 15))
title_label.grid(row=2, column=0, padx=6, pady=6, sticky='w')
title_entry = ttk.Entry(S1, textvariable=StringVar(), font=('calibri', 15))
title_entry.grid(row=2, column=1, padx=6, pady=6, sticky='w')

# Amount label and entries
amount_label = ttk.Label(S1, text='Amount:', font=('Arial', 15))
amount_label.grid(row=3, column=0, padx=6, pady=6, sticky='w')
amount_entry = ttk.Entry(S1, textvariable=StringVar(), font=('calibri', 15))
amount_entry.grid(row=3, column=1, padx=6, pady=6, sticky='w')

# Button attributes and command
# Add Button
add_button = ttk.Button(S1, text='Add Expense', command=recent_entries)
add_button.grid(row=4, column=1, padx=6, pady=6, ipadx=10, ipady=10, sticky='w')

label = ttk.Label(S1, text='Recent Expenses', font=('Arial', 18))
label.grid(row=5, column=1, padx=6, pady=6, sticky='w')

# Recents clear button
clear_button = ttk.Button(S1, text='Clear Recents', command=clear_recents)
clear_button.grid(row=4, column=2, padx=6, pady=6, ipadx=10, ipady=10, sticky='w')

# # Image Insertion code
img = ImageTk.PhotoImage(Image.open("E:\\Programming\\GUI development\\Expense Tracker\\static\\tracker.png"))
panel = Label(S1, image = img)
panel.grid(row=7, column=0, columnspan=3)


# Data view (Tree View)
data_list = ['Date', 'Name', 'Title', 'Amount']
data_view = ttk.Treeview(S1, column=data_list, show='headings', height=10)
for i in data_list:
    data_view.heading(i, text=i.title())
data_view.grid(row=6, column=0, padx=6, pady=6, sticky='w', columnspan=3)
App.mainloop()
