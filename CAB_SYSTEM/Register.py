from tkinter import *
import mysql.connector
import datetime as dt
import tkinter.messagebox
import re

objectDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="CBS"
)
instance = objectDB.cursor()


class RegisterProcess:
    def __init__(self):
        register = Tk()
        register.geometry('1080x768')
        date = dt.datetime.now()

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        def check(email):
            if re.fullmatch(regex, email):
                print("Valid Email")
            else:
                tkinter.messagebox.showwarning(title="Invalid Entry", message="Enter Correct E-mail")

        def insert():
            name = entername.get()
            if not name:
                tkinter.messagebox.showwarning(title="Cannot leave name empty", message="All fields are mandatory")

            username = enteruser.get()
            if not username:
                tkinter.messagebox.showwarning(title="Cannot leave username empty", message="All fields are mandatory")

            gender = "NA"
            if self.v.get() == 1:
                gender = "Female"
            elif self.v.get() == 0:
                gender = "Male"
            else:
                tkinter.messagebox.showwarning(title="No gender selected", message="All fields are mandatory")

            mobile = enternum.get()

            Uid = enteruid.get()
            if not Uid:
                tkinter.messagebox.showwarning(title="Cannot leave uid empty", message="All fields are mandatory")

            email = enteremail.get()
            if not email:
                check(email)

            password = enterpass.get()
            if not password:
                tkinter.messagebox.showwarning(title="Cannot leave password empty", message="All fields are mandatory")

            sql1 = "insert into LogDetails values (%s,%s,%s,%s,%s,%s,%s)"
            val = (name, username, gender, mobile, int(Uid), email, password)
            instance.execute(sql1, val)
            objectDB.commit()
            self.success()

        Label(register, text=f"{date:%A, %B %d, %Y}", font="Calibri, 14").place(x=400, y=650)

        heading = Label(register, text="Register", width=30, font=(
            'georgia 40 bold'), fg='orange', bg='black')
        heading.place(x=0, y=10)

        # Entry for name
        Label(register, text="Name").place(x=400, y=200)
        entername = Entry(register)
        entername.place(x=500, y=200)

        # Entry for username
        Label(register, text="Create Username").place(x=400, y=250)
        enteruser = Entry(register)
        enteruser.place(x=500, y=250)

        # Entry for gender
        self.v = IntVar()
        Label(register, text="Gender").place(x=400, y=300)
        Radiobutton(register, text="Male", variable=self.v, value=0).place(x=500, y=300)
        Radiobutton(register, text="Female", variable=self.v, value=1).place(x=570, y=300)

        Label(register, text="Mobile No.").place(x=400, y=350)
        enternum = Entry(register)
        enternum.place(x=500, y=350)

        Label(register, text="UID").place(x=400, y=400)
        enteruid = Entry(register)
        enteruid.place(x=500, y=400)

        Label(register, text="Email Id").place(x=400, y=450)
        enteremail = Entry(register)
        enteremail.place(x=500, y=450)

        Label(register, text="Create Password").place(x=400, y=500)
        enterpass = Entry(register)
        enterpass.place(x=500, y=500)

        Button(register, text="Register", command=insert).place(x=500, y=550)

        register.mainloop()

    def success(self):
        tkinter.messagebox.showwarning(title="Welcome", message="You have register successfully")
        self.gonext()

    def gonext(self):
        import MidLand as Mid
        Mid.MidLandProcess()


RegisterProcess()
