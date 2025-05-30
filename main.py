import streamlit as st
import datetime

def main():
    st.set_page_config(page_title="Formulário de Informações", layout="centered")

    st.title("Cadastro de Informações Pessoais")
    st.markdown("Preencha o formulário abaixo para registrar seus dados.")

    # Formulário
    with st.form(key="informacoes_form"):
        nome = st.text_input("Nome completo:")
        idade = st.number_input("Idade:", min_value=0, max_value=120, value=0, step=1)
        comida_preferida = st.text_input("Comida preferida:")

        # Botão Enviar
        submit_button = st.form_submit_button(label="ENVIAR")

        if submit_button:
            if nome and idade > 0 and comida_preferida:
                salvar_informacoes(nome, idade, comida_preferida)
                st.success("Informações salvas com sucesso!")
                st.balloons() # Efeito visual de balões
            else:
                st.error("Por favor, preencha todos os campos corretamente.")

def salvar_informacoes(nome, idade, comida_preferida):
    """
    Salva as informações em um arquivo de texto.
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"informacoes_{timestamp}.txt"
    with open(nome_arquivo, "w") as f:
        f.write(f"Nome: {nome}\n")
        f.write(f"Idade: {idade}\n")
        f.write(f"Comida Preferida: {comida_preferida}\n")

if __name__ == "__main__":
    main()