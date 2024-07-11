# 1.Álcool 2.Gasolina 3.Diesel 4.Fim
import sys

opcao_combustivel, alcool, gasolina, diesel = 0, 0, 0, 0

while opcao_combustivel != 4:
    opcao_combustivel = int(input())
    if opcao_combustivel == 1:
        alcool+=1
    elif opcao_combustivel == 2:
        gasolina+=1
    elif opcao_combustivel == 3:
        diesel+=1
    elif opcao_combustivel == 4:
        print(f"MUITO OBRIGADO\nAlcool: {alcool}\nGasolina: {gasolina}\nDiesel: {diesel}")
        sys.exit()