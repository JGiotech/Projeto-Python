from estoque import blusas, calcas, sapatos

#FUNÇÃO PARA EXIBIR MEUS PRODUTOS DO ARQUIVO ESTOQUE
def Exibir_Produtos(blusas, calças, sapatos):
    
    print('Lista de produtos da Loja Virtual Python:\n')

    print('--- Blusas ---')
    #blusa: é o nome temporário que você está dando para cada item da lista, durante a iteração. Você pode dar qualquer nome aqui, mas é comum usar um nome representativo.
    for blusa in blusas:
        print(blusa)

    print('\n--- Calças ---')
    for calça in calças:
        print(calça)

    print('\n--- Sapatos ---')
    for sapato in sapatos:
        print(sapato)


Exibir_Produtos(blusas, calcas, sapatos)
