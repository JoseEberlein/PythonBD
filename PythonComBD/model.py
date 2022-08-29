import mysql.connector
from conexao import conexao

class model:
    def __init__(self):
        self.db_connection = conexao() #abrindo a conexao com o banco de dados
        self.db_connection = self.db_connection.conectar() #metodo qua realiza a conexao com o bd
        self.con = self.db_connection.cursor() #navegacao no banco de dados

    def inserir(self, nome, telefone, endereco, dataDeNascimento):
        try:
            sql = "insert into pessoa(codigo, nome, telefone, endereco, dataDeNascimento) values('', '{}', '{}', '{}', '{}')".format(nome, telefone, endereco, dataDeNascimento)
            self.con.execute(sql)
            self.db_connection.commit() #insere o dado no bd
            return "{} linha afetada".format(self.con.rowcount)
        except Exception as erro:
            return erro

    def selecionar(self):
        try:
            sql = "Select * from pessoa"
            self.con.execute(sql)
            msg = ""

            for(codigo, nome, telefone, endereco, dataDeNascimento) in self.con:
                msg = msg + "\nCodigo: {}, Nome: {}, Telefone: {}, Endereco: {}, Data de Nascimento: {}".format(codigo, nome, telefone, endereco, dataDeNascimento)
            return msg
        except Exception as erro:
            return erro
