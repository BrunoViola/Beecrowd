eficiencia_de_consumo = 12

tempo_gasto = int(input())
velocidade_media = int(input())

distancia_percorrida = tempo_gasto * velocidade_media

quantidade_litros_necessario = distancia_percorrida/eficiencia_de_consumo

print(f"{quantidade_litros_necessario:.3f}")