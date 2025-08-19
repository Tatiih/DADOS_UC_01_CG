#Escreva um programa que, leia dois valores para as variáveis A e B e efetue a troca dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A.
#Apresente os valores trocados.

#entrada de dados 
a=int(input("informe um valor para variável A:"))
b=int(input("informe um valor para a variável B:"))
aux=a
a=b
b=aux
#saída dos dados 
print("o valor da variável A é:",a)
print(" o valor da variável B A é:",b)
