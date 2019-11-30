from Connect import Conn
from validate_email import validate_email

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
            