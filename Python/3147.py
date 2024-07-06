entrada = input()

valores = entrada.split()

valores = [int(valor) for valor in valores]
bem = valores[0]+valores[1]+valores[2]
mal = valores[3]+valores[4]

if bem>=mal:
    print('Middle-earth is safe.')
else:
    bem = bem + valores[5]
    if bem>mal:
         print('Middle-earth is safe.')
   
    else:
        print('Sauron has returned.')