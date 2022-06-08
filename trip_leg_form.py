import json
from tkinter import ttk, messagebox
from tkinter import *
from database import Database
from trip_leg import TripLeg


class TripLegs:
    def __int__(self):
        self.db = Database('json/tripleg.json')
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=10)
        self.e1 = StringVar()
        self.e2 = StringVar()
        self.e3 = StringVar()
        self.e4 = StringVar()
        self.e5 = StringVar()
        cols = ('trip_name', 'start_location', 'destination', 'transport_provider', 'transport_mode')
        self.tree = ttk.Treeview(self.frm, columns=cols, show='headings')
        self.show_trip_leg_form()

    def get_value(self, event):
        if len(self.tree.get_children()) > 0:
            row_id = self.tree.selection()[0]
            select = self.tree.set(row_id)
            self.e1.set(select['trip_name'])
            self.e2.set(select['start_location'])
            self.e3.set(select['destination'])
            self.e4.set(select['transport_provider'])
            self.e5.set(select['transport_mode'])

    def add(self):
        trip_name = self.e1.get()
        start_location = self.e2.get()
        destination = self.e3.get()
        transport_provider = self.e4.get()
        transport_mode = self.e5.get()
        tl = TripLeg(trip_name, start_location, destination, transport_provider, transport_mode)
        tl.save_tripleg()
        messagebox.showinfo("information", "Trip Leg inserted successfully...")
        self.clear_fields()
        self.show()

    def update(self):
        trip_name = self.e1.get()
        start_location = self.e2.get()
        destination = self.e3.get()
        transport_provider = self.e4.get()
        transport_mode = self.e5.get()
        tl = TripLeg(trip_name, start_location, destination, transport_provider, transport_mode)
        tl.update_tripleg()
        messagebox.showinfo("information", "Record Updated successfully...")
        self.clear_fields()
        self.show()

    def delete(self):
        trip_name = self.e1.get()
        start_location = self.e2.get()
        destination = self.e3.get()
        transport_provider = self.e4.get()
        transport_mode = self.e5.get()
        tl = TripLeg(trip_name, start_location, destination, transport_provider, transport_mode)
        tl.delete_tripleg()
        messagebox.showinfo("information", "Record Deleted successfully...")
        self.clear_fields()
        self.show()

    def clear_fields(self):
        self.e1.set("")
        self.e2.set("")
        self.e3.set("")
        self.e4.set("")
        self.e5.set("")

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
                x['trip_name'],
                x['start_location'],
                x['destination'],
                x['transport_provider'],
                x['transport_mode']
            ))

    def show_trip_leg_form(self):
        # root.state("zoomed")
        self.root.title("Solent - Trips")
        self.root.geometry("1223x500")
        self.frm.grid()
        ttk.Label(self.frm, background="green", text="Solent Trip Legs", font=("Arial", 25), anchor="center", padding=5,
                  foreground="white").grid(column=0, row=0, columnspan=10, sticky='nsew')
        ttk.Label(self.frm, text="Trip Name: ", padding=4).grid(column=0, row=2, sticky='e')
        Entry(self.frm, textvariable=self.e1).grid(row=2, column=1, sticky='w')
        ttk.Label(self.frm, text="Start Location: ", padding=4).grid(column=0, row=3, sticky='e')
        Entry(self.frm, textvariable=self.e2).grid(row=3, column=1, sticky='w')
        ttk.Label(self.frm, text="Destination: ", padding=4).grid(column=0, row=4, sticky='e')
        Entry(self.frm, textvariable=self.e3).grid(row=4, column=1, sticky='w')
        ttk.Label(self.frm, text="Transport Provider: ", padding=4).grid(column=0, row=4, sticky='e')
        Entry(self.frm, textvariable=e3).grid(row=4, column=1, sticky='w')
        ttk.Label(self.frm, text="Transport Mode: ", padding=4).grid(column=0, row=6, sticky='e')
        Entry(self.frm, textvariable=self.e5).grid(row=6, column=1, sticky='w')

        self.show()
        self.tree.bind('<<TreeviewSelect>>', self.get_value)
        Button(self.root, text="Add", command=self.add, height=1, width=13).place(x=480, y=200)
        Button(self.root, text="update", command=self.update, height=1, width=13).place(x=590, y=200)
        Button(self.root, text="Delete", command=self.delete, height=1, width=13).place(x=700, y=200)
        Button(self.root, text="Refresh", command=self.show, height=1, width=13).place(x=810, y=200)
        self.root.mainloop()