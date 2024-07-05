import sys


vitorias_inter = 0
vitorias_gremio = 0
empates = 0
grenais = 0

while(True):
    entrada = input()
    valores = entrada.split()

    grenais += 1

    valores = [int(valor) for valor in valores]

    inter = valores[0]
    gremio = valores[1]

    if inter>gremio:
        vitorias_inter += 1
    elif gremio>inter:
        vitorias_gremio += 1
    else:
        empates += 1
    
    print("Novo grenal (1-sim 2-nao)")
    continua = int(input())
    
    if continua == 2:
        print(f"{grenais} grenais")
        print(f"Inter:{vitorias_inter}")
        print(f"Gremio:{vitorias_gremio}")
        print(f"Empates:{empates}")
        if vitorias_inter>vitorias_gremio:
            print("Inter venceu mais")
        elif vitorias_gremio>vitorias_inter:
            print("Gremio venceu mais")

        sys.exit()
