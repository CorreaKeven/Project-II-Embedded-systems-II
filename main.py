# -*- coding: utf-8 -*-

from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap
import sqlite3

def func_cadastro():
    global nome, id_tag, apto, torre, hora_inicial, hora_final

    nome = janela.lineEdit_nome.text()
    apto = janela.lineEdit_apto.text()
    id_tag = janela.lineEdit_id.text()
    torre = janela.lineEdit_torre.text()
    hora_inicial = janela.lineEdit_horario_inicial.text()
    hora_final = janela.lineEdit_horario_final.text()

    print("Usuario Cadastrado => Nome: {} - Torre: {} - Apto: {} - ID: {} - Hora inicial: {} - Hora final: {} ".format(nome, torre, apto ,id_tag, hora_inicial, hora_final))

    try:
        print("Função salva dados em BD")
        conecta = sqlite3.connect("Cadastro.db")
        cursor = conecta.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Moradores(ID INTEGER, Nome TEXT, Torre TEXT, Apto TEXT, Hora_inicial INTEGER, Hora_final INTEGER)')
        cursor.execute("INSERT INTO Moradores(ID, Nome, Torre, Apto, Hora_inicial, Hora_final) VALUES(?,?,?,?,?,?)", (id_tag, nome, torre, apto, hora_inicial, hora_final))
        conecta.commit()
        print("Commit executed")
    except sqlite3.Error as error:
        print("Error while connecting to SQLite database:", error)
    finally:
        if conecta:
            conecta.close()

    
def func_monitora():
    global nome, id_tag, apto, torre, hora_inicial, hora_final

    print("Função monitora entrada/saida")
    conecta = sqlite3.connect("Cadastro.db")
    cursor = conecta.cursor()

    # Imprime todo o banco de dados.
    cursor.execute('SELECT * FROM Moradores')
    for linha in cursor.fetchall():
        print(linha)

    # Procura por um item em específico.
    cursor.execute('SELECT * FROM Moradores WHERE nome = ?', ('Aleixa',))
    # fetchone()[0] = id_tag .:. fetchone()[1] = nome .:. fetchone()[2] = apto
    row = cursor.fetchone()
    if row is not None:
        id_teste = row[0]
        print(id_teste)
        
        # Testando um ID.
        if id_teste == 123321:
            print("Usuário cadastrado")
        else:
            print("Usuário não cadastrado")
            
        id_tag = row[0]    
        nome = row[1]
        torre = row[2]
        apto = row[3]
        
        janela.lineEdit_nomeMon.setText(nome)
        janela.lineEdit_torreMon.setText(torre)
        janela.lineEdit_aptoMon.setText(str(apto))
        janela.lineEdit_id_3.setText(str(id_tag))
    else:
        print("Registro não encontrado.")
            
    conecta.close()
    
    
while True:
    app = QtWidgets.QApplication([])
    janela = uic.loadUi("telaInicialNewAstra.ui")

    #cria pela primeira vez o BD.
    conecta = sqlite3.connect("Cadastro.db")
    cursor = conecta.cursor()
    
    janela.BtnSalvar.clicked.connect(func_cadastro)
    janela.BtnMonitorar.clicked.connect(func_monitora)

    janela.show()
    app.exec_()

