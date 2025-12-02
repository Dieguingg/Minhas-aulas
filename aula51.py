"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):         # Função que cria uma saudação personalizada
    def saudar(nome):         # Função interna que usa a saudação personalizada
        return f'{saudacao}, {nome}!'       # Retorna a saudação completa
    return saudar     # Retorna a função interna


falar_bom_dia = criar_saudacao('Bom dia')     # Cria uma função de saudação para "Bom dia"
falar_boa_noite = criar_saudacao('Boa noite')     # Cria uma função de saudação para "Boa noite"

for nome in ['Maria', 'Joana', 'Luiz']:    #  Lista de nomes para saudar
    print(falar_bom_dia(nome))     # Usa a função de saudação para "Bom dia"
    print(falar_boa_noite(nome))     # Usa a função de saudação para "Boa noite"