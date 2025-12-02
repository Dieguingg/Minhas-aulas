"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

# meu codigo
def soma_listas(lista_a, lista_b):   # função que soma os valores de duas listas
    tamanho_menor = min(len(lista_a), len(lista_b))   # encontra o tamanho da menor lista
    nova_lista = []  # cria uma nova lista vazia
    for i in range(tamanho_menor):  # percorre o índice até o tamanho da menor lista
        nova_lista.append(lista_a[i] + lista_b[i])   # soma os valores das duas listas e adiciona na nova lista
    return nova_lista  # retorna a nova lista
lista_a = [1, 2, 3, 4, 5, 6, 7]  # primeira lista
lista_b = [1, 2, 3, 4]  # segunda lista
resultado = soma_listas(lista_a, lista_b)  # chama a função e armazena o resultado
print(resultado)  # imprime o resultado
"""

# codigo do professor

lista_soma  = [2, 4, 6, 8]

lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)

lista_soma = []
for i in range(len(lista_b)):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)

lista_soma = []
for i, _ in enumerate(lista_b):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)