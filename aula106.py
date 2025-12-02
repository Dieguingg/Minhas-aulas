# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']



# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os   #biblioteca para limpar a tela
import json  #biblioteca para trabalhar com JSON

def listar(tarefas):   #função para listar as tarefas
    print()      #pular linha
    if not tarefas:  #verifica se a lista está vazia
        print('Nenhuma tarefa para listar')  #mensagem caso a lista esteja vazia
        return  # retorna para o programa principal

    print('Tarefas:')    #  mensagem de cabeçalho
    for tarefa in tarefas:  #loop para listar as tarefas
        print(f'\t{tarefa}') #imprime cada tarefa com uma tabulação
    print()    #pular linha


def desfazer(tarefas, tarefas_refazer): #função para desfazer a última tarefa
    print()   #pular linha
    if not tarefas: #verifica se a lista está vazia
        print('Nenhuma tarefa para desfazer')  #mensagem caso a lista esteja vazia
        return # retorna para o programa principal

    tarefa = tarefas.pop()  #remove a última tarefa da lista
    print(f'{tarefa=} removida da lista de tarefas.')  #mensagem informando qual tarefa foi removida
    tarefas_refazer.append(tarefa) #adiciona a tarefa removida na lista de tarefas para refazer
    print()  #pular linha


def refazer(tarefas, tarefas_refazer): #função para refazer a última tarefa desfeita
    print() #pular linha
    if not tarefas_refazer: #verifica se a lista de tarefas para refazer está vazia
        print('Nenhuma tarefa para refazer')  #mensagem caso a lista esteja vazia
        return  # retorna para o programa principal

    tarefa = tarefas_refazer.pop() #remove a última tarefa da lista de tarefas para refazer
    print(f'{tarefa=} adicionada na lista de tarefas.') #mensagem informando qual tarefa foi adicionada
    tarefas.append(tarefa) #adiciona a tarefa removida na lista de tarefas
    print() #pular linha


def adicionar(tarefa, tarefas):  #função para adicionar uma nova tarefa
    print() #pular linha
    tarefa = tarefa.strip() #remove espaços em branco no início e no fim da string
    if not tarefa: #verifica se a string está vazia
        print('Você não digitou uma tarefa.') #mensagem caso a string esteja vazia
        return # retorna para o programa principal
    print(f'{tarefa=} adicionada na lista de tarefas.') #mensagem informando qual tarefa foi adicionada
    tarefas.append(tarefa) #adiciona a tarefa na lista de tarefas
    print() #pular linha


tarefas = [] #lista de tarefas
tarefas_refazer = [] #lista de tarefas para refazer

while True: # permanece no loop até o usuário decidir sair
    print('Comandos: listar, desfazer e refazer')  
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':  #comando para listar as tarefas
        listar(tarefas)
        continue   #volta para o início do loop
    elif tarefa == 'desfazer': #comando para desfazer a última tarefa
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':   #comando para refazer a última tarefa desfeita
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'clear':  #comando para limpar a tela
        os.system('clear')
        continue
    else:
        adicionar(tarefa, tarefas)  #adiciona uma nova tarefa
        listar(tarefas)
        continue