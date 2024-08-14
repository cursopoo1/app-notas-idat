import mysql.connector


class ConexionBd():

    def __init__(self):
        self.conexion = mysql.connector.connect(host='localhost',  database='bdnotas', user='root', password='admin')
    
    def getConexionBd(self):
        return self.conexion
        