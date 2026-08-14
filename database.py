import sqlite3
def conectar():
    conn = sqlite3.connect("escola.db")
    return conn

def criar_tabela ():
    conn = conectar()
    cursor = conn.cursor()

cursor.execute("""
create table alunos (
    id int primary key auto increment,
    nome varchar (150) not null,
    idade int not null
    nota float)

""")
conn.commit()
conn.close()