import streamlit as st
import database as db

st.title("Título")
st.header("Cabeçalho")
st.subheader("Cabeçalho menor")

with st.form("nome_do_formulario"):

    nome = st.text_input("Nome")
    idade = st.number_imput("Idade"), value=50
    xuxu = st.text_imput("Cargo")
    dt_nasc = st.date_input("Data de Nascimento", value= "today")

    st.form_submit_button("Exibir abaixo")

st.write(f"O seu nome é: {nome}")
st.write(f"A sua idade é: {idade}")
st.write(f"O seu cargo é: {xuxu}")
st.write(f"A sua data de nascimento é: {dt_nasc}")
#isso aqui é o site, esses são os campos que vão aparecer no site:

#aqui temos tudo tudo que o usuário VAI VER, O QUE ELE IRÁ PREENCHER,
#O QUE ELE IRÁ CLICAR, O QUE ELE IRÁ INTERAGIR.

#cada ST é o streamlit, ou seja, o que ele irá mostrar na tela, o que
#ele vai renderizar na tela, o que ele vai EXIBIR na tela.

#um MÉTODO é aquilo que abre e fecha os parêntes, o que ele vai executar,
#rodar, fazer e processar na tela.

import streamlit as st
import database as db

db.criar_tabela()

st.title("Almoço")
st.header("Estrogonofe")
st.subheader("de carne é melhor que frango")

with st.form("form_cadastro_aluno"):

    nome = st.text_input("Nome")
    idade = st.number_input("Idade:", value=50)
    nota = st.number_input("Nota:", value= 0.0, step= 0.5, min_value= 0.0, max_value= 10.0)

    btn_form = st.form_submit_button("Enviar")

if btn_form:
    msg = db.cadastro_aluno(nome, idade, nota)
    st.warning(msg)

with st.form("form_delete_aluno"):
    id_aluno = st.number_input("ID DO ALUNO", value=0, step=1, min_value=0)
    
