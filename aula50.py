"""
Higher Order Functions
Funções de primeira classe
"""


def saudacao(msg, nome):                    # define a função saudacao que recebe uma mensagem e um nome
    return f'{msg}, {nome}!'                # retorna a mensagem formatada com o nome


def executa(funcao, *args):                 # define a função executa que recebe uma função e argumentos
    return funcao(*args)                    # retorna a execução da função com os argumentos


print(     
    executa(saudacao, 'Bom dia', 'Luiz')  # chama a função executa com a função saudacao e os argumentos
)
print(
    executa(saudacao, 'Boa noite', 'Maria')  # chama a função executa com a função saudacao e os argumentos
)