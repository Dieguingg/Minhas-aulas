# Variáveis livres + nonlocal (locals, globals)
# print(globals())
# def fora(x):
#     a = x

#     def dentro():
#         # print(locals())

#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())
def concatenar(string_inicial):   # função que concatena strings
    valor_final = string_inicial  # variável local da função concatenar

    def interna(valor_a_concatenar=''): # função interna que concatena strings
        nonlocal valor_final  # declara que valor_final é uma variável não local
        valor_final += valor_a_concatenar # concatena a string passada com a variável não local
        return valor_final  # retorna o valor final
    return interna  # retorna a função interna


c = concatenar('a') # cria uma função que concatena strings começando com 'a'
print(c('b')) # concatena 'b' com 'a' e imprime 'ab'
print(c('c')) # concatena 'c' com 'ab' e imprime 'abc'
print(c('d')) # concatena 'd' com 'abc' e imprime 'abcd'
final = c() # chama a função interna sem argumentos
print(final) # imprime 'abcd'