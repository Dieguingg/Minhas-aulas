# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm
def recursiva(inicio=0, fim=4):  # função recursiva para contar de inicio até fim

    print(inicio, fim)  # imprime os valores atuais de inicio e fim

    # Caso base
    if inicio >= fim: # se inicio for maior ou igual a fim
        return fim # retorna fim para parar a recursão

    # Caso recursivo
    # contar até chegar ao final
    inicio += 1  # incrementa inicio em 1
    return recursiva(inicio, fim) # chama a função recursiva novamente com os novos valores


print(recursiva()) # chama a função recursiva e imprime o resultado

# recursividade - quando uma função chama a si mesma
# stack overflow - erro quando a pilha de chamadas de função excede o limite
# caso base - condição que para a recursão