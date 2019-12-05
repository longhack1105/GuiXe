from tkinter import *
from iconPath import path as icoPath
from Global import Global
from Obj.User import User
from Connect import Conn
from DSTaiKhoan import DSTaiKhoan


class TaiKhoan:
    def add(self, user):
        print("Add func")
        user.showUser()
        
        conn, cursor = Conn.openConn()
        
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
        Conn.closeConn(conn)
        
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
        