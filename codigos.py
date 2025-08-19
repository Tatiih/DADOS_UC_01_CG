#Faça um programa que obtenha o valor para a variável HT (horas trabalhadas no mês), obtenha o valor
#para a variável VH (valor hora trabalhada), obtenha o valor para a variável PD (percentual de desconto) e calcule o
#salário bruto => SB = HT * VH, mais o total de desconto => TD = (PD/100)*SB e o salário líquido => SL = SB – TD.
#Apresentando ao final o Salário Liquido.
vh=float(input("informe  valor da hora trabalhada:"))
ht=float(input("informe a quantidade de horas trabalhadas"))
pd=float(input("informe o percentual de desconto:"))

#processamento de dados
sb=vh*ht
td=(pd/100)*sb
sl=td-td

#saída dos dados
print("o salário líquido é R$",sl)
      
