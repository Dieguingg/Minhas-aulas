from dataclasses import dataclass


@dataclass(init=False)
class Pessoa:
    nome: str
    idade: int
    sobrenome: str

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nome_completo = f'{nome} {sobrenome}'

    def __post_init__(self):
        print('POST INIT')
    
    
    
    
    
'''
    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)
'''



"""
if __name__ == '__main__':
    p1 = Pessoa('Luiz', 30, 'Miranda')
    print(p1)
    print(p1.nome_completo)

    p1.nome_completo = 'João Silva Santos'
    print(p1.nome)
    print(p1.sobrenome)
"""