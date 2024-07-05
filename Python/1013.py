entrada = input()

valores = entrada.split()

valores = [int(valor) for valor in valores]

a = valores[0]
b = valores[1]
c = valores[2]

maiorAB = (a+b+abs(a-b))/2

maiorABC = (maiorAB+c+abs(maiorAB-c))/2

print(f"{int(maiorABC)} eh o maior")