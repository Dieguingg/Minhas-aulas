"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indice, nome in enumerate(lista): # exemplo 1
    print(indice, nome, lista[indice])

# for item in enumerate(lista): , exemplo 2
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista): , exemplo 3
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')