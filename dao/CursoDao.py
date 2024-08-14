from util.ConexionBd import ConexionBd

class CursoDao:

    def __init__(self):
        self.conexion = ConexionBd().getConexionBd()
    
    def listarCursos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT idcurso, nomcurso, credito FROM curso order by IdCurso DESC"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def buscarCurso(self, codcurso):
        cursor = self.conexion.cursor()
        sql = "SELECT idcurso, nomcurso, credito FROM curso WHERE idcurso = '{}'".format(
            codcurso)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarCurso(self, curso):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO curso VALUES ('{}', '{}', '{}')".format(curso.codcurso,
                                                                   curso.nomcurso,
                                                                   curso.credcurso)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
    
    def actualizarCurso(self, curso):
        cursor = self.conexion.cursor()
        sql = "UPDATE curso SET nomcurso = '{}', credito = '{}' where idcurso = '{}'".format(curso.nomcurso,
                                                                   curso.credcurso,
                                                                   curso.codcurso)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()

        
