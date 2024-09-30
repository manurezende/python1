from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys
# o class cria uma classe chamada de Janela3 que inicializara tudo
class Janela3(QWidget):
    def __init__(self):
        super().__init__()
        
        # definir o texto que irá aparecer no titulo da janela
        self.setWindowTitle("cadastrar usuario")
        # definir poçisão e tamanho da janela
        self.setGeometry(15,30,500,400)
        # criar uma caixa de entrada(label)para email, senha e nivel de acesso
        self.label_usuario = QLabel("nome de usuario")
        self.label_email = QLabel("email")
        self.label_senha = QLabel("senha")
        self.label_acesso = QLabel("nivel de acesso")
        
        # criação das LinesEdits, elas vão ser as caixas de texto(onde podemos escrever)
        self.edit_usuario = QLineEdit()
        self.edit_email = QLineEdit()
        self.edit_senha = QLineEdit()
        self.edit_acesso = QLineEdit()
        
        # criar o botão
        self.botao_cad = QPushButton("cadastrar")       # botao_cad = botão de cadastro
        
        # criar o layout vertical para organizar os controles
        layout = QVBoxLayout()
        # adicionar os controles ao layout
        layout.addWidget(self.label_usuario)
        layout.addWidget(self.edit_usuario)
        
        layout.addWidget(self.label_email)
        layout.addWidget(self.edit_email)
        
        layout.addWidget(self.label_senha)
        layout.addWidget(self.edit_senha)
        
        layout.addWidget(self.label_acesso)
        layout.addWidget(self.edit_acesso)
        
        layout.addWidget(self.botao_cad)
        
        self.setLayout(layout)
        
app = QApplication(sys.argv)
janela = Janela3()
janela.show()
app.exec_()