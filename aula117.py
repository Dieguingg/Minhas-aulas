# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
""""
import json   # Biblioteca para trabalhar com JSON em Python

class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

pessoa_1 = Pessoa('Luiz', 'Otávio', 30) # Cria uma instância da classe Pessoa
pessoa_2 = Pessoa('Maria', 'Oliveira', 25) # Cria outra instância da classe Pessoa
pessoa = {
    'pessoa_1': pessoa_1,
    'pessoa_2': pessoa_2
}
with open('aula117.json', 'w', encoding='utf8') as arquivo: # Abre um arquivo para escrita em UTF-8
    json.dump( # Serializa o dicionário 'pessoa' em JSON e escreve no arquivo
        pessoa,
        arquivo,
        default=lambda o: o.__dict__, # Converte objetos para dicionários
        indent=4, # Formata o JSON com indentação de 4 espaços
        ensure_ascii=False # Permite caracteres não ASCII
    )
with open('aula117.json', 'r', encoding='utf8') as arquivo: # Abre o arquivo para leitura em UTF-8
    dados = json.load(arquivo) # Carrega os dados JSON do arquivo
    print(dados) # Imprime os dados carregados
"""

import json

CAMINHO_ARQUIVO = 'aula127.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)
bd = [vars(p1), p2.__dict__, vars(p3)]


def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    print('ELE É O __main__')
    fazer_dump()