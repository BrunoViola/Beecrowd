entrada = int(input())

dias = entrada//60//60
minutos = (entrada - (dias*60*60))//60
segundos = entrada - (dias*60*60) - minutos*60

print(f"{dias}:{minutos}:{segundos}")
