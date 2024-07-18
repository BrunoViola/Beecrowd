import math

while True:
    try:
        entrada = input()
    except EOFError:
        break
    valores = entrada.split()
    valores = [int(valor) for valor in valores]
    
    numA = valores[0]
    numB = valores[1]
    
    soma_dos_fatoriais = math.factorial(numA) + math.factorial(numB)
    print(f"{soma_dos_fatoriais}")
    