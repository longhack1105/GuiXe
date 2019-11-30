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

class XeRa:
    def __init__(self, window):
        self.window = window
        #test
        if Global.test == 1:
            window.geometry("700x500")
            print('test ver')
        else:
            childTab = window.newChild(title='Quản lý xe ra', iconfile=icoPath+'Parking.ico')
            childTab.setSize(leftPos=20, rightPos=730, topPos=20, bottomPos=620)#("400x370+100+100")
            childFrame = childTab.interior

        #window.after_idle(lambda: window.minsize(200, 60))
        #window.title("Hệ thống quản lý bãi xe thông minh")
        #window.geometry("%dx%d+200+200" % (window.winfo_screenwidth()-500, window.winfo_screenheight()-300))


        
        ###frm main
        if Global.test == 1:
            frm = Frame(window)
        else: 
            frm = Frame(childFrame)

        frm.pack(fill=BOTH, expand=1)
        
        ###khai báo
        hoTen = StringVar()
        self.width_pic, self.height_pic = 0, 0
        #self.check=0
        #width, height = 290, 150
        self.width_video, self.height_video = 290, 150
        
        try: self.cap = cv2.VideoCapture(0)  
        except: 
            self.cap.release() 
            self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width_video)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height_video) 
        def show_frame():
            _, frame = self.cap.read()
            frame = cv2.flip(frame, 1)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            
            try: 
                #self.width_video, self.height_video = lblCamPlate.winfo_width()-4, lblCamPlate.winfo_height()-4
                img = img.resize((self.width_video, self.height_video),Image.ANTIALIAS)
            except: pass
            
            imgtk = ImageTk.PhotoImage(image=img)
            
            lblCamFace.imgtk = imgtk
            lblCamFace.configure(image=imgtk)
            
            lblCamPlate.imgtk = imgtk
            lblCamPlate.configure(image=imgtk)
            
            lblCamPlate.after(100, show_frame)

        self.dem = 0    
        def resize_video(event):
            #self.check=1
            self.dem+=1
            print('%s' % str(self.dem))
            
            height = lblCamPlate.winfo_height()
            width = lblCamPlate.winfo_width()
            #self.width_video, self.height_video = lblCamPlate.winfo_width()-4, lblCamPlate.winfo_height()-4
            #self.check = 0
            #show_frame()
            
            
            if self.height_video < height-5:
                self.width_video, self.height_video = width, height
                return
            if self.width_video < width-5:
                self.width_video, self.height_video = width, height
                return
            if self.height_video > height+5:
                self.width_video, self.height_video = width, height
                return
            if self.width_video > width+5:
                self.width_video, self.height_video = width, height
                return
           
        ###frm_cam
        frm_cam = Frame(frm)
        frm_cam.pack(side=LEFT, fill=BOTH, expand=1)
        
        ###frm_camface
        frm_camface = LabelFrame(frm_cam, text='CAMERA MẶT')
        frm_camface.pack(side=TOP, fill=BOTH, expand=1)
        
        lblCamFace = Label(frm_camface)
        lblCamFace.pack(fill=BOTH, expand=1)
        
        ###frm_camplate
        frm_camplate = LabelFrame(frm_cam, text='CAMMERA BIỂN')
        frm_camplate.pack(side=BOTTOM, fill=BOTH, expand=1)
                
        lblCamPlate = Label(frm_camplate)
        lblCamPlate.pack(fill=BOTH, expand=1)
        
        ###call show frame va resize_video
        lblCamPlate.bind("<Configure>", resize_video)
        show_frame()
        
        
        
        
        ###frm_info
        frm_info = LabelFrame(frm, text='THÔNG TIN XE')
        frm_info.pack(side=RIGHT, fill=BOTH, expand=1)
        
        ##ho ten
        frm_hoten = Frame(frm_info)
        frm_hoten.pack(side=TOP, fill=X)
        
        lblHoTen = Label(frm_hoten, text='Họ tên: ', width=8, anchor=W)
        lblHoTen.pack(side=LEFT)
        
        etrHoTen = Entry(frm_hoten, width=30)
        etrHoTen.insert(0, "Tên dân cư/Khách lẻ")
        etrHoTen.pack(side=LEFT)
        
        lblspace = Label(frm_hoten,width=100)
        lblspace.pack(side=LEFT)
        ##day in
        frm_dayin = Frame(frm_info)
        frm_dayin.pack(side=TOP, fill=X)
        
        lblDayIn = Label(frm_dayin, text='Ngày vào: ', width=8, anchor=W)
        lblDayIn.pack(side=LEFT)
        
        dteDayIn = DateEntry(frm_dayin, background='darkblue',
                    foreground='white', borderwidth=2, width=15)
        dteDayIn.pack(side=LEFT)
        
        TimeIn = Frame(frm_dayin)
        TimeIn.pack(side=LEFT)
        
        cboDayInHH = ttk.Combobox(TimeIn, width=2)
        cboDayInHH.pack(side=LEFT)
        cboDayInMM = ttk.Combobox(TimeIn, width=2)
        cboDayInMM.pack(side=LEFT)

        ##dayout
        frm_dayout = Frame(frm_info)
        frm_dayout.pack(side=TOP, fill=X)
        
        lblDayOut = Label(frm_dayout, text='Ngày ra: ', width=8, anchor=W)
        lblDayOut.pack(side=LEFT)
        
        dteDayOut = DateEntry(frm_dayout, background='darkblue',
                    foreground='white', borderwidth=2, width=15)
        dteDayOut.pack(side=LEFT)
        
        TimeOut = Frame(frm_dayout)
        TimeOut.pack(side=LEFT)
        
        cboDayOutHH = ttk.Combobox(TimeOut, width=2)
        cboDayOutHH.pack(side=LEFT)
        cboDayOutMM = ttk.Combobox(TimeOut, width=2)
        cboDayOutMM.pack(side=LEFT)
        
        ##số ngày
        frm_countday = Frame(frm_info)
        frm_countday.pack(side=TOP, fill=X)
        
        lblCountDay = Label(frm_countday, text='Số ngày: ', width=8, anchor=W)
        lblCountDay.pack(side=LEFT)
        
        etrCountDay = Entry(frm_countday, width=30)
        etrCountDay.insert(0, "1")
        etrCountDay.pack(side=LEFT)
        
        ##mã thẻ
        frm_idcard = Frame(frm_info)
        frm_idcard.pack(side=TOP, fill=X)
        
        lblIdCard = Label(frm_idcard, text='Mã thẻ: ', width=8, anchor=W)
        lblIdCard.pack(side=LEFT)
        etrIdCard = Entry(frm_idcard, width=30)
        etrIdCard.pack(side=LEFT)
        
        ##ảnh vào
        frm_picin = LabelFrame(frm_info, text='Ảnh vào')
        frm_picin.pack(side=TOP, fill=BOTH, expand=1)
        
        #ảnh biển
        frm_picin_plate = Frame(frm_picin)
        frm_picin_plate.pack(side=LEFT, fill=X, expand=1)
        
        frm_picin_plate_txt = Frame(frm_picin_plate)
        frm_picin_plate_txt.pack(side=TOP, fill=BOTH, expand=1)
        
        lblPicPlateIn = Label(frm_picin_plate_txt, text='Ảnh biển: ', width=8, anchor=W)
        lblPicPlateIn.pack(side=LEFT)
        
        self.etrPlateIn = Entry(frm_picin_plate_txt)
        self.etrPlateIn.pack(side=LEFT, fill=BOTH, expand=1)
        
        self.imgData = Image.open("1.png")
        resized = self.imgData.resize((30,30),Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(resized)
        
        self.display = Canvas(frm_picin_plate, bd=0, highlightthickness=0)
        self.display.create_image(0, 0, image=self.img, anchor=NW, tags="IMG")

        self.display.pack(side=BOTTOM, fill=BOTH, expand=1)


        #ảnh mặt
        frm_picin_face = Frame(frm_picin)
        frm_picin_face.pack(side=RIGHT, fill=X, expand=1)
        
        frm_picin_face_txt = Frame(frm_picin_face)
        frm_picin_face_txt.pack(side=TOP, fill=BOTH, expand=1)
        
        lblPicPlateOut = Label(frm_picin_face_txt, text='Ảnh mặt: ')
        lblPicPlateOut.pack(side=LEFT)
        
        self.imgData2 = Image.open("2.png")
        resized = self.imgData2.resize((30,30),Image.ANTIALIAS)
        self.img2 = ImageTk.PhotoImage(resized)
        
        self.display2 = Canvas(frm_picin_face, bd=0, highlightthickness=0)
        self.display2.create_image(0, 0, image=self.img2, anchor=NW, tags="IMG2")
        self.display2.pack(side=BOTTOM, fill=BOTH, expand=1)


        ##ảnh ra 
        frm_picout = LabelFrame(frm_info, text='Ảnh ra')
        frm_picout.pack(side=TOP, fill=BOTH, expand=1)
        
        #ảnh biển
        frm_picout_plate = Frame(frm_picout)
        frm_picout_plate.pack(side=LEFT, fill=BOTH, expand=1)
        
        frm_picout_plate_txt = Frame(frm_picout_plate)
        frm_picout_plate_txt.pack(side=TOP, fill=BOTH, expand=1)
        
        lblPicPlateOut = Label(frm_picout_plate_txt, text='Ảnh biển: ', width=8, anchor=W)
        lblPicPlateOut.pack(side=LEFT)
        
        self.etrPlateOut = Entry(frm_picout_plate_txt)
        self.etrPlateOut.pack(side=LEFT, fill=BOTH, expand=1)
        
        self.imgData3 = Image.open("1.png")
        resized = self.imgData3.resize((30,30),Image.ANTIALIAS)
        self.img3 = ImageTk.PhotoImage(resized)
        
        self.display3 = Canvas(frm_picout_plate, bd=0, highlightthickness=0)
        self.display3.create_image(0, 0, image=self.img3, anchor=NW, tags="IMG3")
        self.display3.pack(side=BOTTOM, fill=BOTH, expand=1)

        #ảnh mặt
        frm_picout_face = Frame(frm_picout)
        frm_picout_face.pack(side=RIGHT, fill=BOTH, expand=1)
        
        frm_picout_face_txt = Frame(frm_picout_face)
        frm_picout_face_txt.pack(side=TOP, fill=BOTH, expand=1)
        
        lblPicFaceOut = Label(frm_picout_face_txt, text='Ảnh mặt: ')
        lblPicFaceOut.pack(side=LEFT)
        
        self.imgData4 = Image.open("2.png")
        resized = self.imgData4.resize((30,30),Image.ANTIALIAS)
        self.img4 = ImageTk.PhotoImage(resized)
        
        self.display4 = Canvas(frm_picout_face, bd=0, highlightthickness=0)
        self.display4.create_image(0, 0, image=self.img4, anchor=NW, tags="IMG4")
        self.display4.pack(side=BOTTOM, fill=BOTH, expand=1)
        
        ##data check
        frm_datamacth = Frame(frm_info)
        frm_datamacth.pack(side=TOP, fill=BOTH)
        #thông báo khớp data
        lblDataMacth = Label(frm_datamacth)
        lblDataMacth.config(text='Chưa code', fg='red', font=("Courier",16,'bold'))#data in
        lblDataMacth.pack(side=LEFT, fill=BOTH, expand=1)
        #btnThongXe
        btnThongXe = Button(frm_datamacth, text='Thông xe')
        btnThongXe.pack(side=RIGHT, fill=BOTH, expand=1)
        self.display4.bind("<Configure>", self.resize_pic)
        
        '''
        test 
        
        data = self.get_data(tbl='tbllichsuguixe')
        for row in data:
            print(row['IdGui'])
        
        test 
        '''
        
        
        
    
    def __del__(self):
        self.cap.release()
        
        
    def resize_pic(self, event):
        '''
        self.dem+=1
        print('%s' % str(self.dem))
        '''
        #size = (event.width, event.height)
        #size = (self.display4.winfo_width(), self.display4.winfo_height())
        width, height = self.display4.winfo_width(), self.display4.winfo_height()
        if self.height_pic < height-5:
            self.width_pic, self.height_pic = width, height
            size = (self.display4.winfo_width(), self.display4.winfo_height())
        elif self.width_pic < width-5:
            self.width_pic, self.height_pic = width, height
            size = (self.display4.winfo_width(), self.display4.winfo_height())
        elif self.height_pic > height+5:
            self.width_pic, self.height_pic = width, height
            size = (self.display4.winfo_width(), self.display4.winfo_height())
        elif self.width_pic > width+5:
            self.width_pic, self.height_pic = width, height
            size = (self.display4.winfo_width(), self.display4.winfo_height())

        

        try:

            self.etrPlateOut.config(width=1)
            self.etrPlateIn.config(width=1)
            
            resized = self.imgData.resize(size,Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(resized)
            self.display.delete("IMG")
            self.display.create_image(0, 0, image=self.img, anchor=NW, tags="IMG")
            self.display.config(width=self.display4.winfo_width(), height=self.display4.winfo_height())
            
            resized2 = self.imgData2.resize(size,Image.ANTIALIAS)
            self.img2 = ImageTk.PhotoImage(resized2)
            self.display2.delete("IMG2")
            self.display2.create_image(0, 0, image=self.img2, anchor=NW, tags="IMG2")
            self.display2.config(width=self.display4.winfo_width(), height=self.display4.winfo_height())
            
            resized3 = self.imgData3.resize(size,Image.ANTIALIAS)
            self.img3 = ImageTk.PhotoImage(resized3)
            self.display3.delete("IMG3")
            self.display3.create_image(0, 0, image=self.img3, anchor=NW, tags="IMG3")
            self.display3.config(width=self.display4.winfo_width(), height=self.display4.winfo_height())
            
            resized4 = self.imgData4.resize(size,Image.ANTIALIAS)
            self.img4 = ImageTk.PhotoImage(resized4)
            self.display4.delete("IMG4")
            self.display4.create_image(0, 0, image=self.img4, anchor=NW, tags="IMG4")
            self.display4.config(width=self.display4.winfo_width(), height=self.display4.winfo_height())
        except: pass
        
    def get_data(self, tbl):
        conn, cursor = Conn.getConn()
        sql = "SELECT * FROM %s" % (tbl)
        cursor.execute(sql)
        conn.commit()
        return cursor

        
def main_(): 
    Global.test = 1
    window = Tk()
    app = XeRa(window)
    window.mainloop()
    
if __name__ == '__main__':
    main_()