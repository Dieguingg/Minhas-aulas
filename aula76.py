
# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'strip'

if hasattr(string, metodo):   # Verifica se o objeto tem o atributo/método
    print('Existe upper')     # Se existir, pega o atributo/método
    print(getattr(string, metodo)())    # Chama o método
else:
    print('Não existe o método', metodo)
