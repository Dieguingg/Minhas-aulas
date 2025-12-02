# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

# meu código aqui:
"""
class Carro:
    def __init__ (self, nome):
        self.nome = nome
        self.motor = None
        self.fabricante = None
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante
        



class Motor:
    def __init__ (self, nome):
        self.nome = nome

class Fabricante:
    def __init__ (self, nome):
        self.nome = nome
fabricante1 = Fabricante('Volkswagen')
motor1 = Motor('1.0')
carro1 = Carro('Gol')
carro1.motor = motor1
carro1.fabricante = fabricante1

fabricante2 = Fabricante('Honda')
motor2 = Motor('2.0')
carro2 = Carro('Civic')
carro2.motor = motor2
carro2.fabricante = fabricante2

print(f'Carro: {carro1.nome}, Motor: {carro1.motor.nome}, Fabricante: {carro1.fabricante.nome}')
print(f'Carro: {carro2.nome}, Motor: {carro2.motor.nome}, Fabricante: {carro2.fabricante.nome}')
"""

