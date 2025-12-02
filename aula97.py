from functools import partial  # para criar funções parciais
from types import GeneratorType  # para verificar se é um generator


# map - para mapear dados
def print_iter(iterator):  # função para imprimir os valores de um iterador
    print(*list(iterator), sep='\n')  # desempacota e imprime cada valor em uma nova linha
    print() # pula uma linha


produtos = [  # lista de produtos com nome e preço
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def aumentar_porcentagem(valor, porcentagem):  # função para aumentar o preço por uma porcentagem
    return round(valor * porcentagem, 2) # retorna o valor aumentado e arredondado para 2 casas decimais


aumentar_dez_porcento = partial(  # cria uma função parcial para aumentar 10%
    aumentar_porcentagem,  # função para aumentar porcentagem
    porcentagem=1.1  # fixa a porcentagem em 1.1 (10% de aumento)
)

# novos_produtos = [
#     {**p,
#         'preco': aumentar_dez_porcento(p['preco'])}
#     for p in produtos
# ]


def muda_preco_de_produtos(produto):  # função para mudar o preço do produto
    return {  # cria um novo dicionário
        **produto,  # desempacota o dicionário original
        'preco': aumentar_dez_porcento(  # aumenta o preço em 10%
            produto['preco']  # preço do produto
        )
    }


novos_produtos = list(map(   # mapeia os produtos para novos produtos com preço aumentado
    muda_preco_de_produtos,  # função para mudar o preço do produto
    produtos
))


print_iter(produtos) # imprime a lista original de produtos
print_iter(novos_produtos) # imprime a lista de produtos com preço aumentado

print( # imprime a lista de números multiplicados por 3
    list(map(
        lambda x: x * 3,
        [1, 2, 3, 4]
    ))
)

#lambda - função anônima
#map - aplica uma função a cada item de um iterável