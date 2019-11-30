from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry
import datetime
import pytesseract
import cv2
from Connect import Conn
from Obj.LichSuGuiXe import LichSuGuiXe
from Global import Global
from iconPath import path as icoPath

frame = Frame(bottom_frame)
frame.pack(side = LEFT, fill = BOTH, expand = True, padx = 10, pady = 10)

canvas = Canvas(frame, bg = 'pink')
canvas.pack(side = RIGHT, fill = BOTH, expand = True)

mailbox_frame = Frame(canvas, bg = 'purple')
canvas_frame = canvas.create_window((0,0),
    window=mailbox_frame, anchor = NW)
#mailbox_frame.pack(side = LEFT, fill = BOTH, expand = True)

mail_scroll = Scrollbar(canvas, orient = "vertical", 
    command = canvas.yview)
mail_scroll.pack(side = RIGHT, fill = Y)

canvas.config(yscrollcommand = mail_scroll.set)

mailbox_frame.bind("<Configure>", OnFrameConfigure)
canvas.bind('<Configure>', FrameWidth)

def FrameWidth(event):
    canvas_width = event.width
    anvas.itemconfig(canvas_frame, width = canvas_width)

def OnFrameConfigure(event):
    anvas.configure(scrollregion=canvas.bbox("all"))