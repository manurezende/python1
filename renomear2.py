import os
# para criar uma função em python iremos usar o comando def(definição)
def mudar_nome(ar_or, nv_ar): 
    """
    a função mudar_nome altera o nome do arquivo. 
    o usuario deve fornecer o nome original e o novo nome 
    args:
        ar_or(str): o nome original do arquivo
        nv_ar(str): o novo nome do arquivo
    return:
        retorna uma mensagem para o usuario saber sobre a ação
    """
    os.rename (ar_or, nv_ar)
    msg = "o nome do arquivo foi alterado"
    return msg

arquivo_original = input("Digite o nome do arquivo que sera renomeado: ")
novo_arquivo = input("digite o novo nome do arquivo: ") 

rs = mudar_nome(arquivo_original, novo_arquivo)
print(rs)