import math

entrada = input()

valores = entrada.split()
valores = [int(valor) for valor in valores]

a = valores[0]
b = valores[1]
c = valores[2]

s = (a+b+c)/2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(f"{area:.3f} m2")