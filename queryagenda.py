
import sqlite3

class sqlite_db:
    def __init__(self,banco =None):
        self.conn =None
        self.curso = None
        if banco:
            self.open(banco)

    
    def open(self,banco):
        try:
            self.conn = sqlite3.connect(banco)
            self.cursor = self.conn.cursor()
            #print('acesso')
        except:
           print('invalido')       
    def creartabelas_evento(self):
        cur = self.cursor
        cur.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome text NOT NULL,idade INTEGER,cpf INTEGER,email text NOT NULL,endereco text NOT NULL,numero INTEGER,cidade text NOT NULL,bairro text NOT NULL,complemento text NOT NULL,data_n INTEGER,sexo text NOT NULL );")
    def adicionar_apaga_incluir(self,query):
         cur = self.cursor
         cur.execute(query)
         self.conn.commit()
    def pega_dados(self,query):
        cur = self.cursor
        cur.execute(query)
        return cur.fetchall()
    
#db = sqlite_db("agenda_bd.db")


#db.creartabelas_evento()
#db.cadastro()
