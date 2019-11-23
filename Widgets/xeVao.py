import tkinter
from tkinter import *
from tkinter import font
import PIL
from PIL import Image, ImageTk
from tkinter.ttk import *
from time import strftime
import pytesseract
import cv2
import tkinter.messagebox
from iconPath import path as icoPath

class XeVao:
    def __init__(self, window):
        #window = Tk()
        #window.title('Model Definition')
        #window.resizable(width=FALSE, height=FALSE)
        #window.geometry("1162x696+0+0")
        
        self.window = window
        childTab = window.newChild(title='Tài khoản', iconfile=icoPath+'Parking.ico')
        childTab.setSize(leftPos=20, rightPos=1200, topPos=20, bottomPos=700)#("400x370+100+100")
        childFrame = childTab.interior
        
        SoBien=StringVar()
        HoTen=StringVar()
        MaThe=StringVar()

        def thongbao():
            tkinter.messagebox.showinfo("Lưu ý", "Thông xe thành công")


        camera1=LabelFrame(childFrame, text="Camera trước", width="580", height="348")
        camera1.place(x=0, y=0)
        camera2=LabelFrame(childFrame, text="Camera trước", width="580", height="348")
        camera2.place(x=0, y=348)
        thongtin=LabelFrame(childFrame, text="Thông tin", width="580", height="696")
        thongtin.place(x=580, y=0)


        #===========================================================
        #width, height = 580, 348
        width, height = 580, 300
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        camera1.bind('<Escape>', lambda e: camera1.quit())
        lmain = Label(camera1)
        lmain.pack()

        def show_frame():
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = PIL.Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            lmain.after(10, show_frame)
        show_frame()

        #===========================================================

        khung3=LabelFrame(thongtin, text="Thông tin", width="570", height="687")
        khung3.place(x=610,y=1)

        anhbien=LabelFrame(thongtin, text="Ảnh biên", width=" 250", height="250")
        anhbien.place(x=20,y=280)
        entryanhbien=Entry(thongtin, textvar=SoBien , width=30 )
        entryanhbien.place(x=55, y=550)

        anhmat=LabelFrame(thongtin, text="Ảnh mặt", width=" 250", height="250")
        anhmat.place(x=300,y=280)
        buttonthongxe=Button(thongtin, text="Thông xe", width=20, command=thongbao)
        buttonthongxe.place(x=350,y=550)






        labelhoten=Label(thongtin, text="Họ và Tên : ", width=20)
        labelhoten.place(x=10, y=10)
        entryhoten=Entry(thongtin, textvar=HoTen, width=30 )
        entryhoten.place(x=200, y=10)

        labelngayvao=Label(thongtin, text="Ngày vào : ", width=20)
        labelngayvao.place(x=10, y=50)
        labelngayvao=Entry(thongtin, textvar=MaThe, width=30 )
        labelngayvao.place(x=200, y=50)



        labelmathe=Label(thongtin, text="Mã thẻ : ", width=20)
        labelmathe.place(x=10, y=90)
        entrymathe=Entry(thongtin, textvar=MaThe, width=30 )
        entrymathe.place(x=200, y=90)
