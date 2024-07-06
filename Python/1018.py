nota_de_100, nota_de_50, nota_de_20, nota_de_10, nota_de_5, nota_de_2, nota_de_1 = 0, 0, 0, 0, 0, 0, 0

n = int(input())
total=n

while n>=100:
    n = n-100
    nota_de_100 = nota_de_100+1
while n>=50:
    n = n-50
    nota_de_50 = nota_de_50+1
while n>=20:
    n = n-20
    nota_de_20 = nota_de_20+1

while n>=10:
    n = n-10
    nota_de_10 = nota_de_10+1
while n>=5:
    n = n-5
    nota_de_5 = nota_de_5+1
    
while (n>=2):
    n = n-2
    nota_de_2 = nota_de_2+1

while n>=1:
    n = n-1
    nota_de_1 = nota_de_1+1
    
print(f"{total}\n{nota_de_100} nota(s) de R$ 100,00\n{nota_de_50} nota(s) de R$ 50,00\n{nota_de_20} nota(s) de R$ 20,00\n{nota_de_10} nota(s) de R$ 10,00\n{nota_de_5} nota(s) de R$ 5,00\n{nota_de_2} nota(s) de R$ 2,00\n{nota_de_1} nota(s) de R$ 1,00")
