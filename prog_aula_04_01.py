#Faça um Programa que pergunte em que turno você estuda. Peça para digitar:
#M - Matutino ou V - Vespertino ou N - Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o
#caso

#entrada de dados:
nome=input("informe sseu nome")
turno=('informe M- Mautino ou V- Vespertino ou N- Norturno para o seu turno:')

#saída dos dados:
if turno=='M' or turno=="m":
  print(f'Sr(a){nome}, Bom dia!')
elif turno == 'V' or turno == 'v':
  print(f'Sr(a){nome}, Boa tarde!')
elif turno== 'N'or turno =="n":
  print(f'Sr(a){nome}, Boa note!')


#Faça um Programa que peça um número correspondente a um determinado ano e em
#seguida informe se este ano é ou não bissexto.

#entrada de dados
ano=int(input('informe um ano Qualquer:'))
#saida dos dados
if ano % 4== 0:
  print(f'o ano de{ano} é bissexto.')
else:print(f'o ano de {ano} não é bissexto')


#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
#contrataram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
#baseado no salário atual:
# salários entre R$ 1280,00 e R$ 2700,00 : aumento de 15%
 #alários de R$ 3500,00 em diante : aumento de 5%
#Após o aumento ser calculado, informe na tela: o nome do funcionário, assim como o valor do aumento e
#o novo salário.

 #entrada de dados
nome=input('informe o nome do funcionário:R$')
salario= float(input(' informe o salario atual do funcionario:R$'))
 # processamento de dados 
if salario<=1280:
  percentual=0.20 
elif salario>1280 and salario<=2700:
   percetual=0.15
elif salario >2700 and salario<= 3500:
  percentual=0.10
else:
  percentual=0.05

  # Saída dos dados
print(f'Sr(a) {nome} o seu aumento será de R$ {salario * percentual}, com isso o seu novo salário será de R$ {salario + salario * percentual}')
