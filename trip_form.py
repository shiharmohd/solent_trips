import json
from tkinter import ttk, messagebox
from tkinter import *
from database import Database
from trip import Trip


class TripForm:
    def __init__(self):
        self.db = Database('json/trip.json')
        self.tfroot = Tk()
        self.frm = ttk.Frame(self.tfroot, padding=10)
        cols = ('name', 'start_date', 'travellers', 'duration', 'coordinator', 'contact')
        self.tree = ttk.Treeview(self.frm, columns=cols, show='headings')
        self.e1 = StringVar()
        self.e2 = StringVar()
        self.e3 = StringVar()
        self.e4 = StringVar()
        self.e5 = StringVar()
        self.e6 = StringVar()
        self.show_form()

    def add(self):
        name = self.e1.get()
        start_date = self.e2.get()
        travellers = self.e3.get()
        duration = self.e4.get()
        coordinator = self.e5.get()
        contact = self.e6.get()
        tp = Trip(name, start_date, travellers, duration, coordinator, contact)
        tp.save_trip()
        messagebox.showinfo("information", "Trip inserted successfully...")
        self.clear_fields()

    def update(self):
        name = self.e1.get()
        start_date = self.e2.get()
        travellers = self.e3.get()
        duration = self.e4.get()
        coordinator = self.e5.get()
        contact = self.e6.get()
        tp = Trip(name, start_date, travellers, duration, coordinator, contact)
        tp.update_trip()
        messagebox.showinfo("information", "Record Updated successfully...")
        self.clear_fields()

    def delete(self):
        name = self.e1.get()
        start_date = self.e2.get()
        travellers = self.e3.get()
        duration = self.e4.get()
        coordinator = self.e5.get()
        contact = self.e6.get()
        tp = Trip(name, start_date, travellers, duration, coordinator, contact)
        tp.delete_trip()
        messagebox.showinfo("information", "Record Deleted successfully...")
        self.clear_fields()

    def clear_fields(self):
        self.e1.set("")
        self.e2.set("")
        self.e3.set("")
        self.e4.set("")
        self.e5.set("")
        self.e6.set("")

    def get_value(self,event):
        if len(self.tree.get_children()) > 0:
            row_id = self.tree.selection()[0]
            select = self.tree.set(row_id)
            self.e1.set(select['name'])
            self.e2.set(select['start_date'])
            self.e3.set(select['travellers'])
            self.e4.set(select['duration'])
            self.e5.set(select['coordinator'])
            self.e6.set(select['contact'])

    def show(self):
        self.tree.heading('name', text='Name')
        self.tree.heading('start_date', text='Start Date')
        self.tree.heading('travellers', text='Travellers')
        self.tree.heading('duration', text='Duration')
        self.tree.heading('coordinator', text='Coordinator')
        self.tree.heading('contact', text='Contact')
        self.tree.grid(row=8, column=0, pady=20, columnspan=7, sticky='e')
        records = self.db.load_data()
        # Clear the treeview list items
        for item in self.tree.get_children():
            self.tree.delete(item)
        # load data
        for x in records:
            self.tree.insert("", "end", values=(
                x['name'],
                x['start_date'],
                x['travellers'],
                x['duration'],
                x['coordinator'],
                x['contact']
            ))

    def show_form(self):
        # root.state("zoomed")
        self.tfroot.title("Solent - Trips")
        self.tfroot.geometry("1223x500")
        self.frm.grid()
        ttk.Label(self.frm, background="green", text="Solent Trips", font=("Arial", 25), anchor="center", padding=5,
                  foreground="white").grid(column=0, row=0, columnspan=10, sticky='nsew')

        ttk.Label(self.frm, text="Name: ", padding=4).grid(column=0, row=2, sticky='e')
        Entry(self.frm, textvariable=self.e1).grid(row=2, column=1, sticky='w')

        ttk.Label(self.frm, text="Start Date: ", padding=4).grid(column=0, row=3, sticky='e')
        Entry(self.frm, textvariable=self.e2).grid(row=3, column=1, sticky='w')

        ttk.Label(self.frm, text="Travellers: ", padding=4).grid(column=0, row=4, sticky='e')
        Entry(self.frm, textvariable=self.e3).grid(row=4, column=1, sticky='w')

        ttk.Label(self.frm, text="Duration: ", padding=4).grid(column=0, row=5, sticky='e')

        com_v = ('One-day trip', 'Weekend trip', 'Fortnight trip')
        ttk.Combobox(self.frm, textvariable=self.e4, values=com_v, state='readonly').grid(row=5, column=1, sticky='w')

        ttk.Label(self.frm, text="Coordinator: ", padding=4).grid(column=0, row=6, sticky='e')
        Entry(self.frm, textvariable=self.e5).grid(row=6, column=1, sticky='w')

        ttk.Label(self.frm, text="Contact: ", padding=4).grid(column=0, row=7, sticky='e')
        Entry(self.frm, textvariable=self.e6).grid(row=7, column=1, sticky='w')
        self.show()
        self.tree.bind('<<TreeviewSelect>>', self.get_value)
        Button(self.tfroot, text="Add", command=self.add, height=1, width=13).place(x=480, y=200)
        Button(self.tfroot, text="update", command=self.update, height=1, width=13).place(x=590, y=200)
        Button(self.tfroot, text="Delete", command=self.delete, height=1, width=13).place(x=700, y=200)
        Button(self.tfroot, text="Refresh", command=self.show, height=1, width=13).place(x=810, y=200)
        self.tfroot.mainloop()