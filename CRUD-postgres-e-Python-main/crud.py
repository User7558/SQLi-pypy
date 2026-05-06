from database import conecta, encerra_conexao

"""CRUD
C= CREATE
R= READ
U= UPDATE
D = DELETE
"""

def main():

    connection = conecta()
    cursor = connection.cursor()

    # VAMOS FAZER O CREATE, USANDO O COMANDO INSERT
    # CREATE
    def insert_acoes(ticker, nome_empresa, setor, preco, data_cotacao):
        cmd_insert = "INSERT INTO acoes_b3 (ticker, nome_empresa, setor, preco, data_cotacao) VALUES (%s,%s,%s,%s,%s ); "
        values = ticker, nome_empresa, setor, preco, data_cotacao
        cursor.execute(cmd_insert, values)
        connection.commit()
        print('Dados inseridos com sucesso!')
     

    # READ
    def seleciona():
        cmd_select = "SELECT ticker, nome_empresa, setor, preco, data_cotacao FROM acoes_b3;"
        cursor.execute(cmd_select)
        acoes = cursor.fetchall()
        for acao in acoes:
            print(acao)
        return acao
    

    # update
    def atualiza(novo_preco, ticker):
        cmd_update = f"UPDATE acoes_b3 SET preco={novo_preco} WHERE ticker='{ticker}'"
        cursor.execute(cmd_update)
        connection.commit()
    

    # DELETE
    def deleta(id):
        cmd_delete = f"DELETE FROM acoes_b3 WHERE id='{id}'"
        cursor.execute(cmd_delete)
        connection.commit()
        print('Registro deletado com sucesso!!')

    selecao= 0
    while(selecao == 0):
        print("""O que gostaria de fazer?
              [0] - NADA
              [1] - INSERIR
              [2] - CONSULTAR
              [3] - DELETAR
              [4] - ALTERAR
              [5] - ENCERRAR""")
        selecao = int(input("Resposta: "))
    
    if (selecao == 1):
        ticker = input("Qual o ticker da ação: ")
        empresa = input("Qual nome da empresa: ")
        setor = input("Qual o setor da empresa: ")
        preco = input("Qual o valor da cotação atual: ")
        cotacao_data = input("Qual a data da cotação: ")

        insert_acoes(ticker, empresa, setor, preco, cotacao_data)
        #insert_acoes('CMIG4','CEMIG','Utilidade Pública', 11.06,'2024-10-22')
    elif(selecao == 2):
        seleciona()
    elif(selecao == 3):
        qual = int(input("Qual ID quer deletar? "))
        deleta(qual)
    elif(selecao == 4):
        atualiza(10.58, 'CMIG4')
    elif(selecao == 5):
        encerra_conexao(connection)

if __name__== "__main__":
    main()