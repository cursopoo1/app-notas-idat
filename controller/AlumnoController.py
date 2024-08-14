from PyQt5 import QtWidgets, uic
from dao.AlumnoDao import AlumnoDao
from PyQt5.QtWidgets import QTableWidgetItem
from model.Alumno import Alumno

class AlumnoController:

    def __init__(self):
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frmalumno.ui")
        self.alumnoDao = AlumnoDao()
        self.listarAlumnos()
        self.listarEspecialidades()
        self.listarProcedencia()
        self.ventana.show()
        app.exec()

    def listarAlumnos(self):
        listAlumnos = self.alumnoDao.listarAlumnos()
        cantidad = len(listAlumnos)
        self.ventana.tblalumnos.setRowCount(cantidad)
        fila = 0
        for objAlumno in listAlumnos:
            self.ventana.tblalumnos.setItem(fila, 0, QTableWidgetItem(objAlumno[0]))
            self.ventana.tblalumnos.setItem(fila, 1, QTableWidgetItem(objAlumno[1]))
            self.ventana.tblalumnos.setItem(fila, 2, QTableWidgetItem(objAlumno[2]))
            self.ventana.tblalumnos.setItem(fila, 3, QTableWidgetItem(objAlumno[3]))
            self.ventana.tblalumnos.setItem(fila, 4, QTableWidgetItem(objAlumno[4]))
            fila +=1

    def listarEspecialidades(self):
        listEspecialidades = self.alumnoDao.listarEspecialidades()
        for objEspecialidad in listEspecialidades:
            self.ventana.cbespecialidad.addItem(objEspecialidad[1], objEspecialidad[0])

    def listarProcedencia(self):        
        self.ventana.cbprocedencia.addItem("N")
        self.ventana.cbprocedencia.addItem("P")
