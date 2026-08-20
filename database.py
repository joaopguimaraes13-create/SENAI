import sqlite3
def conectar():
    conn = sqlite3.connect("escola.db")
    return conn

def criar_tabela ():
    conn = conectar()
    cursor = conn.cursor()

cursor.execute("""
create table alunos (
    id INT PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INT NOT NULL
    nota REAL)

""")
conn.commit()
conn.close()

def cadastro_aluno(nome: str, idade, nota):

    if nome.strip() == "":
        return "O nome do aluno não pode ficar em branco. Por favor, preencha!"

    elif idade > 22:
        return "Idade acima de 22 anos"

    else:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO alunos (nome, idade, nota) values (?, ?, ?)"), (nome, idade, nota)

conn.commit()
conn.close()
return
