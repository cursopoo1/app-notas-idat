from util.ConexionBd import ConexionBd

class AlumnoDao:

    def __init__(self) -> None:
        self.conexion = ConexionBd().getConexionBd()

    def listarAlumnos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT a.idalumno, a.nomalumno, a.apealumno, e.nomesp, a.proce FROM alumno a INNER JOIN especialidad e ON a.idesp = e.idesp"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def buscarAlumno(self, idalumno):
        cursor = self.conexion.cursor()
        sql = "SELECT a.idalumno, a.nomalumno, a.apealumno, e.nomesp, a.proce FROM alumno a INNER JOIN especialidad e ON a.idesp = e.idesp WHERE a.idalumno = '{}'".format(
            idalumno)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarAlumno(self, alumno):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO alumno (idalumno, nomalumno, apealumno, idesp, proce) VALUES ('{}', '{}', '{}', '{}', '{}')".format(
            alumno.idalumno, alumno.nomalumno, alumno.apealumno, alumno.idesp, alumno.proce)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
    
    def actualizarAlumno(self, alumno):
        cursor = self.conexion.cursor()
        sql = "UPDATE alumno SET nomalumno = '{}', apealumno = '{}', idesp = '{}', proce = '{}' where idalumno = '{}'".format(
            alumno.nomalumno, alumno.apealumno, alumno.idesp, alumno.proce, alumno.idalumno)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()

    def listarEspecialidades(self):
        cursor = self.conexion.cursor()
        sql = "SELECT idesp, nomesp FROM especialidad"
        cursor.execute(sql)
        return cursor.fetchall()