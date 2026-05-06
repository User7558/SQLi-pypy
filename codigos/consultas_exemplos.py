from database import conecta, encerra_conexao


def main():
    connection = conecta()
    cursor = connection.cursor()

    # DEMONSTRAÇÃO DO TRATAMENTO INSEGURO E SEGURO DE CONSULTAS SQL
    def consulta_paciente():
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")


        print("\n------ CONSULTA INSEGURA ------")

        sql = f"""
        SELECT id, nome, endereco
        FROM pacientes
        WHERE email = '{email}' AND senha = '{senha}';"""

        print("\nSQL executado:")
        print(sql)
        print('\n')

        cursor.execute(sql)
        resultado = cursor.fetchall()

        if resultado:
            print("Login realizado.")
            for r in resultado:
                print(r)
        else:
            print("Credenciais inválidas.")



        print("\n------ CONSULTA SEGURA ------")

        sql = """
        SELECT id, nome, endereco
        FROM pacientes
        WHERE email = %s AND senha = %s;"""

        cursor.execute(sql, (email, senha))
        resultado = cursor.fetchall()

        if resultado:
            print("Login realizado.")
            for r in resultado:
                print(r)
        else:
            print("Credenciais inválidas.")
        print('\n')
        

    # MENU DE SELEÇÃO DO PROGRAMA
    selecao = ''
    while (selecao != '0'):
        print("""O que gostaria de fazer?
              [0] - SAIR
              [1] - CONSULTAR PACIENTE""")
        selecao = input("Selecionado: ")

        if(selecao == '1'):
            consulta_paciente()
        elif(selecao != '0'):
            print("Escolha uma opção válida \n")

    #encerrando a conexão
    encerra_conexao(connection)

if __name__== "__main__":
    main()