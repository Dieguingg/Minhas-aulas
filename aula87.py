
# Exercício - Adiando execução de funções
"""
#meu codigo que esta errado
import time

def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, *args):
    def interna(*outros_args):
        print("A função será executada em 3 segundos...")
    time.sleep(3)  # Adia a execução por 3 segundos
    return funcao(*args, *outros_args)
    return interna

soma_com_cinco = criar_funcao(soma, 5) 
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(3))  # Deve imprimir 8
print(multiplica_por_dez(7))  # Deve imprimir 70
"""
#Explicação:
# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, *args):
    return funcao(*args)


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)
