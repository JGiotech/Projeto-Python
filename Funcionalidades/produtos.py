#CRIAÇÃO DE CLASSE E HERANÇAS DOS MEUS PRODUTOS
class Produtos:
    def __init__(self, nome_produto='', preco_produto=0.0, tamanho='', tipo='', cor ='', quantidade = 0): #variavel tipo = ex casual, ex esportivo
        self.nome_produto = nome_produto
        self.preco_produto = float(preco_produto)
        self.tamanho = tamanho
        self.tipo = tipo
        self.cor = cor
        self.quantidade = int(quantidade)

    def __str__(self): #função para usar o print dentro da classe e n sair feio
        return f'Produto: {self.nome_produto} | Valor: R$ {self.preco_produto:.2f} | Tamanho: {self.tamanho} | Tipo: {self.tipo} | Cor: {self.cor} | Quantidade: {self.quantidade})'

class Blusas(Produtos):

    def __init__(self, nome_produto='', preco_produto=0, tamanho='', tipo='', cor='', material='', quantidade=0): #Isso garante que os atributos herdados da classe Produtos sejam corretamente inicializados sem precisar reescrevê-los na subclasse.
        super().__init__(nome_produto, preco_produto, tamanho, tipo, cor, quantidade) # Chama o construtor da classe pai 
        self.material = material

    def __str__(self):
        return super().__str__() + f'| Material: {self.material}'
    
class Calcas(Produtos):
    def __init__(self, nome_produto='', preco_produto=0, tamanho='', tipo='', cor='', modelo='', quantidade=0): #modelo : ex skinny, flare
        super().__init__(nome_produto, preco_produto, tamanho, tipo, cor, quantidade)
        self.modelo = modelo

    def __str__(self):
        return super().__str__() + f'| Modelo: {self.modelo}'
    
class Sapatos(Produtos):
    def __init__(self, nome_produto='', preco_produto=0, tamanho='', tipo='', cor='', estilo='', quantidade=0): #estilo : ex sapato,bota, sandalia
        super().__init__(nome_produto, preco_produto, tamanho, tipo, cor, quantidade)
        self.estilo = estilo

    def __str__(self):
        return super().__str__() + f'| Estilo: {self.estilo}'
    
   

