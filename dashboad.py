from tkinter import ttk, messagebox
from tkinter import *
from trips_view import TripView
from user_form import UserForm


class Dashboard:
    def __init__(self, user):
        self.root = Tk()
        self.user = user
        self.show_dashboard()

    def load_trips_form(self):
        TripView()


    def load_user_form(self):
        UserForm()

    def show_dashboard(self):
        # root.state("zoomed")
        self.root.title("Solent - Trips")
        # root.geometry("800x500")
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()
        ttk.Label(frm, background="green", text="Solent Trips", font=("Arial", 25), anchor="center", padding=5,
                  foreground="white").grid(column=0, row=0, columnspan=4, sticky='nsew')
        Button(frm, text="Trips", command=self.load_trips_form, height=5, width=13, font=("arial", 16)).grid(column=0, row=1, pady=20, padx=20)
        if self.user['user_type'] == 'Administrator' or self.user['user_type'] == 'Manager':
            Button(frm, text="Users", command=self.load_user_form, height=5, width=13, font=("arial", 16)).grid(column=1, row=1, pady=20, padx=20)
        self.root.mainloop()
