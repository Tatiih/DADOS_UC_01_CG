#Faça um programa que leia uma temperatura em graus Celsius e apresente-a convertida emgraus Fahrenheit. A fórmula de conversão é: F = (9 * C + 160) / 5, na qual F é a temperatura emFarenhit e C é a temperatura em Celsitus

c= float(input('informe a temperatura em graus celsius:'))

#processamento de dados 
f = (9 * c + 160) / 5

#saída de dados 
print(f'A temperatura em graus fahrenheit é {f}ºF.')
