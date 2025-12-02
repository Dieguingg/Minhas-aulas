'''Exercicios com.funções
3 # Crie ump função que multiplica todos os argumentos 
4 # não nomeados recebidos 
5 # Retorne o total para uma variável e mostre o valor
6 # da variável.

8 # Crie uma função fala se um número é par ou impar. 
9 # Retorne se o número é par ou impar.'''

def multiplicar (*args):         # args empacota os valores que enviar para a função em uma tupla
    numero = 1                   # inicializa a variavel numero com 1 para nao multiplicar por 2
    for n in args:               # percorre a tupla args
        numero *= n              # multiplica o valor de numero por n
    return numero                # retorna o valor de numero
print(multiplicar(1, 2, 3, 4, 5)) # chama a função multiplicar e imprime o resultado

def par_ou_impar(numero):                  # define a função par_ou_impar que recebe um número
    if numero % 2 == 0:                     # verifica se o número é divisível por 2 dando resto 0
        return f'O número {numero} é par'   # se for, retorna que o número é par
    return f'O número {numero} é impar'     # se não for, retorna que o número é impar
print(par_ou_impar(6))                       # chama a função par_ou_impar e imprime o resultado