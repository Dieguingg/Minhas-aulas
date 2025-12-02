from itertools import groupby
# itertools - ferramentas para trabalhar com iteradores
# groupby - agrupa elementos de um iterável com base em uma chave

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]


def ordena(aluno): # função para ordenar alunos pela nota
    return aluno['nota'] # retorna a nota do aluno


alunos_agrupados = sorted(alunos, key=ordena) # ordena a lista de alunos pela nota
grupos = groupby(alunos_agrupados, key=ordena) # agrupa os alunos pela nota
#sorted - ordena um iterável com base em uma chave
#key - função que retorna a chave para ordenação ou agrupamento
#groupby - agrupa elementos de um iterável com base em uma chave

for chave, grupo in grupos: # itera sobre os grupos de alunos
    print(chave) # imprime a chave do grupo (nota)
    for aluno in grupo: # itera sobre os alunos do grupo
        print(aluno) # imprime o aluno