entrada = int(input())

anos = entrada//365
meses = (entrada - (anos*365))//30
dias = (entrada - (anos*365))%30

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")