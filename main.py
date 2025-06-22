#importações
import sys
from PySide6.QtWidgets import QFileDialog, QApplication, QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import Slot

#importação modulos
from automacao import cadastro_produtos

class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cadastro de Produtos no Sistema')
        self.setGeometry(100, 100, 1000, 800)

        self.init_ui()

    def init_ui(self):
        #cria o layout
        main_layout = QVBoxLayout()

        #cria o botao
        self.btn_cadastrar = QPushButton('Cadastro de Produtos')
        self.btn_cadastrar.setFixedSize(200, 50)
        self.btn_cadastrar.clicked.connect(self.carregar_arquivo)

        #adiciona o botao no layout
        main_layout.addWidget(self.btn_cadastrar)

        main_layout.addStretch()


        #definir o layout para a janela
        self.setLayout(main_layout)

    @Slot()
    def carregar_arquivo(self):
        file_name, _ = QFileDialog.getOpenFileName( #para selecionar arquivo
            self, #parent -> janela atual
            'Selecionar Arquivo de Produtos', #titulo
            '', #diretorio atual
            'Arquivos CSV (*.csv);; Todos os Arquivos(*)' #filtro de arquivos
        )

        if file_name:
            self.cadastrar(file_name)

    @Slot()
    def cadastrar(self, file_name):
        cadastro_produtos(file_name)

# inicio da aplicação
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_window = AppWindow()
    app_window.show()
    sys.exit(app.exec())