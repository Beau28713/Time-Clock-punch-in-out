import datetime
import time
import tkinter

def in_button(inbut):
    timein = datetime.datetime.now()
    in_button.starttime = time.time()
    print("Time In = " + str(timein))

def out_button(outbut):
    timeout = datetime.datetime.now()
    endtime = time.time()
    elaspedtime = (endtime - in_button.starttime) / 3600
    print("Time Out = " + str(timeout))
    print("Hours worked = " + str(round(elaspedtime, 4)))


######Gui setup########
mainwindow = tkinter.Tk()

inframe = tkinter.Frame(master = mainwindow, relief = tkinter.RAISED, borderwidth = 10)

outframe = tkinter.Frame(master = mainwindow, relief = tkinter.RAISED, borderwidth = 10)

inframe.grid(row = 0, column = 0, padx = 5, pady = 5)

outframe.grid(row = 0, column = 1, padx = 5, pady = 5)

inbut = tkinter.Button(master = inframe, text = "In", width = 10 )

inbut.pack()

inbut.bind("<Button-1>", in_button)#loking for left mouse click

outbut = tkinter.Button(master = outframe, text = "Out", width = 10)

outbut.pack()

outbut.bind("<Button-1>", out_button)#Looking for left mouse click

mainwindow.mainloop()
#########################
