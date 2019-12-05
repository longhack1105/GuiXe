from tkinter import *
from iconPath import path as icoPath
from Global import Global
from Obj.User import User
from Connect import Conn
import main


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
                            main.main_()
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
        