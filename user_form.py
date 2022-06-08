import json
from tkinter import ttk, messagebox
from tkinter import *
from database import Database
from system_user import SystemUser


class UserForm:
    def __init__(self):
        self.db = Database('json/users.json')
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=10)
        self.e1 = StringVar()
        self.e2 = StringVar()
        self.e3 = StringVar()
        self.e4 = StringVar()
        self.e5 = StringVar()
        cols = ('id', 'name', 'user_type', 'username', 'password')
        self.tree = ttk.Treeview(self.frm, columns=cols, show='headings')
        self.show_user_form()

    def add(self):
        id = self.e1.get()
        name = self.e2.get()
        user_type = self.e3.get()
        username = self.e4.get()
        password = self.e5.get()
        user = SystemUser(id, name, user_type, username, password)
        user.save_user()
        messagebox.showinfo("information", "User inserted successfully...")
        self.clear_fields()

    def update(self):
        id = self.e1.get()
        name = self.e2.get()
        user_type = self.e3.get()
        username = self.e4.get()
        password = self.e5.get()
        user = SystemUser(id, name, user_type, username, password)
        user.update_user()
        messagebox.showinfo("information", "Record Updated successfully...")
        self.clear_fields()

    def delete(self):
        id = self.e1.get()
        name = self.e2.get()
        user_type = self.e3.get()
        username = self.e4.get()
        password = self.e5.get()
        user = SystemUser(id, name, user_type, username, password)
        user.delete_user()
        messagebox.showinfo("information", "Record Deleted successfully...")
        self.clear_fields()

    def clear_fields(self):
        self.e1.set("")
        self.e2.set("")
        self.e3.set("")
        self.e4.set("")
        self.e5.set("")

    def get_value(self, event):
        if len(self.tree.get_children()) > 0:
            row_id = self.tree.selection()[0]
            select = self.tree.set(row_id)
            self.e1.set(select['id'])
            self.e2.set(select['name'])
            self.e3.set(select['user_type'])
            self.e4.set(select['username'])
            self.e5.set(select['password'])

    def show(self):
        self.tree.heading('id', text='ID')
        self.tree.heading('name', text='Name')
        self.tree.heading('user_type', text='User Type')
        self.tree.heading('username', text='Username')
        self.tree.heading('password', text='Passwrd')
        self.tree.grid(row=7, column=0, pady=20, columnspan=7, sticky='e')
        records = self.db.load_data()
        # Clear the treeview list items
        for item in self.tree.get_children():
            self.tree.delete(item)
        # load data
        for x in records:
            self.tree.insert("", "end", values=(
                x['id'],
                x['name'],
                x['user_type'],
                x['username'],
                x['password']
            ))

    def show_user_form(self):
        # root.state("zoomed")
        self.root.title("Solent - Users")
        self.root.geometry("1223x500")
        self.frm.grid()
        ttk.Label(self.frm, background="green", text="System Users", font=("Arial", 25), anchor="center", padding=5,
                  foreground="white").grid(column=0, row=0, columnspan=10, sticky='nsew')
        ttk.Label(self.frm, text="ID: ", padding=4).grid(column=0, row=2, sticky='e')
        Entry(self.frm, textvariable=self.e1).grid(row=2, column=1, sticky='w')
        ttk.Label(self.frm, text="Name: ", padding=4).grid(column=0, row=3, sticky='e')
        Entry(self.frm, textvariable=self.e2).grid(row=3, column=1, sticky='w')
        ttk.Label(self.frm, text="User Type: ", padding=4).grid(column=0, row=4, sticky='e')
        types = ('Administrator', 'Manager', 'Coordinator')
        ttk.Combobox(self.frm, textvariable=self.e3, values=types, state='readonly').grid(row=4, column=1, sticky='w')
        ttk.Label(self.frm, text="Username: ", padding=4).grid(column=0, row=5, sticky='e')
        Entry(self.frm, textvariable=self.e4).grid(row=5, column=1, sticky='w')
        ttk.Label(self.frm, text="Password: ", padding=4).grid(column=0, row=6, sticky='e')
        Entry(self.frm, textvariable=self.e5).grid(row=6, column=1, sticky='w')
        self.show()
        self.tree.bind('<<TreeviewSelect>>', self.get_value)
        Button(self.root, text="add", command=self.add, height=1, width=13).place(x=480, y=180)
        Button(self.root, text="update", command=self.update, height=1, width=13).place(x=590, y=180)
        Button(self.root, text="Delete", command=self.delete, height=1, width=13).place(x=700, y=180)
        Button(self.root, text="Refresh", command=self.show, height=1, width=13).place(x=810, y=180)
        self.root.mainloop()