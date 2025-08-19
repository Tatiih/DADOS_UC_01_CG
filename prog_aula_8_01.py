#Faça um programa que solicite o salário bruto de um funcionário para calcular o seu salário líquido,sabendo que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato.

#ENTRADA DE DADOS 

# Solicita o salário bruto ao usuário
salario_bruto = float(input("Digite o salário bruto do funcionário: R$ "))

# Calcula os descontos
desconto_ir = salario_bruto * 0.11   # 11% de Imposto de Renda
desconto_inss = salario_bruto * 0.08 # 8% de INSS
desconto_sindicato = salario_bruto * 0.05 # 5% de sindicato

# Calcula o salário líquido
salario_liquido = salario_bruto - (desconto_ir + desconto_inss + desconto_sindicato)

# Exibe os resultados
print("\n--- Detalhamento dos Descontos ---")
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto IR (11%): R$ {desconto_ir:.2f}")
print(f"Desconto INSS (8%): R$ {desconto_inss:.2f}")
print(f"Desconto Sindicato (5%): R$ {desconto_sindicato:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")


