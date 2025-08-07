entrada = input()
entrada = entrada.split()

valores = [int(valor) for valor in entrada]

numero_tomadas = sum(valores) - 3

print (numero_tomadas) 