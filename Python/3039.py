carrinhos = 0
bonecas = 0
numero_criancas = int(input())

for i in range(numero_criancas):
    entrada = input().split()
    sexo = entrada[1]
    if sexo == 'M':
        carrinhos += 1
    else:
        bonecas += 1

print(f"{carrinhos} carrinhos\n{bonecas} bonecas")
