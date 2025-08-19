# O Departamento Estadual de Meteorologia solicitou o desenvolvimento de um programa que leia conjunto indeterminado de temperaturas, ao final informe a menor e a maior temperatura, bem como a médiadelas.

def main():
    temperaturas = []

    print("Digite as temperaturas (digite 'fim' para encerrar):")

    while True:
        entrada = input("Temperatura: ")
        if entrada.lower() == 'fim':
            break
        try:
            temp = float(entrada)
            temperaturas.append(temp)
        except ValueError:
            print("Entrada inválida. Digite um número ou 'fim' para encerrar.")

    if temperaturas:
        menor = min(temperaturas)
        maior = max(temperaturas)
        media = sum(temperaturas) / len(temperaturas)

        print(f"\nMenor temperatura: {menor:.2f}°C")
        print(f"Maior temperatura: {maior:.2f}°C")
        print(f"Média das temperaturas: {media:.2f}°C")
    else:
        print("\nNenhuma temperatura foi registrada.")

if __name__ == "__main__":
    main()

