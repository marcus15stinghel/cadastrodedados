import streamlit as st

# Título
st.title('Cadastro de dados')



with st.form('cadastro', clear_on_submit=True):

    #E-mail
    email = st.text_input('Informe seu E-mail', value='').strip()

    # Nome
    nome = st.text_input('Informe seu nome completo', value='').strip()

    cont_nome = len(nome)
    if cont_nome <= 3:
        if nome:
            st.write('O nome informado é muito pequeno!\n')

    # Idade
    idade = st.number_input('Informe sua idade: ', step=1, min_value=0, max_value=150)

    if idade < 0 or idade > 150:
        if idade:
            st.write('Informe uma idade válida!\n')

    # Salário
    salario = st.number_input('Informe o seu salário mensal: ', min_value=0)

    if salario < 0:
        if salario:
            st.write('Digite um valor válido!\n')

    # Sexo
    sexo = st.selectbox('Informe seu sexo:', ('', 'Masculino', 'Feminino'), 0)

    # Estado Civil
    civil = st.selectbox('Informe seu estado civil:', ('', 'Solteiro(a)', 'Casado(a)', 'Divorciado(a)', 'Viuvo(a)'), 0)

    # Finalização
    button = st.form_submit_button('Salvar')

save = []
save.append(email)

if button:

    button2 = st.button('Novo usuário', help='Clique para adicionar mais um usuário')

    st.write('\n\nSeus dados foram registrados com sucesso!\n')
    st.write(f'Nome: {nome}')
    st.write(f'Idade: {idade}')
    st.write(f'Salário: {salario}')
    st.write(f'Sexo: {sexo}')
    st.write(f'Estado civil: {civil}')

    with open(fr'Arquivos\{nome}.txt', 'w') as txt:
        txt.write(f'{nome} \n{idade} \n{salario} \n{sexo} \n{civil}')


    #Envio de e-mail
    import smtplib
    import email.message

    def enviar_email():
        corpo = f"""
    <p>Seus seguintes dados foram registrados com sucesso: </p>
    <p>     Nome: {nome}</p>
    <p>     Idade: {idade}</p>
    <p>     Salário: {salario}</p>
    <p>     Sexo: {sexo}</p>
    <p>     Civíl: {civil}</p>
    """

        msg = email.message.Message()
        msg['Subject'] = f"Olá {nome}! Obrigado por se cadastrar!"
        msg['From'] = 'spiral.marcas@gmail.com'
        msg['To'] = save[0]
        password = 'tesmurhmuflmdils'
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

    enviar_email()

