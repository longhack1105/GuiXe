from tkinter import *

master = Tk()
frame = Frame(master)

w = Canvas(master, width=200, height=100)
w.pack()

w.create_window(0, 0, window=frame, anchor="nw")

mainloop()