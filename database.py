import sqlite3
# Importa o SQLite pra gente conseguir mexer no banco de dados


def conectar():
# Função que abre a conexão com o banco
    conn = sqlite3.connect("escola.db")
    # Conecta no arquivo escola.db (se não existir, ele cria)
    return conn
    # Retorna a conexão


# ----- CRIANDO A TABELA -----


def criar_tabela():
# Função pra criar a tabela dos alunos
    conn = conectar()
    # Abre a conexão com o banco
    cursor = conn.cursor()
    # Cria o cursor, que é o que vai executar os comandos SQL

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos(
            ID INTEGER PRIMARY KEY AUTOINCREMENT, -- ID único que aumenta sozinho
            nome TEXT NOT NULL,                   -- Nome do aluno
            idade INTEGER NOT NULL,               -- Idade do aluno
            nota REAL                             -- Nota do aluno
        )
    """)

    conn.commit()
    # Salva a criação da tabela no banco
    conn.close()
    # Fecha a conexão


# ----- C - CREATE (Inserir aluno) -----


def criar_aluno(nome, idade, nota):
# Função que recebe os dados do aluno que vai ser cadastrado
    conn = conectar()
    # Conecta no banco
    cursor = conn.cursor()
    # Cria o cursor pra executar o comando

    cursor.execute(
        "INSERT INTO alunos(nome, idade, nota) VALUES (?, ?, ?)",
        (nome, idade, nota),
    )
    # Coloca os dados recebidos dentro da tabela

    conn.commit()
    # Salva o novo aluno no banco
    conn.close()
    # Fecha a conexão


# ----- R - READ (Buscar/Exibir aluno) -----


def buscar_aluno(nome):
# Função pra procurar um aluno pelo nome
    conn = conectar()
    # Conecta no banco
    cursor = conn.cursor()
    # Cria o cursor

    cursor.execute("SELECT * FROM alunos WHERE nome = ?", (nome,))
    # Procura na tabela o aluno com o nome informado

    alunos = cursor.fetchall()
    # Pega todos os resultados encontrados

    conn.close()
    # Fecha a conexão
    return alunos
    # Retorna os alunos encontrados


# ----- U - UPDATE (Editar aluno) -----


def editar_aluno(id, nome, idade, nota):
# Função pra editar os dados de um aluno que já está cadastrado
    conn = conectar()
    # Conecta no banco
    cursor = conn.cursor()
    # Cria o cursor

    cursor.execute(
        """
        UPDATE alunos
        SET nome = ?, idade = ?, nota = ?
        WHERE ID = ?
    """,
        (nome, idade, nota, id),
    )
    # Atualiza os dados do aluno usando o ID dele

    conn.commit()
    # Salva as alterações
    conn.close()
    # Fecha a conexão


# ----- D - DELETE (Apagar aluno) -----


def deletar_aluno(id):
# Função pra apagar um aluno chato pra cacete usando o ID
    conn = conectar()
    # Conecta no banco
    cursor = conn.cursor()
    # Cria o cursor

    cursor.execute("DELETE FROM alunos WHERE ID = ?", (id,))
    # Apaga o aluno que tiver aquele ID

    conn.commit()
    # Confirma a exclusão no banco
    conn.close()
    # Fecha a conexão
