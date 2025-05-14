palavra = input('Digite uma palavra para ser invertida: ')
palavra_invertida = ''

tamanho_palavra = len(palavra) - 1

for i in range(tamanho_palavra, -1, -1):
    palavra_invertida += palavra[i]

print(palavra_invertida)