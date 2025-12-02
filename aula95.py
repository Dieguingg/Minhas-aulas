# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product
# itertools - ferramentas para trabalhar com iteradores
# combinations - combinações
# permutations - permutações
# product - produto cartesiano

def print_iter(iterator):   # função para imprimir os valores de um iterador
    print(*list(iterator), sep='\n')  # desempacota e imprime cada valor em uma nova linha
    print() # pula uma linha


pessoas = [ # lista de nomes de pessoas
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [ # lista de características de camisetas
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

print_iter(combinations(pessoas, 2)) # combinações de 2 pessoas
print_iter(permutations(pessoas, 2)) # permutações de 2 pessoas
print_iter(product(*camisetas)) # produto cartesiano das características das camisetas