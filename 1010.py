total = 0

for numero in range(1, 3):
    entrada = input()
    valores = entrada.split()
    valores = [float(valor) for valor in valores]

    quantidade = valores[1]
    valor = valores[2]
    
    total += quantidade*valor

print(f"VALOR A PAGAR: R$ {total:.2f}")
