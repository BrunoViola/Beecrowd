tamanho = int(input())

tamanho *= tamanho

verifica_se_par = True if tamanho%2==0 else False

if verifica_se_par: #se for par, o número de casas brancas e pretas será igual
    print(f"{tamanho//2} casas brancas e {tamanho//2} casas pretas")
else: #se for ímpar, o número de casas brancas será maior em uma unidade
    print(f"{(tamanho//2)+1} casas brancas e {tamanho//2} casas pretas")