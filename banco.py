import sqlite3
import pandas as pd

class Banco:
    def creat_table():
        banco = sqlite3.connect('bancoDeDados.db')
        cursor = banco.cursor()
        cursor.execute("""
            CREATE TABLE bolao (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    jogador TEXT NOT NULL,
                    criado_em DATE NOT NULL,
                    arquivo TEXT NOT NULL,
                    n1 id INTEGER NOT NULL,
                    n2 id INTEGER NOT NULL,
                    n3 id INTEGER NOT NULL,
                    n4 id INTEGER NOT NULL,
                    n5 id INTEGER NOT NULL,
                    n6 id INTEGER NOT NULL 
                                );
                    """)
        banco.close()
    
    def insert_data(jogador:str,data:str,arquivo:str,n1:int,n2:int,n3:int,n4:int,n5:int,n6:int):
        banco = sqlite3.connect('bancoDeDados.db')
        cursor = banco.cursor()
        cursor.execute(f"""INSERT INTO bolao (jogador, criado_em,arquivo, n1,n2,n3,n4,n5,n6)
        VALUES ('{jogador}', '{data}', '{arquivo}', '{n1}','{n2}','{n3}','{n4}','{n5}','{n6}')""")
        banco.commit()
        banco.close()
    
    def read_data():
        banco = sqlite3.connect('bancoDeDados.db')
        cursor = banco.cursor()
        resultado = cursor.execute("SELECT * FROM bolao").fetchall()
        banco.close()
        tabela = pd.DataFrame(resultado,columns=['id','jogador','data','arquivo','n1','n2','n3','n4','n5','n6'])
        return tabela.head(len(resultado))



