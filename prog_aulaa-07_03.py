#- Faça um programa que verifique a quantidade de acertos de uma prova com cinco questões, sabendoque serão fornecidos pelo usuário as letras assinaladas em cada questão. Para isso será criado um vetor chamado GABARITO com as seguintes respostas: A, B, B, D, E.

# entrada de dados

# Gabarito da prova
GABARITO = ['A', 'B', 'B', 'D', 'C']

# Lista para armazenar as respostas do usuário
respostas_usuario = []

# Coleta das respostas do usuário
print("Digite as suas respostas para as 5 questões (A, B, C, D ou E):")
for i in range(5):
    resposta = input(f"Resposta da questão {i+1}: ").strip().upper()
    while resposta not in ['A', 'B', 'C', 'D', 'E']:
        print("Resposta inválida! Digite apenas A, B, C, D ou E.")
        resposta = input(f"Resposta da questão {i+1}: ").strip().upper()
    respostas_usuario.append(resposta)

# Verificação dos acertos
acertos = 0
for i in range(5):
    if respostas_usuario[i] == GABARITO[1]:
        acertos += 1

# Exibição do resultado
print(f"\nVocê acertou {acertos} questão(ões) de 5.")


