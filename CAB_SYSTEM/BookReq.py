from tkinter import *
import tkinter.messagebox
import mysql.connector
import random as r


objectDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Veracita@19!",
    database="CBS"
)
instance = objectDB.cursor(buffered=True)


class BookingProcess:
    def __init__(self):
        book = Tk()
        book.geometry('1080x768')

        def getval():
            mobile = bmnum.get()
            if not bmnum:
                tkinter.messagebox.showwarning(title="Cannot leave Mobile No. empty", message="All fields are mandatory")

            # Uid = buid.get()
            # if not Uid:
            #     tkinter.messagebox.showwarning(title="Cannot leave UID empty", message="All fields are mandatory")

            start = bfrom.get()
            if not bfrom:
                tkinter.messagebox.showwarning(title="Cannot leave from location empty", message="All fields are mandatory")

            end = bto.get()
            if not bto:
                tkinter.messagebox.showwarning(title="Cannot leave to location empty", message="All fields are mandatory")

            day = bday.get()
            if not bday:
                tkinter.messagebox.showwarning(title="Cannot leave password empty", message="All fields are mandatory")

            stime = btime.get()
            if not btime:
                tkinter.messagebox.showwarning(title="Cannot leave password empty", message="All fields are mandatory")

            botp = ""
            for i in range(4):
                botp += str(r.randint(1, 9))

            sql1 = "insert into BookDetails values (%s,%s,%s,%s,%s,%s)"
            val = (int(mobile), start, end, day, int(stime), botp)

            # bmobile , bfrom, bto, bday, btime, otp "

            instance.execute(sql1, val)
            objectDB.commit()
            tkinter.messagebox.showinfo("Booking Successful", botp)
            import MidLand as Mi
            Mi.MidLandProcess()

        heading = Label(book, text="Book your ride", width=30, font=(
            'georgia 40 bold'), fg='orange', bg='black')
        heading.place(x=0, y=10)

        Label(book, text="Mobile No.", font='georgia 16 bold').place(x=400, y=200)
        bmnum = IntVar()
        Entry(book, textvariable=bmnum).place(x=550, y=200)

        # Label(book, text="UID").place(x=400, y=250)
        # buid = IntVar()
        # Entry(book, textvariable=buid).place(x=500, y=250)

        Label(book, text="From", font='georgia 16 bold').place(x=400, y=250)
        bfrom = StringVar()
        Entry(book, textvariable=bfrom).place(x=550, y=250)

        Label(book, text="To", font='georgia 16 bold').place(x=400, y=300)
        bto = StringVar()
        Entry(book, textvariable=bto).place(x=550, y=300)

        Label(book, text="Day", font='georgia 16 bold').place(x=400, y=350)
        bday = IntVar()
        Entry(book, textvariable=bday).place(x=550, y=350)

        #time in hrs
        Label(book, text="Time", font='georgia 16 bold').place(x=400, y=400)
        btime = IntVar()
        Entry(book, textvariable=btime).place(x=550, y=400)

        Button(book, text="Book", font='georgia 16 bold', command=getval).place(x=500, y=500)
        book.mainloop()


BookingProcess()