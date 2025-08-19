#Faça um programa que receba do usuário o nome e a idade de 10 pessoas. Ao finalmostre a soma e a média das idades.

# entrada d dados
for i in range(10):
    nome=input('informe seu nome')
idade=int(input('informe suaidade:'))

soma=soma+idade
#saida de dados
media=soma/(i+1)
print(f'a soma das idades foi{soma}anos')
print(f'a media das iddes foi{media:.1f}anos.')