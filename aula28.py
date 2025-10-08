'''
Exercicio
Exiba os indices da lista
Maria
Helena
Luiz


lista = ['Maria', 'Helena', 'Luiz']
for nome in lista:
    print(lista.index(nome), nome)
    '''
#ou 
"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
# essa foi a forma que o professor fez no video
# porem a minha forma tambem esta correta!!