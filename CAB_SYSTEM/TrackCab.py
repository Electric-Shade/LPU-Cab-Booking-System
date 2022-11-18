from tkinter import *
import datetime as dt
import mysql.connector
objectDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Veracita@19!",
    database="CBS"
)
instance = objectDB.cursor(buffered=True)

class TrackCabProcess:
    def __init__(self):
        Tcab = Tk()
        Tcab.geometry('1080x768')
        date = dt.datetime.now()

        def otpuser():
            otp_verify = onetp.get()
            mobile_verify = mob.get()

            print(onetp.get())

            loadpass = "SELECT otp FROM BookDetails WHERE bmobile = %s "
            val = ([mobile_verify])

            instance.execute(loadpass, val)
            passcheck = instance.fetchone()

            print(passcheck[0])
            passlist = (otp_verify)

            if passcheck[0] == passlist:
                Label(Tcab, Text="You cab is on it's way").place(x= 400,y=600)
            else:
                print("You're not booked, Go back to booking page")
            # print("values were", username_verify, password_verify)

        Label(Tcab, text=f"{date:%A, %B %d, %Y}", font="Calibri, 14").place(x=400, y=650)

        heading = Label(Tcab, text="Track Your Cab", width=30, font=(
            'georgia 40 bold'), fg='orange', bg='black')
        heading.place(x=0, y=10)

        heading = Label(Tcab, text="Before tracking your cab please ensure that your have your username and OTP", width=83, font=(
            'georgia 14 bold'), fg='orange', bg='black')
        heading.place(x=0, y=100)

        Label(Tcab, text="Enter your Mobile No.", font='georgia 15 bold').place(x=300, y=200)
        mob = IntVar()
        Entry(Tcab, textvariable=mob).place(x=600, y=200)

        Label(Tcab, text="Enter your OTP", font='georgia 15 bold').place(x=300, y=300)
        onetp = IntVar()
        Entry(Tcab, textvariable=onetp).place(x=600, y=300)

        Button(Tcab, text="Track", width=17, height=2, command=otpuser()).place(x=450, y=400)

        Button(Tcab, text="Book", width=17, height=2, command=self.jump_book).place(x=450, y=500)

        Tcab.mainloop()

    def jump_book(self):
        import BookReq as Bo
        Bo.BookingProcess()


TrackCabProcess()