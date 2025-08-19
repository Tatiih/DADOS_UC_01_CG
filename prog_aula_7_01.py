#Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá ser impressoo maior e o menor elemento do veto.

#entrada de dados 
# Inicializa a lista vazia
numeros = []

# Recebe 10 números do usuário
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

# Encontra o maior e o menor valor
maior = max(numeros)
menor = min(numeros)

# Exibe os resultados
print(f"\nMaior número: {maior}")
print(f"Menor número: {menor}")




