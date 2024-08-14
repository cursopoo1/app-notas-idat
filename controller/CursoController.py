from PyQt5 import QtWidgets, uic
from dao.CursoDao import CursoDao
from model.Curso import Curso
from PyQt5.QtWidgets import QTableWidgetItem

class CursoController:

    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.objCursoDao = CursoDao()
        self.ventana = uic.loadUi("view/frmcurso.ui")
        self.ventana.tblcursos.setColumnWidth(0, 80)
        self.ventana.tblcursos.setColumnWidth(1, 220)
        self.ventana.tblcursos.setColumnWidth(2, 70)
        self.ventana.btnguardar.clicked.connect(self.btnguardarOnClick)
        self.ventana.btnnuevo.clicked.connect(self.btnnuevoOnClick)
        self.ventana.tblcursos.cellClicked.connect(self.tblCursosCellClick)
        self.ventana.show()
        self.listarCursos()
        app.exec()
    
    def tblCursosCellClick(self, fila):
        codCurso = self.ventana.tblcursos.item(fila, 0).text()
        self.ventana.txtcodcurso.setText(codCurso)
        self.ventana.txtcodcurso.setEnabled(False)
        objCurso = self.objCursoDao.buscarCurso(codCurso)
        self.ventana.txtnomcurso.setText(objCurso[1])
        self.ventana.txtcredcurso.setText(str(objCurso[2]))

    
    def btnnuevoOnClick(self):
        self.ventana.txtcodcurso.setText("")
        self.ventana.txtcodcurso.setEnabled(True)
        self.ventana.txtnomcurso.setText("")
        self.ventana.txtcredcurso.setText("")

    def btnguardarOnClick(self):
        codcurso = self.ventana.txtcodcurso.text()
        nomcurso = self.ventana.txtnomcurso.text()
        credcurso = self.ventana.txtcredcurso.text()
        nuevoCurso = Curso(codcurso, nomcurso, credcurso)
        if self.ventana.txtcodcurso.isEnabled():
            self.objCursoDao.insertarCurso(nuevoCurso)
        else:
            self.objCursoDao.actualizarCurso(nuevoCurso)
        self.listarCursos()

    
    def listarCursos(self):
        listCursos = self.objCursoDao.listarCursos()
        cantidad = len(listCursos)
        self.ventana.tblcursos.setRowCount(cantidad)
        fila = 0
        for curso in listCursos:
            self.ventana.tblcursos.setItem(fila, 0, QTableWidgetItem(curso[0]))
            self.ventana.tblcursos.setItem(fila, 1, QTableWidgetItem(curso[1]))
            self.ventana.tblcursos.setItem(fila, 2, QTableWidgetItem(str(curso[2])))
            fila +=1

    
