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
        self.ventana.tblalumnos.cellClicked.connect(self.tblAlumnosCellClick)
        self.ventana.btnnuevo.clicked.connect(self.nuevoFormularioAlumno)
        self.ventana.show()
        app.exec()
    
    def nuevoFormularioAlumno(self):
        self.ventana.txtcodigo.setText("")
        self.ventana.txtcodigo.setEnabled(True)
        self.ventana.txtnombres.setText("")
        self.ventana.txtapellidos.setText("")
        self.ventana.cbespecialidad.setCurrentIndex(0)
        self.ventana.cbprocedencia.setCurrentIndex(0)        
    
    def tblAlumnosCellClick(self, fila):
        codAlumno = self.ventana.tblalumnos.item(fila, 0).text()
        self.ventana.txtcodigo.setText(codAlumno)
        self.ventana.txtcodigo.setEnabled(False)
        objAlumno = self.alumnoDao.buscarAlumno(codAlumno)
        self.ventana.txtnombres.setText(objAlumno[1])
        self.ventana.txtapellidos.setText(objAlumno[2])
        self.ventana.cbespecialidad.setCurrentText(objAlumno[3])
        self.ventana.cbprocedencia.setCurrentText(objAlumno[4]) 

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
