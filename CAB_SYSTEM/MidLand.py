from tkinter import *
import datetime as dt

class MidLandProcess:
    def __init__(self):
        Mid = Tk()
        Mid.geometry('1080x768')
        date = dt.datetime.now()

        Label(Mid, text=f"{date:%A, %B %d, %Y}", font="Calibri, 14").place(x=400, y=650)

        heading = Label(Mid, text="Book/Track Ride", width=30, font=(
            'georgia 40 bold'), fg='orange', bg='black')
        heading.place(x=0, y=10)

        Button(Mid, text="Booking", width=25, height=5, command=self.jump_book).place(x=300, y=200)

        Button(Mid, text="Track Ride", width=25, height=5, command=self.trackride).place(x=600, y=200)
        Mid.mainloop()

    def jump_book(self):
        import BookReq as Bo
        Bo.BookingProcess()

    def trackride(self):
        import TrackCab as tr
        tr.TrackCabProcess()


MidLandProcess()