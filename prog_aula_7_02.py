#Construa um programa que armazene 10 números inteiros em um vetor. Ao final informe quantos números são pares e quantos são ímpares

#entrada de dados 

# Criar uma lista para armazenar os números
num = []

# Ler 10 números do usuário
for i in range(10):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    num.append(num)

# Inicializar contadores
pares = 0
impares = 0

# Contar pares e ímpares
for num in num:
    if num % 2 == 0:
        qtd_pares += 1
    else:
        qtd_impares += 1

# Exibir os resultados
print(f"\nQuantidade de números pares: {qtd_pares}")
print(f"Quantidade de números ímpares: {qtd_impares}")
