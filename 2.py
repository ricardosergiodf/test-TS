anterior = 0
atual = 1

num_escolhido = int(input('Digite um numero: '))

while atual < num_escolhido:
    proximo = anterior + atual
    anterior = atual
    atual = proximo

if atual == num_escolhido or num_escolhido == 0:
    print(f"O número {num_escolhido} pertence a Fibonacci")
else:
    print(f'{num_escolhido} não pertence a Fibonacci')