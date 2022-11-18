from tkinter import *
import Routes as Ro
import datetime as dt
import mysql.connector
objectDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Veracita@19!",
    database="CBS"
)
instance = objectDB.cursor(buffered=True)


class Cabms:
    def __init__(self):
        cabms = Tk()
        cabms.geometry('1080x768')

        date = dt.datetime.now()
        Label(cabms, text=f"{date:%A, %B %d, %Y}", font="Calibri, 14").place(x=400, y=650)
        heading = Label(cabms, text="Car Booking System", width=30, font=(
            'georgia 40 bold'), fg='orange', bg='black')
        heading.place(x=0, y=10)

        login = Button(cabms, text="Login", font=(
            'georgia 20 bold'), fg='black', bg='grey', command=self.login)
        login.place(x=100, y=300)

        new_user = Button(cabms, text="New User", font=(
            'georgia 20 bold'), fg='black', bg='grey', command=self.register)
        new_user.place(x=450, y=300)

        avail_routes = Button(cabms, text="Available Routes", font=(
            'georgia 20 bold'), fg='black', bg='grey')
        avail_routes.place(x=800, y=300)

        cabms.mainloop()

    def register(self):
        import Register as Re
        Re.RegisterProcess()

    def login(self):
        import Login as Lo
        Lo.LoginProcess()
    # def routes(self):
    #     Ro.()


Cabms()






