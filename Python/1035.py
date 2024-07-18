entrada = input()

valores = entrada.split()
valores = [int(valor) for valor in valores]

a = valores[0]
b = valores[1]
c = valores[2]
d = valores[3]

somaCD = c+d
somaAB = a+b 

verifica_b_maior_c = True if b>c else False
verifica_d_maior_a = True if d>a else False
verificar_a_par = True if a%2==0 else False
verifica_c_d_positivos = True if c>0 and d>0 else False

if verifica_b_maior_c and verifica_d_maior_a and somaCD>somaAB and verifica_c_d_positivos and verificar_a_par:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
