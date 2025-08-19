#Faça um programa que calcule a media de um aluno composto por três notas. Ao final mostre o nome do aluno e sua respectiva media
nome_aluno=input("digite o nome do aluno:")
nota1=float(input("digite a primeira nota:"))
nota2=float(input("digite a segunda nota:"))
nota3=float(input("digite a terceira nota:"))

#processo de dados 
media=(nota1+nota2+nota3) /3

# saída de dados
print(f"o nome do aluno{nome_aluno}obtevea media{media: .2f}")
# saída de dados 
print(f"o nome do aluno {nome_aluno} obteve a media
{media:.2f}")
# saída de dados