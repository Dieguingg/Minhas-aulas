# Exemplo de uso dos sets
letras = set() # Cria um set vazio
while True:  
    letra = input('Digite: ') # Solicita ao usuário que digite uma letra
    letras.add(letra.lower()) # Adiciona a letra ao set em minúsculo

    if 'l' in letras: # Verifica se a letra 'l' está no set
        print('PARABÉNS') 
        break

    print(letras) # Exibe o conteúdo atual do set