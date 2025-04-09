from Funcionalidades.exibir_produtos import blusas, calcas, sapatos, Exibir_Produtos

#Começando a criar a main e testando minha função para exibir produtos com menu interativo

Exibir_Produtos(blusas, calcas, sapatos)

while True:
    print("--------------------------------------------------------------")
    print("----------BEM VINDO A LOJA VIRTUAL DE ROUPAS PYSTORE----------")
    print("--------------------------------------------------------------")
    print("1 - Exibir produtos da loja")
    print("\n")
    
    opcao = input("Selecione a opção que deseja para prosseguir sua compra: ")
    
    if opcao == "1":
        Exibir_Produtos(blusas, calcas, sapatos)
        
    elif opcao == "2":
        print("encerrando o sistema")
        break
    
    voltar = input("DIGITE 'voltar' PARA VOLTAR AO MENU INICIAL: ")
    
    if voltar.lower == ("voltar"):
        break