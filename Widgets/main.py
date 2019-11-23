from tkinter import *
from MDI import *
import Pmw, sys
from PIL import Image, ImageTk
import pymysql.cursors
from validate_email import validate_email
from tkintertable import TableCanvas, TableModel
import tkinter as tk
from iconPath import path as icoPath
from ProgressBar import ProgressBar
from FlatButtons import FlatRadiogroup
from Tree import Tree
from Toolbar import Toolbar
import xeVao

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
            xeVao.XeVao(self.window)
            
        if path == "xe_ra":
            demo = self.window.newChild(title='system', iconfile=icoPath+'Parking.ico')
            tab = ChildTab(demo)
            tab.buildDemoTab()
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
            conn, cursor = Conn.conn, Conn.conn.cursor()
            sql = "SELECT * FROM tbllichsuguixe"
            cursor.execute(sql)
            car_in = 0
            car_out = 0
            for row in cursor:
                if(row["IdCam"] == 1):
                    car_in+=1
                if(row["IdCam"] == 2):
                    car_out+=1
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
        conn, cursor = Conn.conn, Conn.conn.cursor()
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
class TaiKhoan:
    def add(self, user):
        print("Add func")
        user.showUser()
        
        conn, cursor = Conn.conn, Conn.conn.cursor() 
        
        #print(user.isValueEmail())
        #print(user.isValuephone())
        
        if(user.isNull()):
            messagebox.showerror("Error", "Chưa nhập đủ thông tin!")
        elif(user.isLoopIdNguoiDung()):
            messagebox.showerror("Error", "Tên đăng nhập đã tồn tại!")
        elif(user.isValueEmail() == False): 
            messagebox.showerror("Error", "Email không hợp lệ!")
        elif(user.isValuephone() == False):
            messagebox.showerror("Error", "Số điện thoại không hợp lệ!")
        else:
            #format_str = """INSERT INTO tblnguoidung(IdNguoiDung, Pass, HoDem, Ten, DienThoai, Email, IdQuyen, TamNgung) VALUES ( "{v1}", "{v2}", "{v3}", "{v4}", "{v5}", "{v6}", {v7}, {v8})"""
            #sql = format_str.format(v1=user.getIdNguoiDung(), v2=user.getPassw(), v3=user.getHoDem()
            #, v4=user.getTen(), v5=user.getDienThoai(), v6=user.getEmail(), v7=user.getIdQuyen(), v8=user.getTamNgung())
            sql = "INSERT INTO tblnguoidung(IdNguoiDung, Pass, HoDem, Ten, DienThoai, Email, IdQuyen, TamNgung) "\
                + "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (user.getIdNguoiDung(), user.getPassw(), user.getHoDem()
                , user.getTen(), user.getDienThoai(), user.getEmail(), user.getIdQuyen()
                , user.getTamNgung()))
            conn.commit()
            messagebox.showinfo("Infor", "Thêm tài khoản thành công")
        
    def open_tab(self, path):
        print("danh sách tài khoản func")
        if(path == 'ds_tai_khoan'):
            DSTaiKhoan(self.window)
        
    def __init__(self, window):
        self.window = window
        childTab = window.newChild(title='Tài khoản', iconfile=icoPath+'Parking.ico')
        childTab.setSize(leftPos=20, rightPos=420, topPos=20, bottomPos=390)#("400x370+100+100")
        childFrame = childTab.interior
        #window.after_idle(lambda: window.minsize(window.winfo_width(), window.winfo_height()))
        #window.wm_iconbitmap(icoPath+'Parking.ico')
        #window.title("Tài khoản")
        
        ##khai báo
        var_name = StringVar()
        var_pass = StringVar()
        var_fname = StringVar()
        var_lname = StringVar()
        var_phone = StringVar()
        var_email = StringVar()
        var_quyen = StringVar()
        var_tamngung = StringVar()
        
        frm_main = Frame(childFrame)
        frm_main.pack(fill='both', expand=1)
        
        ##edit
        frm_edit = LabelFrame(frm_main, text="Nhập thông tin")
        frm_edit.pack(padx=5, pady=5, fill='both', expand=1)
        
        #IdNguoiDung
        frm_id = Frame(frm_edit, bd=1, relief=FLAT)
        frm_id.pack(pady=(20,5), padx=20)
        
        lbl_name = Label(frm_id, text="Tên đăng nhập: ", anchor=W, width=15)
        lbl_name.pack(side=LEFT, padx=(0,5))
        
        entry_name = Entry(frm_id, textvariable=var_name, bd=2, width=30)
        entry_name.pack(side = RIGHT)
        
        #pass
        frm_pass = Frame(frm_edit, bd=1, relief=FLAT)
        frm_pass.pack(pady=(5,5))
        
        lbl_pass = Label(frm_pass, text="Mật khẩu: ", anchor=W, width=15)
        lbl_pass.pack(side=LEFT, padx=(0,5))
        
        entry_pass = Entry(frm_pass, textvariable=var_pass, bd=2, width=30)
        entry_pass.pack(side = RIGHT)
        
        #name
        frm_name = Frame(frm_edit, bd=1, relief=FLAT)
        frm_name.pack(pady=(5,5))
        
        lbl_name = Label(frm_name, text="Họ tên: ", anchor=W, width=15)
        lbl_name.pack(side=LEFT, padx=(0,5))
          
        entry_lname = Entry(frm_name, textvariable=var_lname, bd=2, width=10)
        entry_lname.pack(side = RIGHT)
        entry_lname.insert(0, 'Tên')
        
        entry_fname = Entry(frm_name, textvariable=var_fname, bd=2, width=19)
        entry_fname.pack(side = RIGHT)
        entry_fname.insert(0, 'Họ đệm')
        
        #phone
        frm_phone = Frame(frm_edit, bd=1, relief=FLAT)
        frm_phone.pack(pady=(5,5))
        
        lbl_phone = Label(frm_phone, text="Số điện thoại: ", anchor=W, width=15)
        lbl_phone.pack(side=LEFT, padx=(0,5))
        
        entry_phone = Entry(frm_phone, textvariable=var_phone, bd=2, width=30)
        entry_phone.pack(side = RIGHT)
                
        #email
        frm_email = Frame(frm_edit, bd=1, relief=FLAT)
        frm_email.pack(pady=(5,5))
        
        lbl_email = Label(frm_email, text="Email: ", anchor=W, width=15)
        lbl_email.pack(side=LEFT, padx=(0,5))
        
        entry_email = Entry(frm_email, textvariable=var_email, bd=2, width=30)
        entry_email.pack(side = RIGHT)
        
        #quyền
        frm_quyen = Frame(frm_edit, bd=1, relief=FLAT)
        frm_quyen.pack(pady=(5,5))
        
        lbl_quyen = Label(frm_quyen, text="Quyền: ", anchor=W, width=15)
        lbl_quyen.pack(side=LEFT, padx=(0,5))
        if(Global.quyen == 1):
            dict_quyen = {"Nhân viên": 3, "Quản lý":2, "Admin":1}
        else:
            dict_quyen = {"Nhân viên": 3, "Quản lý":2}
        lst_quyen = list(dict_quyen.values())
        lst_quyen_key = list(dict_quyen.keys())
        
        drlst_quyen = OptionMenu(frm_quyen, var_quyen, *lst_quyen_key)
        var_quyen.set(lst_quyen_key[0])
        drlst_quyen.config(width=10)
        drlst_quyen.pack(side = RIGHT, padx=(0, 81))
        
        #tam ngung
        frm_tamngung = Frame(frm_edit, bd=1, relief=FLAT)
        frm_tamngung.pack(pady=(5,5))
        
        lbl_tamngung = Label(frm_tamngung, text="Trạng thái: ", anchor=W, width=15)
        lbl_tamngung.pack(side=LEFT, padx=(0,5))
        
        dict_tamngung = {"Tạm ngưng": 1, "Hoạt động": 0}
        lst_tamngung = list(dict_tamngung.values())
        lst_tamngung_key = list(dict_tamngung.keys())
        
        drlst_tamngung = OptionMenu(frm_tamngung, var_tamngung, *lst_tamngung_key)
        var_tamngung.set(lst_tamngung_key[0])
        drlst_tamngung.config(width=10)
        drlst_tamngung.pack(side = RIGHT, padx=(0, 81))
        
        ##func
        frm_btn = Frame(frm_edit)
        frm_btn.pack(pady=10, fill='y')
        
        if(Global.quyen == 1 or Global.quyen == 2):
            btn_ds = Button(frm_btn, text ="Danh sách TK", width=10, command = lambda: self.open_tab('ds_tai_khoan'))
            btn_ds.pack(side=LEFT, pady=(5, 5), padx=25)
        
        btn_add = Button(frm_btn, text ="Thêm TK ->", width=10, 
            command = lambda: self.add(user = User(
                var_name.get(), 
                var_pass.get(), 
                var_fname.get(), 
                var_lname.get(),
                var_phone.get(), 
                var_email.get(), 
                dict_quyen[var_quyen.get()], 
                dict_tamngung[var_tamngung.get()]
            ))
        )
        btn_add.pack(side=LEFT, pady=(5, 5), padx=25)
        childFrame.bind('<Return>', lambda event=None: btn_add.invoke())
        
        
        
#########################################################################################
class DSTaiKhoan: 
       
    def fix(self, data_user):
        err = False
        print('fix fuc')
        print(data_user)
        
        conn, cursor = Conn.conn, Conn.conn.cursor()
        
        
        try:
            sql = "DELETE FROM tblnguoidung"
            cursor.execute(sql)
            conn.commit()
            
            for user in data_user.values():
                print(str(user['TamNgung']))
                if(str(user['TamNgung']) == "" or str(user['TamNgung']) == '0'):
                    tamNgung = 0
                elif(ord(user['TamNgung']) == 0):
                    tamNgung = 0
                else:
                    tamNgung = 1
                    
                sql = "INSERT INTO tblnguoidung(IdNguoiDung, Pass, HoDem, Ten, DienThoai, Email, IdQuyen, TamNgung) "\
                    + "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (user['IdNguoiDung'], user['Pass'], user['HoDem']
                    , user['Ten'], user['DienThoai'], user['Email'], user['IdQuyen']
                    , tamNgung))
                conn.commit()
        except:
            messagebox.showerror("Error", "#01 data in data user have error")                
       
    def print_cell(self, event):
            print(table.currentrow, table.currentcol)
            
    def makeDirectionary(self):
        user_dict = {}
        ##lấy data
        conn, cursor = Conn.conn, Conn.conn.cursor()
        sql = "SELECT * FROM tblnguoidung"
        cursor.execute(sql)
        i=0
        for row in cursor:
            user_dict[str(i)] = {'IdNguoiDung':row['IdNguoiDung'], 'Pass':row['Pass'], 'HoDem':row['HoDem'], 'Ten':row['Ten'],
                                'DienThoai':row['DienThoai'], 'Email':row['Email'], 'IdQuyen':row['IdQuyen'], 'TamNgung':row['TamNgung']}
            i+=1
        return user_dict
    def __init__(self, window):
        childTab = window.newChild(title='Danh sách tài khoản', iconfile=icoPath+'Parking.ico')
        childTab.setSize(leftPos=20, rightPos=800, topPos=20, bottomPos=420)#("400x370+100+100")
        childFrame = childTab.interior
        #window.after_idle(lambda: window.minsize(window.winfo_width(), window.winfo_height()))
        #window.wm_iconbitmap(path+'Parking.ico')
        #window.title("danh sách tài khoản")
        #window.after_idle(lambda: window.maxsize(780, 500))

        ##data
        user_dict = self.makeDirectionary()
        ##tạo bảng
        table_frame = Frame(childFrame)
        table_frame.pack(side=TOP)
        table = TableCanvas(table_frame,
                width=780,
                maxheight=400,
                data=user_dict,
                showkeynamesinheader=True,
                read_only=False,
                cellwidth=75,
                editable=True,
                thefont=("Arial", 10),
                currentrow=-1,
                leftclick_only=True,
                header_selection=False,
                multirow_selection=False,
                cell_selection=True)

        table.bind("<Double-1>", self.print_cell)
        table.grid(row=0, column=0, sticky=NW+SE)
        table.show()
        table.redraw()
        #getdatafix
        data_user = table.model.data
        #btn
        frm_btn = Frame(childFrame)
        frm_btn.pack(side=BOTTOM)
        
        btn_fix = Button(frm_btn, text='Cập nhập dữ liệu',command=lambda:self.fix(data_user))
        btn_fix.pack(pady=10)
        table.redraw()
        
        
        
#################################################################################################################
class User:
    def __init__(self, idNguoiDung, passw, hoDem, ten, dienThoai, email, idQuyen, tamNgung):
        self.idNguoiDung = idNguoiDung
        self.passw = passw
        self.hoDem = hoDem
        self.ten = ten
        self.dienThoai = dienThoai
        self.email = email
        self.idQuyen = idQuyen
        self.tamNgung = tamNgung
    
    def getIdNguoiDung(self):
        return self.idNguoiDung
        
    def getPassw(self):
        return self.passw
        
    def getHoDem(self):
        return self.hoDem
        
    def getTen(self):
        return self.ten
        
    def getDienThoai(self):
        return self.dienThoai
        
    def getEmail(self):
        return self.email
        
    def getIdQuyen(self):
        return self.idQuyen
        
    def getTamNgung(self):
        return self.tamNgung
        
    def showUser(self):
        print(
            self.idNguoiDung,
            self.passw,
            self.hoDem,
            self.ten,
            self.dienThoai,
            self.email,
            self.idQuyen,
            self.tamNgung
        )
    def isNull(self):
        if(
            self.idNguoiDung == "" or
            self.passw == "" or
            self.hoDem == "" or
            self.ten == "" or
            self.dienThoai == "" or
            self.email == ""
        ):
            return True
        else:
            return False
            
    def isLoopIdNguoiDung(self):
        conn, cursor = Conn.conn, Conn.conn.cursor() 
        sql = "SELECT * FROM tblnguoidung"
        cursor.execute(sql)
        for row in cursor:
            if(self.idNguoiDung == row['IdNguoiDung']):
                return True
                break
            else:
                return False
                break
    
    def isValueEmail(self):
        return validate_email(self.email)
        
    def isValuephone(self):
        if len(self.dienThoai) != 10 and len(self.dienThoai) != 11 and len(self.dienThoai) != 12 :
            return False
        elif self.dienThoai.isdigit():
            return True
        else:
            return False
            
            
##################################################################################################
            
class ChildTab:
    def __init__(self, childTab):
        self.childTab = childTab
    def buildDemoTab(self):
        window = self.childTab.interior
        lbl = Label(window, text='demoTab')
        lbl.pack()
        self.childTab.widgetSetFocus(lbl)
        
        
        
        
################################################################################################### 
   
class Global:
    quyen = 0
    
    
class Conn:  
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '',                             
        db = 'qlbaixe',
        cursorclass = pymysql.cursors.DictCursor)
    print ("connect ok!!")
    
    
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
    


















