# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)



import copy # importa o modulo copy para fazer cópias profundas
novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.10, 2)}  # esse codigo aumenta o preco em 10%
    for produto in produtos
]
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos), key=lambda x: x['nome'], reverse=True   # ordena do maior para o menor
)
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos), key=lambda x: x['preco']   # ordena do menor para o maior
)
print('Novos Produtos com Preço Aumentado:')  # imprime os novos produtos com preço aumentado
print(*novos_produtos, sep='\n')


print('\nProdutos Ordenados por Nome (Decrescente):')  # imprime os produtos ordenados por nome
print(*produtos_ordenados_por_nome, sep='\n')


print('\nProdutos Ordenados por Preço (Crescente):')  # imprime os produtos ordenados por preço
print(*produtos_ordenados_por_preco, sep='\n')



""" o professor deu uma dica para criar um modulo
 usando a lista de produtos, codigo do professor:
https://github.com/luizomf/cursopython2023/commit/3cde6551f47fe3fdc92c5df296ea954b09d0c953"""


