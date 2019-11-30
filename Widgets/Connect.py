import pymysql.cursors

class Conn:  
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '',                             
        db = 'qlbaixe',
        cursorclass = pymysql.cursors.DictCursor)
    print ("connect ok!!")
    
    def getConn():
        return Conn.conn, Conn.conn.cursor()