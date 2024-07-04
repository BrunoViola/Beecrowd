nome = input()
salario_fixo = float(input())
total_de_vendas = float(input())

salario = salario_fixo + (total_de_vendas*0.15)

print(f'TOTAL = R$ {salario:.2f}')