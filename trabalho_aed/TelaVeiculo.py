import sys
from PyQt5.QtWidgets import *
from Veiculo import Veiculo
from Carro import Carro  

class TelaVeiculo(QMainWindow):
    def __init__(self, titulo="Tela de Veículo"):
        super().__init__()
        self.setWindowTitle(titulo)
        self.setGeometry(100, 150, 300, 150)
        self.layout = QVBoxLayout()
        self.definirLayout()

        self.btnSalvar = QPushButton("Salvar", self)
        self.btnSalvar.clicked.connect(self.salvar)
        self.layout.addWidget(self.btnSalvar)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def salvar(self):
        modelo = self.txtModelo.text()
        cor = self.txtCor.text()
        if modelo != "" and cor != "" and self.cmbCategoria.currentIndex != 0:
            ano = self.txtAno.text()
            valor = None
            if ano != "":
                valor = int(ano)

            portas = self.txtPortas.text()
            vPortas = None
            if portas != "":
                vPortas = int(portas)

            cat = self.cmbCategoria.currentData()
            carro = Carro(modelo, cor, valor, vPortas, cat)  
            QMessageBox.information(self, "Carro Salvo", str(carro))

    def definirLayout(self):
        self.lblModelo = QLabel("Modelo: ")
        self.txtModelo = QLineEdit(self)

        self.lblCor = QLabel("Cor: ")        
        self.txtCor = QLineEdit(self)

        self.lblAno = QLabel("Ano: ")
        self.txtAno = QLineEdit(self)

        self.layout.addWidget(self.lblModelo)
        self.layout.addWidget(self.txtModelo)

        self.layout.addWidget(self.lblCor)   
        self.layout.addWidget(self.txtCor)   

        self.layout.addWidget(self.lblAno)
        self.layout.addWidget(self.txtAno)

