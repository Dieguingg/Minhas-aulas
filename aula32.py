# Listas de Compras 
"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""




lista = []

while True:
    opcao = input('Selecione uma opção: [i]nserir, [a]pagar, [l]istar:')
    

    if opcao == 'i':
        Valor = input('Valor: ')
        lista.append(Valor)

    elif opcao == 'a':
        indice_str =(
            input('Escolha o índice para apagar: ')
        )
        try:
            indice = int(indice_str)
            del Lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        if len(lista) == 0:
            print('Nada para listar')

        for i, Valor in enumerate(lista):
            print(i, Valor)
        
    else:
        print('Por favor, escolha i, a ou l.')

# fui refazendo o codigo junto com o do professor        
# so nao estou conseguindo apagar o item da lista usando o indice


#codigo do professor
'''
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')
   
'''