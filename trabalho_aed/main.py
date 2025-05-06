import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QComboBox, QMessageBox
)

from categoria import Categoria
from desktop import Desktop
from notebook import Notebook

class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Produtos")
        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout()

        self.modelo_input = QLineEdit()
        self.cor_input = QLineEdit()
        self.preco_input = QLineEdit()
        self.categoria_input = QLineEdit()
        self.tipo_combo = QComboBox()
        self.extra_input = QLineEdit()
        self.cadastrar_btn = QPushButton("Cadastrar")

        self.tipo_combo.addItems(["Desktop", "Notebook"])

        layout.addWidget(QLabel("Modelo:"))
        layout.addWidget(self.modelo_input)

        layout.addWidget(QLabel("Cor:"))
        layout.addWidget(self.cor_input)

        layout.addWidget(QLabel("Preço:"))
        layout.addWidget(self.preco_input)

        layout.addWidget(QLabel("Categoria:"))
        layout.addWidget(self.categoria_input)

        layout.addWidget(QLabel("Tipo de Produto:"))
        layout.addWidget(self.tipo_combo)

        layout.addWidget(QLabel("Potência da Fonte (Desktop) ou Tempo de Bateria (Notebook):"))
        layout.addWidget(self.extra_input)

        layout.addWidget(self.cadastrar_btn)

        self.cadastrar_btn.clicked.connect(self.cadastrar_produto)

        self.setLayout(layout)

    def cadastrar_produto(self):
        try:
            modelo = self.modelo_input.text()
            cor = self.cor_input.text()
            preco = float(self.preco_input.text())
            categoria = Categoria(1, self.categoria_input.text())
            extra = self.extra_input.text()
            tipo = self.tipo_combo.currentText()

            if tipo == "Desktop":
                produto = Desktop(modelo, cor, preco, categoria, extra)
            else:
                produto = Notebook(modelo, cor, preco, categoria, extra)

            produto.cadastrar()
            QMessageBox.information(self, "Produto Cadastrado", produto.getInformacoes())
            self.limpar_campos()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro: {str(e)}")

    def limpar_campos(self):
        self.modelo_input.clear()
        self.cor_input.clear()
        self.preco_input.clear()
        self.categoria_input.clear()
        self.extra_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Interface()
    janela.show()
    sys.exit(app.exec_())
