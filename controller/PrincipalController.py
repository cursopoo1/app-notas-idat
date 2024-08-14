from PyQt5 import QtWidgets, uic
from controller.AlumnoController import AlumnoController
from controller.CursoController import CursoController

class PrincipalController:

    def __init__(self):
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frmprincipal.ui")
        self.ventana.show()
        self.ventana.actionCurso.triggered.connect(self.actionCursoClick)
        self.ventana.actionAlumno.triggered.connect(self.actionAlumnoClick)
        app.exec()
    
    def actionCursoClick(self):
        self.formCurso = CursoController()
        self.formCurso.ventana.show()
    
    def actionAlumnoClick(self):
        self.formAlumno = AlumnoController()
        self.formAlumno.ventana.show()    
