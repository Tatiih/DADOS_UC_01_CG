#Faça um programa que pergunte a uma pessoa, a sua idade, o seu peso e quanto dormiu
#nas últimas 24 h e diga se ela pode doar ou não sangue de acordo com as seguintes condições:
 #Ter entre 16 e 69 anos.
#Pesar mais de 50 kg.
#Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas)
#Escreva um programa que, dados 3 números inteiros (n1, n2 e n3), diga qual deles é maior.

idade=int(input("digite sua idade:"))
peso=int(input("digite seu peso:"))
horas_dormidas=int(input("Quantas horas você dormiu nas ultimas 24 horas"))

if idade>=16 and idade<=69 and peso>50 and horas_dormidas>= 6:print("você pode doar sangue") 
else: print("você não pode doar sangue")