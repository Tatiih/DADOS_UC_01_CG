## Faça um programa em que o usuário forneça 10 números inteiros compreendidos entre 1 e 100. Ao final mostre a quantidade de números pares e ímpares, assim como o menor e o maior número fornecido.

# Entrada dos dados
par = 0
impar = 0
maior = 1
menor = 100
n = 1
for i in range(5):
    while True:
        num = int(input(f'Informe o {n}º valor inteiro entre 1 e 100: '))
        if num >= 1 and num <= 100:
            n += 1
            break
        else:
            print('Verifique o Valor Fornecido')
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    if num >= maior:
        maior = num
    if num <= menor:
        menor = num
print(f'A quantidade de valores pares foi {par}')
print(f'A quantidade de valores ímpares foi {impar}')
print(f'O maior valor fornecido foi {maior}')
print(f'O menor valor fornecido foi {menor}')
