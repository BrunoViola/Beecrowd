from math import sqrt
import sys

entrada = input()

valores = entrada.split()
valores = [float(valor) for valor in valores]

a = valores[0]
b = valores[1]
c = valores[2]

delta = b**2 - 4*a*c

if delta < 0 or a == 0:
   print('Impossivel calcular')
   sys.exit()
elif delta == 0:
   x1 = x2 = (-b)/(2*a)
else:
   x1 = (-b+sqrt(delta))/(2*a)
   x2 = (-b-sqrt(delta))/(2*a)

print(f'R1 = {x1:.5f}')
print(f'R2 = {x2:.5f}')