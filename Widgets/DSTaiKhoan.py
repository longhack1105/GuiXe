from tkinter import *
from iconPath import path as icoPath
from Global import Global
from Obj.User import User
from Connect import Conn
from tkintertable import TableCanvas, TableModel


class DSTaiKhoan: 
       
    def fix(self, data_user):
        err = False
        print('fix fuc')
        #print(data_user)
        
        conn, cursor = Conn.openConn()
        try:
            sql = "DELETE FROM tblnguoidung"
            cursor.execute(sql)
            conn.commit()
            
            for user in data_user.values():
                #print(str(user['TamNgung']))
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
        Conn.closeConn(conn)
       
    def print_cell(self, event):
            print(table.currentrow, table.currentcol)
            
    def makeDirectionary(self):
        user_dict = {}
        ##lấy data
        conn, cursor = Conn.openConn()
        sql = "SELECT * FROM tblnguoidung"
        cursor.execute(sql)
        i=0
        for row in cursor:
            user_dict[str(i)] = {'IdNguoiDung':row['IdNguoiDung'], 'Pass':row['Pass'], 'HoDem':row['HoDem'], 'Ten':row['Ten'],
                                'DienThoai':row['DienThoai'], 'Email':row['Email'], 'IdQuyen':row['IdQuyen'], 'TamNgung':row['TamNgung']}
            i+=1
        Conn.closeConn(conn)
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