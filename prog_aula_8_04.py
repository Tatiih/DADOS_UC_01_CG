#4- Foi realizada uma pesquisa de algumas características físicas da população de uma certa região qual coletaram os seguintes dados referentes a cada habitante para serem analisados - sexo (masculino e feminino)- cor dos olhos (azuis, verdes ou castanhos)- cor dos cabelos (louros, castanhos, pretos)- idadeFaça um programa que determine e escreva:a) a maior idade dos habitantes;b) a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive;c) a quantidade de indivíduos que tenham olhos verdes e cabelos louros;

def main():
    maior_idade = 0
    mulheres_18_35 = 0
    olhos_verdes_cabelos_louros = 0

    while True:
        print("\n--- Cadastro de Habitante ---")

        sexo = input("Sexo (masculino/feminino): ").strip().lower()
        while sexo not in ['masculino', 'feminino']:
            sexo = input("Entrada inválida. Sexo (masculino/feminino): ").strip().lower()

        olhos = input("Cor dos olhos (azuis/verdes/castanhos): ").strip().lower()
        while olhos not in ['azuis', 'verdes', 'castanhos']:
            olhos = input("Entrada inválida. Cor dos olhos (azuis/verdes/castanhos): ").strip().lower()

        cabelos = input("Cor dos cabelos (louros/castanhos/pretos): ").strip().lower()
        while cabelos not in ['louros', 'castanhos', 'pretos']:
            cabelos = input("Entrada inválida. Cor dos cabelos (louros/castanhos/pretos): ").strip().lower()

        try:
            idade = int(input("Idade: "))
        except ValueError:
            print("Idade inválida. Cadastre este habitante novamente.")
            continue

        # Atualizações de estatísticas
        if idade > maior_idade:
            maior_idade = idade

        if sexo == 'feminino' and 18 <= idade <= 35:
            mulheres_18_35 += 1

        if olhos == 'verdes' and cabelos == 'louros':
            olhos_verdes_cabelos_louros += 1

        # Continuar?
        continuar = input("Deseja cadastrar outro habitante? (s/n): ").strip().lower()
        if continuar != 's':
            break

    # Resultados
    print("\n--- Resultados da Pesquisa ---")
    print(f"a) Maior idade dos habitantes: {maior_idade} anos")
    print(f"b) Mulheres com idade entre 18 e 35 anos: {mulheres_18_35}")
    print(f"c) Indivíduos com olhos verdes e cabelos louros: {olhos_verdes_cabelos_louros}")

if __name__ == "__main__":
    main()
