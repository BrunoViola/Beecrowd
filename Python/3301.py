entrada = input()

idades = entrada.split()
idades = [int(idade) for idade in idades]

idade_huguinho = idades[0]
idade_zezinho = idades[1]
idade_luisinho = idades[2]

idades.sort()

if idade_zezinho == idades[1]:
    print("zezinho")
if idade_luisinho == idades[1]:
    print("luisinho")
if idade_huguinho == idades[1]:
    print("huguinho")