# Escreva um programa que, dado 5 números inteiros calcule a soma deles e apresente o resultado ao final.

# Entrada dos dados
soma = 0

# Processamento dos dados
for i in range(5):
    num = int(input('Informe um Número: '))
    soma = soma + num

# Saída dos dados
print(f'O Resultado da Soma é {soma}')
