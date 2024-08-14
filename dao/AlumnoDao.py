from util.ConexionBd import ConexionBd

class AlumnoDao:

    def __init__(self) -> None:
        self.conexion = ConexionBd().getConexionBd()

    def listarAlumnos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT a.idalumno, a.nomalumno, a.apealumno, e.nomesp, a.proce FROM alumno a INNER JOIN especialidad e ON a.idesp = e.idesp"
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