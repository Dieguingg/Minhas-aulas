# count é um iterador sem fim (itertools)
from itertools import count

c1 = count(step=8, start=8)   # iterador que gera números a partir de 8, com passo 8
r1 = range(8, 100, 8)   # iterador que gera números de 8 a 100, com passo 8

print('c1', hasattr(c1, '__iter__'))   # verifica se c1 é um iterador
print('c1', hasattr(c1, '__next__'))   # verifica se c1 tem o método __next__
print('r1', hasattr(r1, '__iter__'))   # verifica se r1 é um iterador
print('r1', hasattr(r1, '__next__'))   # verifica se r1 tem o método __next__

print('count')   # imprime os valores gerados por c1
for i in c1:     # itera sobre c1
    if i >= 100: # interrompe o loop se o valor for maior ou igual a 100
        break    # sai do loop

    print(i)   # imprime o valor atual
print()   # pula uma linha
print('range')  # imprime os valores gerados por r1
for i in r1:   # itera sobre r1
    print(i)   # imprime o valor atual