pi = 3.14159

entrada = input()

valores = entrada.split()
valores = [float(valor) for valor in valores]

a = valores[0]
b = valores[1]
c = valores[2]

area_triangulo_retangulo = (a*c)/2

area_circulo = pi * c**2

area_trapezio = ((a+b)*c)/2

area_quadrado = b**2

area_retangulo = a * b

print(f"TRIANGULO: {area_triangulo_retangulo:.3f}")
print(f"CIRCULO: {area_circulo:.3f}")
print(f"TRAPEZIO: {area_trapezio:.3f}")
print(f"QUADRADO: {area_quadrado:.3f}")
print(f"RETANGULO: {area_retangulo:.3f}")