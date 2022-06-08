from tkinter import *
from tkinter import ttk, messagebox

from dashboad import Dashboard
from database import Database
from system_user import SystemUser


class LoginForm:
    def __init__(self):
        self.root = Tk()
        self.username = StringVar()
        self.password = StringVar()
        self.msg = StringVar()
        self.frm = ttk.Frame(self.root, padding=15)
        self.view_login_form()

    def view_login_form(self):
        self.root.geometry('230x160')
        self.root.title('Solent Trips - Login')
        self.frm.grid()
        ttk.Label(self.frm, background="green", text="Solent Trip Login", font=("Arial", 9), anchor="center", padding=5,
                  foreground="white").grid(column=0, row=0, columnspan=2, sticky='ew')
        ttk.Label(self.frm, text="Username: ", padding=4, font=("Arial", 8)).grid(column=0, row=1)
        ttk.Label(self.frm, text="Password: ", padding=4, font=("Arial", 8)).grid(column=0, row=2)
        Entry(self.frm, textvariable=self.username, font=("Arial", 8)).grid(row=1, column=1)
        Entry(self.frm, textvariable=self.password, show='*', font=("Arial", 8)).grid(row=2, column=1)
        ttk.Label(self.frm, text="", textvariable=self.msg, font=("Arial", 8), foreground="red").grid(column=0, row=4, columnspan=2)
        ttk.Button(self.frm, text="Login", command=self.authenticate_login).grid(column=1, row=3, sticky="e")
        self.root.mainloop()

    def authenticate_login(self):
        user = self.username.get()
        passwd = self.password.get()
        db = Database('json/users.json')

        if user == '' or passwd == '':
            self.msg.set("fill the empty fields!!!")
        else:
            x = db.get_one_user_from_json(user)
            if x:
                if passwd == passwd:
                    self.root.destroy()
                    db = Dashboard(x)
                else:
                    self.msg.set("Username or password incorrect!")
            else:
                self.msg.set("Username or password incorrect!")


