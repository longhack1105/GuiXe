from tkinter import *
from MDI import *
import Pmw, sys
from PIL import Image, ImageTk
from validate_email import validate_email
from tkintertable import TableCanvas, TableModel
import tkinter as tk
from iconPath import path as icoPath
from ProgressBar import ProgressBar
from FlatButtons import FlatRadiogroup
from Tree import Tree
from Toolbar import Toolbar
import XeVao
from Connect import Conn
from Global import Global
from Obj.User import User
from XeRa import XeRa
from TaiKhoan import TaiKhoan
try:
    from tkinter import messagebox
except:
    # Python 2
    import tkMessageBox as messagebox
##







##################################################
class Main:
    def event_ctrl_h(self, event):
        self.open_tab("system")
    
    def event_ctrl_v(self, event):
        self.open_tab("xe_vao")

    def event_ctrl_space(self, event):
        self.open_tab("xe_ra")

    #def open_tab(self, path): #Gọi theo class (import xxx --> self.app = xxx.tên class(self.newWindow) )
        #self.newWindow = Toplevel(self.window)
        #if path == "system":
        #    self.app = DemoOpenTab(self.newWindow)        
        #if path == "xe_vao":
        #    self.app = DemoOpenTab(self.newWindow)        
        #if path == "xe_ra":
        #    self.app = DemoOpenTab(self.newWindow)        
        #if path == "report":
        #    self.app = DemoOpenTab(self.newWindow)
        #if path == "tai_khoan":
        #    self.app = TaiKhoan(self.newWindow)
    
    def open_tab(self, path): #Gọi trực tiếp (import xxx --> xxx() or xxx.tên def)
        if path == "system":  
            demo = self.window.newChild(title='system', iconfile=icoPath+'Parking.ico')
            tab = ChildTab(demo)
            tab.buildDemoTab()
            
        if path == "xe_vao":
            XeVao.XeVao(self.window)
            
        if path == "xe_ra":
            XeRa(self.window)
            
        if path == "report":
            demo = self.window.newChild(title='system', iconfile=icoPath+'Parking.ico')
            tab = ChildTab(demo)
            tab.buildDemoTab()
            
        if path == "tai_khoan":
            TaiKhoan(self.window)
        
        if path == "ds_tai_khoan":
            childTab = self.window.newChild(title='Danh sách tài khoản', iconfile=icoPath+'Parking.ico')
            DSTaiKhoan(window)
            
        #if path == "login":
         
    def __init__(self, window):
        self.window = window
        #window.geometry("1500x700")
        window.after_idle(lambda: window.minsize(200, 60))
        window.wm_iconbitmap(icoPath+'Parking.ico')
        window.title("Hệ thống quản lý bãi xe thông minh")
        window.geometry("%dx%d+0+0" % (window.winfo_screenwidth()-100, window.winfo_screenheight()-70))
        ##khai báo
        var = StringVar()
        
        ##check login
        if(Global.quyen == 0):
            window.destroy()
            login()
            #window.withdraw() #ẩn cửa sổ
            #window.deiconify() #tắt ẩn cửa sổ
        
        if(Global.quyen != 0):
            #window.deiconify()
            ##menu top
            menu_top = Menu(window)
            window.config(menu=menu_top)
            if(Global.quyen == 1 or Global.quyen == 2):
                subm_system = Menu(menu_top, tearoff=0)
                menu_top.add_cascade(label="Hệ thống", menu=subm_system)
                if(Global.quyen == 1):
                    subm_system.add_command(label="Hệ thống", command=lambda:self.open_tab("system"), underline=1)#system
                
                subm_system.add_command(label="Tài khoản", command=lambda:self.open_tab("tai_khoan")) #accelerator="Ctrl+Space"
                window.bind("<Control-h>", self.event_ctrl_h)
                #menu_top.add_cascade(label="Hệ thống", menu=subm_system)
            
            
            subm_manage = Menu(menu_top, tearoff=0)
            menu_top.add_cascade(label="Quản lý", menu=subm_manage)
            subm_manage.add_command(label="Làn xe vào", command=lambda:self.open_tab("xe_vao"), accelerator="Ctrl+V")
            subm_manage.add_command(label="Làn xe ra", command=lambda:self.open_tab("xe_ra"), accelerator="Ctrl+Space")
                
            #window.bind("<Control-v>", self.event_ctrl_v) 
            window.bind("<Control-v>", self.event_ctrl_v) 
            window.bind("<Control-space>", self.event_ctrl_space)
            
            if(Global.quyen == 1 or Global.quyen == 2):
                subm_report = Menu(menu_top, tearoff=0)
                menu_top.add_command(label="Báo cáo", command=lambda:self.open_tab("report"))
                #menu_top.add_cascade(label="Báo cáo", menu=subm_report)
            
            
            ##toolbar top
            #toolbar = Frame(window, bd=1, relief=FLAT)
            
            #img = Image.open(path+"phone.png")
            #img = img.resize((20, 20), Image.ANTIALIAS)
            #eimg = ImageTk.PhotoImage(img)
            #btn_phone = Button(toolbar, image=eimg, relief=FLAT, command=lambda:self.open_tab("phone"))
            #btn_phone.image = eimg
            #btn_phone.pack(side=LEFT, padx=2, pady=2)
            
            #img = Image.open(path+"pen.png")
            #img = img.resize((20, 20), Image.ANTIALIAS)
            #eimg = ImageTk.PhotoImage(img)
            #btn_pen = Button(toolbar, image=eimg, relief=FLAT, command=lambda:self.open_tab("pen"))
            #btn_pen.image = eimg
            #btn_pen.pack(side=LEFT, padx=2, pady=2)
            
            spaces = [window.topspace, window.leftspace, window.rightspace]

            toolbar_top = Toolbar(window.topspace, dockingspaces=spaces, title='')
            
            toolbar_top.sendCommand(commandname='tk', command=lambda:self.open_tab("xe_vao"))
            toolbar_top.addFlatbutton(imagefile=icoPath+'tk.gif', commandname='tk')
            
            toolbar_top.sendCommand(commandname='pen', command=lambda:self.open_tab("xe_vao"))
            toolbar_top.addFlatbutton(imagefile=icoPath+'draw.gif', commandname='pen')
        
            
            ##content
            #content = Frame(window, bg='gray', bd=1, relief=FLAT)
            
            
            ##footer
 
            #footer = Frame(window, bd=1, relief=FLAT)
            #test = "##"
            #lbl_car_num = Label(footer, textvariable=var)
            #lbl_car_num.pack(side=LEFT, padx=2, pady=2)
            #var_str = "Số xe vào: "+ test +" Số xe ra: "+ test +" Xe còn lại: "+ test
            #var.set(var_str)
            #lấy giá trị xe
            conn, cursor = Conn.openConn()
            sql = "SELECT * FROM tbllichsuguixe"
            cursor.execute(sql)
            car_in = 0
            car_out = 0
            for row in cursor:
                if(row["IdCam"] == 1):
                    car_in+=1
                if(row["IdCam"] == 2):
                    car_out+=1
            Conn.closeConn(conn)
            
            car = car_in-car_out
            var_str = "Số xe vào: "+ str(car_in) +" Số xe ra: "+ str(car_out) +" Xe còn lại: "+ str(car)
            
            teststatusbar = Label(window.statusbar, text=var_str)
            teststatusbar.pack(side='left')
            
            ##chia tỉ lệ
            #window.columnconfigure(0, weight=1) # 100% 

            #window.rowconfigure(0, weight=1) 
            #window.rowconfigure(1, weight=999) 
            #window.rowconfigure(2, weight=1)

            #toolbar.grid(row=0, sticky='news')
            #content.grid(row=1, sticky='news')
            #footer.grid(row=2, sticky='news')


#######################################################################
class Login:
    def login(self, var_name, var_pass, window):
        print('login func')       
        conn, cursor = Conn.openConn()
        sql = "SELECT * FROM tblnguoidung"
        cursor.execute(sql)
        name = var_name.get()
        passw = var_pass.get()
        if(name == "" or passw == ""):
            messagebox.showerror("Error", "Chưa nhập đủ thông tin!")
        else:
            for row in cursor:
                if(name == row['IdNguoiDung']):
                    if(passw == row['Pass']):
                        print(ord(row['TamNgung']))
                        if(ord(row['TamNgung']) == 0):
                            Global.quyen = int(row['IdQuyen'])
                            window.destroy()
                            main_()
                            error = ''
                            break
                        else:
                            error = 'Khoa' 
                            break
                    else:
                        error = 'SaiPass'
                        break
                else:
                    error = 'SaiName'
            if(error == 'SaiName'):
                messagebox.showerror("Error", "Sai tên đăng nhập!")
            if(error == 'SaiPass'):
                messagebox.showerror("Error", "Sai mật khẩu!")
            if(error == 'Khoa'):
                messagebox.showerror("Error", "Bạn bị tạm dừng hoạt động!")
        Conn.closeConn(conn)

        
    def __init__(self, window):
        self.window = window
        window.geometry("400x150")
        window.after_idle(lambda: window.minsize(window.winfo_width(), window.winfo_height()))
        window.wm_iconbitmap(icoPath+'Parking.ico')
        window.title("Login")
        
        
        ##khai báo
        var_pass = StringVar()
        var_name = StringVar()
                
        ##content
        #Name
        frame_name = Frame(window, bd=1, relief=FLAT)
        frame_name.pack(padx=20,pady=(30,5))
        
        lbl_name = Label(frame_name, text="Tên đăng nhập: ", anchor=W, width=15)
        lbl_name.pack(side=LEFT, padx=(0,5))
        
        entry_name = Entry(frame_name, textvariable=var_name, bd=2, width=25)
        entry_name.pack(side = RIGHT)
        entry_name.focus_set ()
        
        #pass
        frame_pass = Frame(window, bd=1, relief=FLAT)
        frame_pass.pack(padx=20,pady=(5,5))
        
        lbl_pass = Label(frame_pass, text="Mật khẩu: ", anchor=W, width=15)
        lbl_pass.pack(side=LEFT, padx=(0,5))
        
        entry_pass = Entry(frame_pass, textvariable=var_pass, bd=2, width=25)
        entry_pass.pack(side = RIGHT)
        
        #btn login
        frame_login = Frame(window, bd=1, relief=FLAT)
        frame_login.pack(padx=20,pady=(5,5))
        
        btn_login = Button(frame_login, text ="Login", command = lambda: self.login(var_name, var_pass, window))
        btn_login.pack()
        #window.bind('<Return>', lambda event, a = var_name, b = var_pass, c = window: self.login(a, b, c))
        window.bind('<Return>', lambda event=None: btn_login.invoke())
        
        #
        
#########################################################################
            
class ChildTab:
    def __init__(self, childTab):
        self.childTab = childTab
    def buildDemoTab(self):
        window = self.childTab.interior
        lbl = Label(window, text='demoTab')
        lbl.pack()
        self.childTab.widgetSetFocus(lbl)

        
################################################################################################### 
   

    
def center(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    
def main_(): 
    window = MDIParent(title='MDIParent')
    app = Main(window)
    center(window)
    window.mainloop()
    
def login_():
    window = Tk()
    app = Login(window)
    center(window)
    window.mainloop()
    
if __name__ == '__main__':
    login_()
    


















