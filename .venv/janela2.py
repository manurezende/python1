# importação da biblioteca grafica PyQt5
# importar os controles(QtWidgets) para a biblioteca gafrica
# neste exemplo usamos o comando import com o * para importar todos os controles da biblioteca
from PyQt5.QtWidgets import *
# importação da biblioteca de sistema para abrir e fechar a janela que sera construida
# ao abrir e fechar a janela tambem estarmos retirando-a da memoria
import sys

from PyQt5.QtWidgets import QWidget
# criação da estrutura geral da nossa janela
# a janela e seus controles estão sendo criadas de forma agrupadas dentro de uma classe
# a classe Janela2 esta herdando todasas configurações estruturais de uma tela normal
# clase QWidget está classe define os botões: minimizar,maximizar e fechar
# alem de aprese4ntar um titulo para a janela
class Janela2(QWidget):
    # o comando de (definition->definição) define uma função.
    # nesse caso estamos definindo a função de inicialização da classe
    # init(__init__) esta função realiza o start(coloca para funcionar)a classe janela dois
    # na função init passamos como parametro o comando self 
    # ele indica a classe que teremos controle que devem ser usados por ela
    # portanto todo controle que está com o prefixo self faz referencia a propria classe
    # ex: self.label_nome = Qlabel : isso indica para a classe janela 2
    # que a label para o nome pertence a ela assim como os demais controles
    
    def __init__(self):
        super().__init__()
        # adicionar um texto ao titulo a janela, o self olha para si e fala que este comando faz parte da classe Janela2
        self.setWindowTitle("janela de cadastro")
        # configurar tamanho e posição
        # o primeiro valor é a posição x medida em pixel
        # o segundo valor é a posição y medida em pixel
        # o terceiro valor é a largura(width) medida em pixel
        # o quarto valor é a altura(height) medida em pixel
        self.setGeometry(500,200,500,250)
        
        # adicionar uma label a janela 
        # uma label (rotulo) é um texto que é apresentado em uma janela para indicar oque deve ser feito
        # ela irá apresentar o texto "nome completo" isso india que ele deve escrever
        # geralmente ela é usada em combinação a uma caixa de texto(QLineEdit)
        self.label_nome = QLabel ("nome completo: ")
        
        
        # para alterar o estilo do texto usamos os comandos de css
        # color             -> cor da letra
        # font-size         -> tamanho da letra
        # font-weight       -> peso da fonte (negrito = bold)
        # text-transform    -> altera a altura da letra
                            # UpperCase   -> maiuscula
                            # LowerCase   -> minuscula 
                            # Capitalize  -> primeira letra de cada palavra maiucula             
        self.label_nome.setStyleSheet("QLabel{color:#ff0000; font-size:12pt; font-weight:bold; text-transform:upperCase}")
        
        
        self.label_email = QLabel ("email: ")
        self.label_cpf = QLabel ("cpf: ")
        self.label_sexo = QLabel ("sexo: ")
        self.label_idade = QLabel ("idade: ")
        
        # adicionar uma caixa de texto usada para o usuario ter uma interção com a label1'
        self.edit_nome = QLineEdit()
        
        # backgroud-color -> cor de fundo
        # padding         -> margem interna
        # border-radius   -> arredondar os cantos
        self.edit_nome.setStyleSheet("QLineEdit{background-color:#999999; color:#fff; padding:10px; border-radius:10px}")
        
        
        
        self.edit_email = QLineEdit()
        self.edit_cpf = QLineEdit()
        
        # declaração combobox = caixa de texto com opções
        self.combo_sexo = QComboBox()
        self.combo_idade = QComboBox()
        
        # criar uma lista com 2 sexos
        lista_sexo = ["masculino", "femenino"]
        # adicionar a lista a combo
        self.combo_sexo.addItems(lista_sexo)
        
        # criar uma lista para idade que vai de 16 a 100
        lista_idade = []
        # para popular(colocar varios dados em um determinado local) a caixa(combobox) da idade com valores de 16 até 100
        # estamos usando uma estrutura de repetição, que faz uma contagem de 16 a 101 com o comando range
        # durante a contagem cada numero é convertido para string, pois o combobox só aceita valores em texto
        for i in range(16,101):
            lista_idade.append(str(i))
            
        self.combo_idade.addItems(lista_idade)
        
        # adicionar layout para organizar os elementos
        # estamos usando o gerenciador de layout vertical(QVBoxLayout)
        # ele é usado para organizar os comandos que vão aparecer na janela2
        # ele foi utilizado para exibie um abaixo do outro 
        # para exibir um do lado do outro usamos (QHBoxLayout)
        layout = QVBoxLayout()
        
        # para adiciona a label_nome e o edit_nome ao organizador(layout)vertical
        # usamos o comando add(adicionar) Widgets(controle)
        # assim os controles irão aparecer um abaixo do outro por estar na vertical
        layout.addWidget(self.label_nome)
        layout.addWidget(self.edit_nome)
        
        layout.addWidget(self.label_email)
        layout.addWidget(self.edit_email) 

        layout.addWidget(self.label_cpf)
        layout.addWidget(self.edit_cpf) 
        
        layout.addWidget(self.label_sexo)
        layout.addWidget(self.combo_sexo)     
        
        layout.addWidget(self.label_idade)
        layout.addWidget(self.combo_idade)           
        
        # adicionae o layout a tela
        self.setLayout(layout)
        
app = QApplication(sys.argv)
# inicia a tela, ou  seja carrega a janela em memoria
jan = Janela2()
# exibe a janela em tela
jan.show()
# o comando app.exec_ executa os comandos acima e gerencia o botão de fechar para retirar a janela
app.exec_()
        