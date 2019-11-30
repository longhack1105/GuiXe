from Connect import Conn

class LichSuGuiXe:
    def __init__(self, idGui, idCam, ngayTao, bienSo, hinhAnh, maXacNhan, trangThai, idNguoiDung, doChinhXac):
        self.idGui = idGui
        self.idCam = idCam
        self.ngayTao = ngayTao
        self.bienSo = bienSo
        self.hinhAnh = hinhAnh
        self.maXacNhan = maXacNhan
        self.trangThai = trangThai
        self.idNguoiDung = idNguoiDung
        self.doChinhXac = doChinhXac
        
    def getIdGui(self):
        return self.idGui
        
    def getIdCam(self):
        return self.idCam
        
    def getNgayTao(self):
        return self.ngayTao
        
    def getBienSo(self):
        return self.bienSo
        
    def getHinhAnh(self):
        return self.hinhAnh
        
    def getMaXacNhan(self):
        return self.maXacNhan
        
    def getTrangThai(self):
        return self.trangThai
        
    def getIdNguoiDung(self):
        return self.idNguoiDung
        
    def getDoChinhXac(self):
        return self.doChinhXac
        
    def showLichSuGuiXe(self):
        print(
            self.idGui,
            self.idCam,
            self.ngayTao,
            self.bienSo,
            self.hinhAnh,
            self.maXacNhan,
            self.trangThai,
            self.idNguoiDung,
            self.doChinhXac
        )
    '''    
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
    '''
    '''        
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
    '''        