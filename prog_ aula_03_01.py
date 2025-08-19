# Escreva um programa que informe se um usário é maior ou menor de idade.

# Entrada dos dados
nome = input('Informe seu nome: ')
idade = int(input('Informe a sua idade: '))

# Saída dos dados
if idade >= 65:
    print(f'Sr(a) {nome}, você é Pertence a Terceira Idade')
elif idade >= 18:
    print(f'Sr(a) {nome}, você é Maior de Idade')
else:
    print(f'Sr(a) {nome}, você é Menor de Idade')




