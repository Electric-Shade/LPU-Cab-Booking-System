from tkinter import *
import datetime as dt
import mysql.connector
import re
objectDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Veracita@19!",
    database="CBS"
)
instance = objectDB.cursor(buffered=True)


class LoginProcess:
    def __init__(self):
        login = Tk()
        login.geometry('1080x768+200+150')
        date = dt.datetime.now()
        login.resizable(False, False)

        def verifyuser():
            username_verify = ue.get()
            password_verify = pd.get()
            # uid_verify = ud.get()

            loadpass = "SELECT password FROM LogDetails WHERE username = %s "
            val = ([username_verify])

            instance.execute(loadpass, val)
            passcheck = list(instance.fetchone())
            print(passcheck)
            passlist = []
            passlist.append(password_verify)

            if passcheck == passlist:
                print("logged in with username", username_verify, "and password", password_verify)
                self.next()
            else:
                print("You're not registered, Register Now by clicking on new user")
            # print("values were", username_verify, password_verify)

        heading = Label(login, text="Login", font=(
            'georgia 40 bold'), width=30, fg='orange', bg='black')
        heading.place(x=0, y=0)

        Label(login, text=f"{date:%A, %B %d, %Y}", font="Calibri, 14").place(x=400, y=650)

        Label(login, text="UserName").place(x=400, y=200)
        ue = StringVar()
        Entry(login, textvariable=ue).place(x=500, y=200)

        # Label(login, text="UID").place(x=400, y=300)
        # ud = StringVar()
        # Entry(login, textvariable=ud).place(x=500, y=300)

        Label(login, text="Password").place(x=400, y=300)
        pd = StringVar()
        Entry(login, textvariable=pd).place(x=500, y=300)

        Button(login, text="New User", command=self.newuser).place(x=505, y=500)

        Button(login, text="Login Now", command=verifyuser).place(x=500, y=400)
        login.mainloop()

    def newuser(self):
        import Register as Ro
        Ro.RegisterProcess()

    def next(self):
        import MidLand as Mi
        Mi.MidLandProcess()


Call = LoginProcess()
