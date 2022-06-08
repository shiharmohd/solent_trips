from tkinter import ttk
from tkinter import *

from traveller_form import TravellerForm
from trip_form import TripForm
from database import Database


class TripView:
    def __init__(self):
        self.db = Database('json/trip.json')
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=10)
        cols = ('name', 'start_date', 'travellers', 'duration', 'coordinator', 'contact')
        self.tree = ttk.Treeview(self.frm, columns=cols, show='headings')
        self.show_trips_view()

    def show_trips(self):
        TripForm()

    def show_travellers(self):
        TravellerForm()

    def show(self):
        self.tree.heading('name', text='Name')
        self.tree.heading('start_date', text='Start Date')
        self.tree.heading('travellers', text='Travellers')
        self.tree.heading('duration', text='Duration')
        self.tree.heading('coordinator', text='Coordinator')
        self.tree.heading('contact', text='Contact')
        self.tree.grid(row=2, column=0, pady=20, columnspan=10, sticky='e')
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

    def show_trips_view(self):
        # root.state("zoomed")
        self.root.title("Solent - Trips")
        self.root.geometry("1223x500")
        self.frm.grid()
        ttk.Label(self.frm, background="green", text="Solent Trips", font=("Arial", 25), anchor="center", padding=5,
                  foreground="white").grid(column=0, row=0, columnspan=6, sticky='nsew')
        btfrm = ttk.Frame(self.frm, padding=5)
        btfrm.grid(column=0, row=1)
        Button(btfrm, text="Trips", command=self.show_trips, height=2, width=13).grid(column=0, row=0, padx=5)
        Button(btfrm, text="Travellers", command=self.show_travellers, height=2, width=13).grid(column=1, row=0, padx=5)
        Button(btfrm, text="Refresh", command=self.show, height=2, width=13).grid(column=2, row=0, padx=5)
        self.show()
        self.root.mainloop()