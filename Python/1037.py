entrada = float(input())

if entrada < 0 or entrada > 100:
   print('Fora de intervalo')
elif entrada >= 0 and entrada <= 25:
   print('Intervalo [0,25]')
elif entrada <= 50:
   print('Intervalo (25,50]')
elif entrada <= 75:
   print('Intervalo (50,75]')
elif entrada <= 100:
   print('Intervalo (75,100]')