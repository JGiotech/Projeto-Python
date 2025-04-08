
from produtos import Blusas, Calcas, Sapatos

blusa1 = Blusas('Blusa cropped feminina', 65.90, 'M, P e G', 'casual', 'preta', 'Algodão', 8,)
blusa2 = Blusas('Blusa Estampada masculina', 78.49, 'M e G', 'praiana', 'colorida', 'Esportiva', 5)
blusa3 = Blusas('Blusa Social feminina e masculina', 149.99, 'M, G, P', 'social', 'azul e preta', 'Seda', 10)
blusa4 = Blusas('Blusa lisa unisex', 55.90, 'GG, M, G, P, PP','casual', 'azul, branca, vermelha, preta', 'Algodão', 20)

calça1 = Calcas('Calça jeans feminina e masculina', 120.00, 'P, M, G', 'casual', 'azul', 'Jeans', 10)
calça2 = Calcas('Calça moletom masculina', 98.90, 'M, G, GG', 'esportiva', 'cinza', 'Moletom', 7)
calça3 = Calcas('Calça social unisex', 140.00, 'P, M, G, GG', 'social', 'preta', 'Poliéster', 12)
calça4 = Calcas('Calça legging feminina', 75.50, 'PP, P, M, G', 'fitness', 'preta e cinza', 'Elastano', 15)

sapato1 = Sapatos('Tênis esportivo masculino e feminino', 210.00, '39, 40, 41, 42', 'esportivo', 'preto e vermelho', 'Sintético', 6)
sapato2 = Sapatos('Sandália rasteira feminina', 89.90, '35, 36, 37, 38, 39', 'casual', 'bege', 'Couro', 10)
sapato3 = Sapatos('Sapato social masculino', 299.90, '39, 40, 41, 42, 43', 'social', 'preto', 'Couro legítimo', 4)
sapato4 = Sapatos('Bota cano curto unisex', 259.00, '36, 37, 38, 39, 40, 41', 'casual', 'marrom', 'Camurça', 8)

blusas = [blusa1, blusa2, blusa3, blusa4]
calcas = [calça1, calça2, calça3, calça4]
sapatos = [sapato1, sapato2, sapato3, sapato4]

#criei o arquivo ESTOQUE para guardar todas as instâncias dos produtos (meus objetos)

#OBS: Falta criar agora o controle do estoque 