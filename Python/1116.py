quantidade_pares = int(input())

for i in range (1, quantidade_pares+1):
    entrada = input()
    valores = entrada.split()
    valores = [int(valor) for valor in valores]

    dividendo = valores[0]
    divisor = valores[1]

    if divisor == 0:
        print("divisao impossivel")
    else:
        resultado = dividendo/divisor
        print(f"{resultado:.1f}")