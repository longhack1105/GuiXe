import pymysql.cursors

class Conn:  
    def openConn():

        conn = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = '',                             
            db = 'qlbaixe',
            cursorclass = pymysql.cursors.DictCursor)
        print ("connect ok!!")
        return conn, conn.cursor()
            
    def closeConn(conn):
        try:
            conn.close()
            print ("close connect ok!!")
        except:
            print('close conn false')