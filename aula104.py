import json   # Biblioteca para trabalhar com JSON em Python

pessoa = {   # Dicionário representando uma pessoa
    'nome': 'Luiz Otávio 2',# Nome da pessoa
    'sobrenome': 'Miranda', # Sobrenome da pessoa
    'enderecos': [  # Lista de endereços da pessoa
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,  # Altura da pessoa
    'numeros_preferidos': (2, 4, 6, 8, 10),  # Números preferidos da pessoa
    'dev': True,  # Indica se a pessoa é desenvolvedora
    'nada': None,  # Campo vazio
}

with open('aula117.json', 'w', encoding='utf8') as arquivo: # Abre um arquivo para escrita em UTF-8
    json.dump( # Serializa o dicionário 'pessoa' em JSON e escreve no arquivo
        pessoa,
        arquivo,
        ensure_ascii=False, # Permite caracteres não ASCII no JSON
        indent=2, # Formata o JSON com indentação de 2 espaços
    )

with open('aula117.json', 'r', encoding='utf8') as arquivo: # Abre o arquivo para leitura em UTF-8
    pessoa = json.load(arquivo) # Desserializa o conteúdo JSON do arquivo para um dicionário Python
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'], pessoa['sobrenome'], pessoa['enderecos'])