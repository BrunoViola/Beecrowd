import math

primeira_linha = input()
segunda_linha = input()

p1 = primeira_linha.split()
p1 = [float(coordenada) for coordenada in p1]

p2 = segunda_linha.split()
p2 = [float (coordenada) for coordenada in p2]

x1 = p1[0]
y1 = p1[1]

x2 = p2[0]
y2 = p2[1]

distancia = math.sqrt((x2-x1)**2+(y2-y1)**2)

print(f"{distancia:.4f}")