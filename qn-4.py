from tkinter import *
from tkinter import messagebox
master = Tk()
master.title('tk')
Label(master, text='Bookingid').grid(row=0)
Label(master, text='Passenger Name').grid(row=1)
Label(master, text='Flight').grid(row=2)
Label(master, text='source').grid(row=3)
Label(master, text='Duration').grid(row=4)
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
var1 = IntVar()
Radiobutton(master, text="Delhi", variable=var1).grid(row=3, column=1, sticky=W)
var2 = IntVar()
Radiobutton(master, text="Mumbai Destination", variable=var2).grid(row=3, column=2, sticky=W)
var3 = IntVar()
Radiobutton(master, text="Chennai", variable=var3).grid(row=3, column=3, sticky=W)
var4 = IntVar()
Radiobutton(master, text="Kolkata", variable=var4).grid(row=3, column=4, sticky=W)

spin = Spinbox(master, from_= 0, to = 25)
spin.grid(row=4,column=1)

btn = Button(master, text='Insert').grid(row=5)
btn = Button(master, text='Update').grid(row=5, column=1)
btn = Button(master, text='Delete').grid(row=6)
btn = Button(master, text='Select').grid(row=6, column=1)
mainloop()