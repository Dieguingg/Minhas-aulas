# Exercício - sistema de perguntas e respostas


perguntas = [                # Lista de dicionários
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0     # Contador de acertos
for pergunta in perguntas:     # Itera sobre a lista de perguntas
    print('Pergunta:', pergunta['Pergunta'])   # Acessa o valor da chave 'Pergunta'
    print()  # Pula uma linha

    opcoes = pergunta['Opções']   # Acessa o valor da chave 'Opções'
    for i, opcao in enumerate(opcoes):   # Itera sobre a lista de opções com índice
        print(f'{i})', opcao)  # Mostra o índice e a opção
    print() # Pula uma linha

    escolha = input('Escolha uma opção: ')    # Recebe a escolha do usuário

    acertou = False  # Variável para verificar se acertou
    escolha_int = None  # Variável para armazenar a escolha convertida em inteiro
    qtd_opcoes = len(opcoes)  # Quantidade de opções disponíveis

    if escolha.isdigit(): # Verifica se a escolha é um número
        escolha_int = int(escolha)   # Converte a escolha para inteiro

    if escolha_int is not None:  # Verifica se a conversão foi bem-sucedida
        if escolha_int >= 0 and escolha_int < qtd_opcoes:   # Verifica se o índice está dentro do intervalo
            if opcoes[escolha_int] == pergunta['Resposta']:   # Compara a opção escolhida com a resposta correta
                acertou = True   # Marca como acertou

    print()  # Pula uma linha
    if acertou:  # Verifica se acertou
        qtd_acertos += 1   # Incrementa o contador de acertos
        print('Acertou 👍')  # Exibe mensagem de acerto
    else:
        print('Errou ❌') # Exibe mensagem de erro

    print()   # Pula uma linha


print('Você acertou', qtd_acertos)  # Exibe a quantidade de acertos
print('de', len(perguntas), 'perguntas.')   # Exibe a quantidade total de perguntas