import json
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from database import Database
from traveller import Traveller


class TravellerForm:
    def __init__(self):
        self.db = Database('json/traveller.json')
        self.e1 = StringVar()
        self.e2 = StringVar()
        self.e3 = StringVar()
        self.e4 = StringVar()
        self.e5 = StringVar()
        self.e6 = StringVar()
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=10)
        cols = ('id', 'name', 'address', 'date_of_birth', 'emergency_contact', 'government_id')
        self.tree = ttk.Treeview(self.frm, columns=cols, show='headings')
        self.show_traveller_form()

    def add(self):
        id = self.e1.get()
        name = self.e2.get()
        address = self.e3.get()
        date_of_birth = self.e4.get()
        emergency_contact = self.e5.get()
        government_id = self.e6.get()
        traveller = Traveller(id, name, address, date_of_birth, emergency_contact, government_id)
        traveller.save_traveller()
        messagebox.showinfo("information", "Traveller inserted successfully...")
        self.clear_fields()

    def update(self):
        id = self.e1.get()
        name = self.e2.get()
        address = self.e3.get()
        date_of_birth = self.e4.get()
        emergency_contact = self.e5.get()
        government_id = self.e6.get()
        traveller = Traveller(id, name, address, date_of_birth, emergency_contact, government_id)
        traveller.update_traveller()
        messagebox.showinfo("Information", "Record Updated successfully...")
        self.clear_fields()

    def delete(self):
        id = self.e1.get()
        name = self.e2.get()
        address = self.e3.get()
        date_of_birth = self.e4.get()
        emergency_contact = self.e5.get()
        government_id = self.e6.get()
        traveller = Traveller(id, name, address, date_of_birth, emergency_contact, government_id)
        traveller.delete_traveller()
        messagebox.showinfo("information", "Record Deleted successfully...")
        self.clear_fields()

    def clear_fields(self):
        self.e1.set("")
        self.e2.set("")
        self.e3.set("")
        self.e4.set("")
        self.e5.set("")
        self.e6.set("")

    def get_value(self, event):
        row_id = self.tree.selection()[0]
        select = self.tree.set(row_id)
        self.e1.set(select['id'])
        self.e2.set(select['name'])
        self.e3.set(select['address'])
        self.e4.set(select['date_of_birth'])
        self.e5.set(select['emergency_contact'])
        self.e6.set(select['government_id'])

    def show(self):
        records = self.db.load_data()
        # Clear the treeview list items
        for item in self.tree.get_children():
            self.tree.delete(item)
        # load data
        for x in records:
            self.tree.insert("", "end", values=(
                x['id'],
                x['name'],
                x['address'],
                x['date_of_birth'],
                x['emergency_contact'],
                x['government_id']
            ))

    def show_traveller_form(self):
        # root.state("zoomed")
        self.root.geometry("1225x500")
        self.root.title("Solent - Travellers")
        self.frm.grid()
        ttk.Label(self.frm, background="green", text="Solent Travellers", font=("Arial", 25), anchor="center", padding=5,
                  foreground="white").grid(column=0, row=0, columnspan=10, sticky='nsew')
        ttk.Label(self.frm, text="ID: ", padding=4).grid(column=0, row=2, sticky='e')
        Entry(self.frm, textvariable=self.e1, width=5).grid(row=2, column=1, sticky='w')
        ttk.Label(self.frm, text="Name: ", padding=4).grid(column=0, row=3, sticky='e')
        Entry(self.frm, textvariable=self.e2, width=50).grid(row=3, column=1, sticky='w')
        ttk.Label(self.frm, text="Address: ", padding=4).grid(column=0, row=4, sticky='e')
        Entry(self.frm, textvariable=self.e3, width=50).grid(row=4, column=1, sticky='w')
        ttk.Label(self.frm, text="Date of Birth: ", padding=4).grid(column=0, row=5, sticky='e')
        Entry(self.frm, textvariable=self.e4).grid(row=5, column=1, sticky='w')
        ttk.Label(self.frm, text="Emergency Contact: ", padding=4).grid(column=0, row=6, sticky='e')
        Entry(self.frm, textvariable=self.e5).grid(row=6, column=1, sticky='w')
        ttk.Label(self.frm, text="Government ID: ", padding=4).grid(column=0, row=7, sticky='e')
        Entry(self.frm, textvariable=self.e6).grid(row=7, column=1, sticky='w')
        self.tree.heading('id', text='ID')
        self.tree.heading('name', text='Name')
        self.tree.heading('address', text='Address')
        self.tree.heading('date_of_birth', text='Date of Birth')
        self.tree.heading('emergency_contact', text='Emergency Contact')
        self.tree.heading('government_id', text='Government ID')
        self.tree.grid(row=8, column=0, pady=20, columnspan=7, sticky='e')
        self.show()
        self.tree.bind('<<TreeviewSelect>>', self.get_value)
        Button(self.root, text="Add", command=self.add, height=1, width=13).place(x=480, y=200)
        Button(self.root, text="update", command=self.update, height=1, width=13).place(x=590, y=200)
        Button(self.root, text="Delete", command=self.delete, height=1, width=13).place(x=700, y=200)
        Button(self.root, text="Refresh", command=self.show, height=1, width=13).place(x=810, y=200)
        self.root.mainloop()