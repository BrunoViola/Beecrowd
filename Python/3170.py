bolinhas = int(input())
galhos = int(input())

if galhos%2==0:
    qtd_bolinhas_faltantes = (galhos/2) - bolinhas
else:
    qtd_bolinhas_faltantes = (galhos-1)/2 - bolinhas
    
if qtd_bolinhas_faltantes>0:
    print(f"Faltam {int(qtd_bolinhas_faltantes)} bolinha(s)")
else:
    print("Amelia tem todas bolinhas!")