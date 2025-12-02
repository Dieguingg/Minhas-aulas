"""
 eu vou fazer um codigo que du´lica um valor, triplica um valor e quadruplica um valor o numero recebido do parâmetro
"""

"""
def multiplicar (*args):         # args empacota os valores que enviar para a função em uma tupla
    numero = 2                   # inicializa a variavel numero com 1 para nao multiplicar por 2
    for n in args:               # percorre a tupla args
        numero *= n              # multiplica o valor de numero por n
    return numero                # retorna o valor de numero
print(multiplicar(2))       # multiplica por 2
print(multiplicar(3))      # multiplica por 3 
print(multiplicar(4))     # multiplica por 4
"""

def criar_multiplicador (multiplicador):    # função que cria uma função que multiplica um valor pelo multiplicador
    def multiplicar (numero):               # função interna que multiplica o valor recebido pelo multiplicador
        return numero * multiplicador       # retorna o valor multiplicado
    return multiplicar         # retorna a função interna
duplicar = criar_multiplicador(2)          # cria a função que multiplica por 2
triplicar = criar_multiplicador(3)         # cria a função que multiplica por 3
quaduplicar = criar_multiplicador(4)       # cria a função que multiplica por 4

print (duplicar(2))        # chama a função que multiplica por 2
print (triplicar(2))       # chama a função que multiplica por 3
print (quaduplicar(2))    # chama a função que multiplica por 4
