faixa_isento = 2000.0
primeira_faixa_desconto = 1000.0
segunda_faixa_desconto = 1500.0

salario = float(input())
auxiliar_calculo = salario

if salario <= faixa_isento:
    print("Isento")
else:
    if salario >= 2000.01 and salario <= 3000.0:
        auxiliar_calculo -= faixa_isento
        imposto_total = auxiliar_calculo * 0.08

    elif salario >= 3000.01 and salario <= 4500.0:
        auxiliar_calculo -= faixa_isento
        auxiliar_calculo -= primeira_faixa_desconto
        imposto_total = primeira_faixa_desconto*0.08 + auxiliar_calculo * 0.18

    else:
        auxiliar_calculo -= faixa_isento
        auxiliar_calculo -= primeira_faixa_desconto
        auxiliar_calculo -= segunda_faixa_desconto
        imposto_total = primeira_faixa_desconto*0.08 + segunda_faixa_desconto*0.18 + auxiliar_calculo * 0.28

    print(f"R$ {imposto_total:.2f}")