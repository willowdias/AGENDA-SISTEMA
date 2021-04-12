from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QComboBox, QMainWindow, QWidget, QLabel, QLineEdit
import sys
from PyQt5.QtCore import QSize  
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QFormLayout, QLineEdit, QMessageBox, QPushButton, QTableWidgetItem
from reportlab.pdfgen import canvas
from PyQt5.QtGui import QFont, QIntValidator, QPixmap,QIcon
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import inch, cm
from queryagenda import sqlite_db
class agenda(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(agenda, self).__init__()
        uic.loadUi('AGENDA.ui', self)
        self.show()
    
        ###############lineedit#####apaga
        self.linewillow = QLineEdit(self)        
        self.linewillow.setMaxLength(4)
        self.linewillow.move(20, 230)
        self.linewillow.resize(40, 20)
        self.linewillow.setStyleSheet("background-color: rgb(2, 85, 117,0);color: rgb(255, 0, 0);")
        
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('ID')
        self.nameLabel.resize(10, 20)
        self.nameLabel.move(10, 230)#nome do campo id
        self.nameLabel.setStyleSheet("background-color: rgb(2, 85, 117,0);color: rgb(255, 0, 0);")
        
        #################################                               
        ###########cadsatro de clientes###########
        self.lineEdit_cpf.setInputMask("000.000.000.00;_")#cpf               
        self.lineEdit_celular_tel.setInputMask("00000000000")#celular
        self.lineEdit_data_nascimento.setInputMask("00/00/0000")#dada nascimento
        self.lineEdit_idade.setValidator(QtGui.QIntValidator())#idade
        self.lineEdit_numero.setValidator(QtGui.QIntValidator())#numero 
        self.lineEdit_apaga_cliente.setValidator(QtGui.QIntValidator())#ID_APAGA CLIENTE
        self.linewillow.setValidator(QtGui.QIntValidator())#ID_APAGA CLIENTE  
        self.lineEdit.setValidator(QtGui.QIntValidator())#numero interio
        #############################################
        #icone
        self.setWindowIcon(QIcon("Agenda/icon/icone_inical2.png"))
        #
        self.ver_usuario_cliente()#mostra clientes
        #cadastro cliente####################################
        self.Button_apagar.clicked.connect(self.apaga_clienter)
        self.Button_salva.clicked.connect(self.cadastro_cliente)
        ########################################################
        #alera#######
        self.checkBox.toggled.connect(self.check_alerta)
        ################################################

        ############################################################
        self.actionclaro.triggered.connect(self.claro)
        self.actionescuro.triggered.connect(self.escuro)
        #data time
        #self.dateEdit.dateChanged.connect(self.data)#data
        #self.timeEdit.timeChanged.connect(self.horas)#horas
        self.pushButton_confirma.clicked.connect(self.horas)
        self.pushButton_confirma.clicked.connect(self.data)
     #### #####################
        self.pushButton_confirma.clicked.connect(self.tipodetecnico)
        self.pushButton_confirma.clicked.connect(self.atendimneto) 
        self.comboxprofissao_t()
        #self.combo_atendimento.activated.connect(self.atendimneto)
        #self.combo_profissao.activated.connect(self.tipodetecnico)
     ######PAGINA######
        self.actionCadastro_atendimento.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.atendimento))
        self.actionCadastro_Client.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.cadastrocliente))   
    ########combobox#########
    def atendimneto(self):
        a=str(self.combo_atendimento.currentText())
        self.listWidget_dados.addItem(a) 
        self.textBrowser_atendimento.setText(a)
    def tipodetecnico(self):
        text = str(self.combo_profissao.currentText())
        self.listWidget_dados.addItem(f'Tecnico: {text} ')
        self.textBrowser_profissao.setText(text)    
    def comboxprofissao_t(self):#item da lista
        profissao=["","tecnico","analista","GERENTE"]

        self.combo_profissao.addItems(profissao)
        self.combo_atendimento.addItems(profissao)   
    
    ###########combox########################
    #data time
    def data(self):#data
        value =self.dateEdit.date()
        self.listWidget_dados.addItem(('Dia {0}/ Mês {1}/ Ano {2}  '.format(value.day(), value.month(), value.year()))) 
        self.textEdi_data.setText(('Dia {0}/ Mês {1}/ Ano {2}  '.format(value.day(), value.month(), value.year()))) 
    def horas(self):#horas  
        hora = self.timeEdit.time()                  
        self.textEdi_hora.setText(('Horas {0}:{1} Minutos'.format(hora.hour(),hora.minute())))
        self.listWidget_dados.addItem(('Dados Cliente\n'+'Horas {0}:{1} Minutos'.format(hora.hour(),hora.minute())))
    #salva###############################
    def salvar_Dados(self):
        text=self.listWidget_dados.selectedItems()
        for y in text:
            print(y.text())
    def check_alerta(self):#alerta cliente agendado
        import time, sys
        bt=self.sender()
        buttonReply=QMessageBox.question(self, 'ALERTA', "CLIENTE ESPECIAL", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply==QMessageBox.Yes:        
            if bt.isChecked() == True:
                print('bom dia')  
        else:
            print('Verdade')   
        
    ####################TEMA##################
    def claro(self): 
        self.frame_2_escuro.close()
        self.frame_2_claro.show()
        self.frame_escuro.close()
        self.frame_claro.show()
    def escuro(self):
        self.frame_2_escuro.show()
        self.frame_2_claro.close()
        self.frame_escuro.show()
        self.frame_claro.close()
    ###########################################   
    
    #######cadastro cliente####
    def cadastro_cliente(self):
        db = sqlite_db("agenda_bd.db")
        cliente=str(self.lineEdit_nome.text())
        idade_idade=str(self.lineEdit_idade.text()) 
        cpf_cpf=str(self.lineEdit_cpf.text())
        email_email=str(self.lineEdit_email.text())
        end_endereco=str(self.lineEdit_endereco.text())
        numer_n=str(self.lineEdit_numero.text())
        cidade_cid=str(self.lineEdit_cidade.text())
        bairro_bairro=str(self.lineEdit_bairro.text())
        completento_cop=str(self.lineEdit_complemento.text())
        data_nc=str(self.lineEdit_data_nascimento.text())
        sexo_sexo = str(self.comboBox_sexo.currentText())
        if (cliente==""or idade_idade=="" or cpf_cpf=="" or email_email==""or end_endereco=="" or numer_n==""or
        cidade_cid==""or bairro_bairro==""or completento_cop==""or data_nc==""or sexo_sexo==""):
        
            return QMessageBox.about(self, "Title", "PREENCHAR OS DADOS")
        else:
            buttonReply=QMessageBox.question(self, 'CADASTRO CLIENTE', "DESEJA CADASTRA CLIENTE", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply==QMessageBox.Yes:  
                db.adicionar_apaga_incluir("INSERT INTO  clientes (nome,idade,cpf,email,endereco,numero,cidade,bairro,complemento,data_n,sexo)VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(cliente,idade_idade,cpf_cpf,email_email,end_endereco,numer_n,cidade_cid,bairro_bairro,completento_cop,data_nc,sexo_sexo))
                QMessageBox.about(self, "Title", "USUARIO CADASTRO COM SUCESSO")
                self.ver_usuario_cliente()
            if buttonReply==QMessageBox.Yes:
                
                #x posicao y=direcao 400=tamanho 695 posicao
                ##########cabeçalho do pdf################
                logo = ImageReader('offsistema.png')#logo                
                pdf = canvas.Canvas('{}.pdf'.format("OFF SISTEMA"))
                pdf.drawImage(logo, 400, 700,5*cm, 5*cm)#logo                
                pdf.drawString(35,724,'='*20+ 'Dados cliente  '+'='*20)
                pdf.drawString(35,750,'='*20+'OFF SISTEMA'+'='*20)  
                ########corpo do pdf 
                pdf.drawString(30,680, f'Cliente: {cliente} Idade: {idade_idade} Cpf: {cpf_cpf} ')
                pdf.line(30,675,580,675)#linha cliente
                pdf.drawString(30,665,f'Email: {email_email} End: {end_endereco} Nº {numer_n} Cidade {cidade_cid}')
                pdf.line(30,660,580,660)#llinha email
                pdf.drawString(30,650, f'Bairro: {bairro_bairro} Completo: {completento_cop} data nascimento: {data_nc} Tipo sexo: {sexo_sexo}')
                pdf.line(30,645,580,645)#linha bairro
                pdf.save()               
                
                QMessageBox.about(self, "Title", "PDF GERADO COM SUECESSO")
            else:
                print('Erro ao gerar {}.pdf'.format("brasil"))
                QMessageBox.about(self, "Title", "processo cancelado")
    #######################################################################################################
    def ver_usuario_cliente(self):
        db = sqlite_db("agenda_bd.db")
        try:    
            dados_lidos=db.pega_dados("SELECT * FROM clientes")
            self.tableWidget_clientes.setRowCount(0)
            self.tableWidget_clientes.resizeColumnToContents(0)
            for linha, dados in enumerate (dados_lidos):
                self.tableWidget_clientes.insertRow(linha)
                for coluna_n, dados in enumerate(dados):
                    self.tableWidget_clientes.setItem(linha,coluna_n,QTableWidgetItem(str(dados)))
        except:
            print()
    ###################apaga clientes###########
    def apaga_clienter(self):#apaga cliente tela cadastro clientes       
        
        db = sqlite_db("agenda_bd.db")
        
        id=self.linewillow.text()
     
        if id=="":
            self.nameLabel.show()
            self.linewillow.show()               
            QMessageBox.about(self, "Title", "DESEJA CLIENTE PRENCHA ID?")
               
                
        elif id==self.linewillow.text():                         
            db.adicionar_apaga_incluir("DELETE FROM clientes WHERE id={}".format(id))
            QMessageBox.about(self, "Title", "USUARIO APAGADO COM SUCESSO")
            self.ver_usuario_cliente()
            self.linewillow.setText("")
            self.linewillow.close() 
            self.nameLabel.close()   
            
        
    ####################################################################################################### 

    
    
        
        
    
if __name__ == '__main__':
        
    app = QtWidgets.QApplication([])
    window = agenda()
    sys.exit(app.exec_())