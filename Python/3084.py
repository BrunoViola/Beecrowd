import sys

for line in sys.stdin:
    try:
        entrada = line.split()
        entrada = [int(valor) for valor in entrada] 
        hora = entrada[0]//30
        minuto = entrada[1]//6
    
        if hora<10:
            if minuto<10:
                print(f"0{hora}:0{minuto}")
            else:
                print(f"0{hora}:{minuto}")
        
        else:
            if minuto<10:
                print(f"{hora}:0{minuto}")
            else:
                print(f"{hora}:{minuto}")
    except EOFError:
        sys.exit()
    
    